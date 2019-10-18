import os
import pickle

import pandas as pd
import numpy as np

# sklearn package supports a plenty of methods
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import SGDClassifier  # svm

# grid search
from sklearn.model_selection import GridSearchCV
from pprint import pprint
from time import time

"""
=====
This code only for demonstrating the workflow of applying SVM in NLP
This is only a part of the whole program, so it can not be executed properly without data
=====
"""


def tokenize(txt):
    """Tokenize by whitespace."""
    return txt.split()


def scores(row):
    """Map textual sentiment categories to numbers in pandas df."""
    if row["cla"] == "neutral":
        val = 0
    elif row["cla"] == "positive":
        val = 1
    else:
        val = -1

    return val


def balanced_subsample(pre_balance_x, pre_balance_y, subsample_size_coef=1.0, balance_seed=None):
    """
    Create a balanced subsample with upsampling.
    :param pre_balance_x: Sample X, pre-balance
    :param pre_balance_y: Sample y, pre-balance
    :param subsample_size_coef: Choosing the coefficient to define max number of oversampling
    :param balance_seed: for random module
    :return: DataFrame, size = (max_elems * subsample_size_coef * 3, 2), includes pos, neutral, negative sentiment samples_uni_sentiment
    """

    # Create a DataFrame to contain the samples of each fold to do the oversampling
    pre_balance_data = pd.concat([pre_balance_x, pre_balance_y], axis=1)
    max_elems = pre_balance_data.sentiment.value_counts().values.max()
    sample_out_data = pd.DataFrame()

    for sent in pre_balance_data['sentiment'].unique():
        samples_uni_sentiment = pre_balance_data[pre_balance_data.sentiment == sent]
        # print(samples_uni_sentiment.sentiment.unique())
        num_dup = int(max_elems * subsample_size_coef - len(samples_uni_sentiment))
        # print(num_dup)
        dup_samples = samples_uni_sentiment.sample(n=num_dup, random_state=balance_seed, axis=0, replace=True)
        # print(len(dup_samples))
        print(dup_samples)
        sample_out_data = pd.concat([sample_out_data, dup_samples], axis=0)

    balanced_data = pd.concat([pre_balance_data, sample_out_data], axis=0)
    # count_ = balanced_data.sentiment.value_counts()  # check 3 sentiments have the same size after oversampling
    return balanced_data


def customize_cross_validation(pre_fold_y, pre_fold_X, folds, seed):
    """
    Stratified k-fold cross-validation with oversampling.
    :param pre_fold_y: Series, marked as -1, 0, 1
    :param pre_fold_X: Series, text information
    :param folds: number of folds for the cross-validation
    :param seed: set for random module
    :return: Nested list, shape = (5 folds * 2 sets)
            2 sets = [balanced_sample_size of training set, balanced_sample_size of test set]
    """
    # Instance of StratifiedKFold
    skf = StratifiedKFold(n_splits=folds, shuffle=True, random_state=seed)
    custom_cv = []

    # Standard way to
    for train_index, test_index in skf.split(pre_fold_X, pre_fold_y):
        print(test_index)
        print(train_index)

        X_train, X_test = pre_fold_X[train_index], pre_fold_X[test_index]
        y_train, y_test = pre_fold_y[train_index], pre_fold_y[test_index]

        balanced_train_samples = balanced_subsample(pre_balance_x=X_train, pre_balance_y=y_train, balance_seed=seed)
        balanced_test_samples = balanced_subsample(pre_balance_x=X_test, pre_balance_y=y_test, balance_seed=seed)

        # attach all the indices of each folds, training set and test set
        balanced_index = [list(balanced_train_samples.index), list(balanced_test_samples.index)]
        custom_cv.append(balanced_index)

    return custom_cv


# change directory
direct_code = '/Users/hujunjie/Desktop/CodeBase/NasdaqSentiment/'
direct_data = '/Volumes/JeremyHu/DataBase/NasdaqSentiment/data/'

os.chdir(direct_data + "financial_phrase_bank/")

# load phrasebank
phrasebank = pickle.load(open("lem_Sentences_66Agree.p", "rb"))

phrase_bank_data = pd.DataFrame(np.transpose(phrasebank), columns=['lemma', 'cla'])
# phrase_bank_data['ident'] = phrase_bank_data.index
phrase_bank_data["sentiment"] = phrase_bank_data.apply(scores, axis=1)

# setup
seed = 123  # seed for generating random number
folds = 5  # choosing 5 folds for cross-validation

# CountVectorizer
stop_words = (None, 'english')
max_df = (0.85, 0.90, 0.95, 1.0)
min_df = (0.00, 0.01, 0.05, 0.1)
ngram_range = ((1, 1), (1, 2))
sublinear_tf = (True, False)

# TfidfTransformer
use_idf = (True, False)
norm = ('l1', 'l2')

# SGDClassifier
alpha = (0.005, 0.001, 0.0005, 0.0001, 0.00005, 0.00001, 0.000005, 0.000001)
loss = ('hinge', 'log', 'squared_hinge', 'perceptron')  # loss function methods
penalty = (None, 'l1', 'l2', 'elasticnet')

# obtain cross validation set
sample_lemma = phrase_bank_data["lemma"]
sample_sentiment = phrase_bank_data["sentiment"]

custom_cross_validation = customize_cross_validation(pre_fold_y=sample_sentiment, pre_fold_X=sample_lemma, folds=folds,
                                                     seed=seed)

piper = Pipeline([("vect", CountVectorizer(tokenizer=tokenize)),
                  ("tfidf", TfidfTransformer()),
                  ("clf", SGDClassifier(shuffle=True,
                                        n_iter=80,
                                        random_state=seed)),
                  ])

parameters = {
    # CountVectorizer param
    'vect__ngram_range': ngram_range,
    'vect__stop_words': stop_words,
    'vect__max_df': max_df,
    'vect__min_df': min_df,
    'tfidf__sublinear_tf': sublinear_tf,
    # TfidfTransformer param
    'tfidf__use_idf': use_idf,
    'tfidf__norm': norm,
    'clf__alpha': alpha,
    # SGDClassifier param
    'clf__penalty': penalty,
    'clf__loss': loss,
}

grid_search = GridSearchCV(piper, parameters, n_jobs=-1, verbose=1, refit=True, cv=custom_cross_validation)

print("Performing grid search...")
print("pipeline:", [name for name, _ in piper.steps])
print("parameters:")
pprint(parameters)
t0 = time()
grid_search.fit(sample_lemma, sample_sentiment)
print("done in %0.3fs" % (time() - t0))

print("Best score: %0.3f" % grid_search.best_score_)
print("Best parameters set:")
best_parameters = grid_search.best_estimator_.get_params()
for param_name in sorted(parameters.keys()):
    print("\t%s: %r" % (param_name, best_parameters[param_name]))

# set pipeline to best model from grid search
piper = grid_search.best_estimator_

# save best parameters
direct = "/Volumes/JeremyHu/DataBase/NasdaqSentiment/output/model"
os.chdir(direct)

# extract weights from sgdclassifier
piper_fit = piper.fit(sample_lemma, sample_sentiment)

sgd_fit = piper_fit.steps[2][1]
sgd_ws = getattr(sgd_fit, 'coef_')

# extract classes from sgdclassifier
sgd_ws_classes = getattr(sgd_fit, 'classes_')

# extract feature names from count vectorizer
feature_names = piper_fit.steps[0][1].get_feature_names()

# construct pandas df

res = pd.DataFrame({"w_neg": pd.Series(sgd_ws[0]),
                    "w_neu": pd.Series(sgd_ws[1]),
                    "w_pos": pd.Series(sgd_ws[2]),
                    "lab": pd.Series(feature_names),
                    })

os.chdir(direct + "tmp")

res.to_csv("sgd_weights.csv", sep=';')

piper_fit = piper.fit(sample_lemma, sample_sentiment)

with open("œsupervised_model_1708.p", 'wb') as piper_file_out:
    pickle.dump(piper_fit, piper_file_out)

print("Training Completed")
