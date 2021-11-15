"""
INPUT DATA MANIPULATION
"""

import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

df = pd.read_csv(os.getcwd()+ '/DEDA_HMM/HeartWatch-Details-20201002-to-20201228.csv', na_values=['NaN'])
df.head(5)

date_list = [x[:-6] for x in df['ISO'].tolist()]
df['Timestamp'] = pd.to_datetime(date_list)
df.set_index('Timestamp', inplace=True)
df.head(5)
print(df.shape)

print("The number of non-missing (i.e., valid) values in 'Schlaf': \t", df["Schlaf"].notna().sum())
print("The number of non-missing (i.e., valid) values in 'HF wenn inaktiv': \t", df["HF wenn inaktiv"].notna().sum())
print("The number of non-missing (i.e., valid) values in 'Gehen': \t", df["Gehen"].notna().sum())
print("The number of non-missing (i.e., valid) values in 'Trainings': \t", df["Trainings"].notna().sum())
print("The number of non-missing (i.e., valid) values in 'Max-%': \t", df["Max-%"].notna().sum())
print("The number of non-missing (i.e., valid) values in 'Notizen': \t", df["Notizen"].notna().sum())

df["Gehen"] = df["Gehen"].fillna(0)  # nan is replaced with 0
df["HF wenn inaktiv"] = df["HF wenn inaktiv"].fillna(0)
df.drop(['ISO', 'Datum', 'Zeit', 'Schlaf', 'Trainings',  'Max-%', 'Notizen'], axis='columns', inplace=True)
df['Typ'].value_counts(dropna=False)

df['Typ'] = df['Typ'].map({'hoher ruhefaktor':0, 'ruhend':1, 'erhöht':2, 'niedrig':3})
df.head(10)

df.info()
df.describe()

fig, ax = plt.subplots(3,1, figsize=(15,30))
ax[0].scatter(df.index, df['bpm'], c=df['HF wenn inaktiv'], s=2, cmap='rainbow')
ax[1].scatter(df.index, df['bpm'], c=df['Gehen'], s=2, cmap='rainbow')
ax[2].scatter(df.index, df['bpm'], c=df['Typ'], s=2, cmap='rainbow')
ax[2].set_xlabel('Timestamp')
ax[0].set_title('Heart Rate with different conditions of "HF wenn inaktiv" (purple:0, red:1)')
ax[1].set_title('Heart Rate with different conditions of "Gehen (Going)" (purple:0, red:1)')
ax[2].set_title('Heart Rate with different conditions of "Typ" \n (hoher ruhefaktor:purple, ruhend:blue, erhöht:yellow, niedrig:red)')
fig.savefig(os.getcwd() + "/DEDA_HMM/Raw data visualization.png", dpi = 300, transparent=True)
plt.show()

print("The minimum bpm when 'Gehen(Goinig)=1' is: \t", df[df['Gehen']==1].min().bpm)

zoom = df.loc['2020-10-17 7:00': '2020-10-25 02:00'] #for inspecting missing data
fig, ax = plt.subplots(3,1, figsize=(15,30))
ax[0].plot(zoom.index, zoom['bpm'], linestyle='-', c='grey')
ax[0].scatter(zoom.index, zoom['bpm'], c=zoom['HF wenn inaktiv'],s=10, cmap='rainbow')
ax[1].plot(zoom.index, zoom['bpm'], linestyle='-', c='grey')
ax[1].scatter(zoom.index, zoom['bpm'], c=zoom['Gehen'], s=10, cmap='rainbow')
ax[2].plot(zoom.index, zoom['bpm'], linestyle='-', c='grey')
ax[2].scatter(zoom.index, zoom['bpm'], c=zoom['Typ'], s=10, cmap='rainbow')
ax[2].set_xlabel('Timestamp')
ax[0].set_title('Heart Rate with different conditions of "HF wenn inaktiv" (purple:0, red:1)')
ax[1].set_title('Heart Rate with different conditions of "Gehen (Going)" (purple:0, red:1)')
ax[2].set_title('Heart Rate with different conditions of "Typ" \n (hoher ruhefaktor:purple, ruhend:blue, erhöht:yellow, niedrig:red)')

plt.show()

df.loc['2020-10-17 08:30':'2020-10-25 01:10']

"""
DATA PREPROCESSING
"""

print("Is the index label unique? (i.e, no duplicate index labels): \n", df.index.is_unique)

temp1 = df['bpm'].groupby(level=0).mean()
temp2 = df[['HF wenn inaktiv', 'Gehen', 'Typ']].groupby(level=0).agg(lambda x:x.value_counts().index[0]) #mode
print(temp1.head(5))
print(temp2.head(5))

df = pd.concat([temp1, temp2], axis=1)
print("Is the index label unique? (i.e, no duplicate index labels): \n", df.index.is_unique)
df.head(10)

min_index = df.index.min()
max_index = df.index.max()
print(min_index)
print(max_index)

reg_period = pd.date_range(min_index, max_index, freq='S') #'T'='min', 'S': sec.
reg_period

df = df.reindex(reg_period)
df.head(5)

temp1 = df['bpm'].resample('5T').mean()
temp2 = df[['HF wenn inaktiv', 'Gehen', 'Typ']].resample('5T').agg(lambda x: x.value_counts().index[0] if len(x.value_counts().index)>0 else np.nan) #mode

df = pd.concat([temp1, temp2], axis=1)
df.head(5)

print(temp1.isna().sum())
print(temp2.isna().sum())

zoom1 = df.loc['2020-10-25 00:00': '2020-10-26 00:00', 'bpm']
zoom2 = df.loc['2020-10-27 00:00': '2020-10-28 00:00', 'bpm']
zoom3 = df.loc['2020-10-29 00:00': '2020-10-30 00:00', 'bpm']
zoom4 = df.loc['2020-10-31 00:00': '2020-11-01 00:00', 'bpm']
fig, ax = plt.subplots(4,1, figsize=(15,12))
ax[0].plot(zoom1.index, zoom1, linestyle='-', c='green', linewidth = 2)
ax[1].plot(zoom2.index, zoom2, linestyle='-', c='red', linewidth = 2)
ax[2].plot(zoom3.index, zoom3, linestyle='-', c='blue', linewidth = 2)
ax[3].plot(zoom4.index, zoom4, linestyle='-', c='purple', linewidth = 2)
ax[0].set_title('Time series of the specific day')
ax[3].set_xlabel('Timestamp')
plt.show()

df['Hour'] = df.index.hour
df['Minute'] = df.index.minute

df_daily_bpm = df[['bpm', 'Hour', 'Minute']].groupby(['Hour', 'Minute']).mean() #Now df_daily has MultiIndex([(0,  0),...,(0, 45)],names=['Hour', 'Minute'])
df_daily_bpm_std = df[['bpm', 'Hour', 'Minute']].groupby(['Hour', 'Minute']).std() #Now df_daily has MultiIndex([(0,  0),...,(0, 45)],names=['Hour', 'Minute'])

temp1 = df_daily_bpm + 1.96*df_daily_bpm_std
temp2 = df_daily_bpm - 1.96*df_daily_bpm_std

print(df_daily_bpm.shape)

fig, ax = plt.subplots(figsize=(12,10))
temp1.plot(label='Mean + 1.96*SD', ax = ax)
df_daily_bpm.plot(label='Mean', ax = ax)
temp2.plot(label='Mean - 1.96*SD', ax = ax)
ax.set_title('Everage daily behavior')
ax.set_yticks([60, 80, 100, 120, 140])
plt.legend(['Mean + 1.96*SD','Mean', 'Mean - 1.96*SD'])
plt.show()

low = 25
up = 75

df_daily_bpm_low = df[['bpm', 'Hour', 'Minute']].groupby(['Hour', 'Minute']).quantile(low/100) #Now df_daily has MultiIndex([(0,  0),...,(0, 45)],names=['Hour', 'Minute'])
df_daily_bpm_Q50 = df[['bpm', 'Hour', 'Minute']].groupby(['Hour', 'Minute']).quantile() #Now df_daily has MultiIndex([(0,  0),...,(0, 45)],names=['Hour', 'Minute'])
df_daily_bpm_up = df[['bpm', 'Hour', 'Minute']].groupby(['Hour', 'Minute']).quantile(up/100) #Now df_daily has MultiIndex([(0,  0),...,(0, 45)],names=['Hour', 'Minute'])


fig, ax = plt.subplots(figsize=(12,10))
df_daily_bpm_up.plot(label=r'$97.5^{th}$ Quantile', ax = ax)
df_daily_bpm_Q50.plot(label='Median', ax = ax)
df_daily_bpm_low.plot(label=r'$2.5^{th}$ Quantile', ax = ax)

plt.title('Everage daily behavior')
ax.set_yticks([60, 80, 100, 120, 140])
plt.legend([ str(up)+r'$^{th}$ Quantile','Median',str(low)+r'$^{th}$ Quantile'])
plt.show()

df_daily_bpm_Q50

df = df.loc['2020-10-25 01:03:16':]

df_isna = df[df['bpm'].isna()] #choose the missing data that needs replacement by dictionary of df_daily_bpm_Q50
## df_isna is a "copy" of slice from df, then any alternation of df_isna cannot influence df itself
print(df_isna.index)
df_isna.head(5)

df.loc[df['bpm'].isna(), 'bpm']  = df_daily_bpm_Q50.loc[[(i, j) for i, j in zip(df_isna['Hour'].values, df_isna['Minute'].values)]].values
print("Number of missing data for each variable is now:\n",df.isna().sum(axis=0))

df["HF wenn inaktiv"].fillna(method='ffill', inplace=True)
df["Gehen"].fillna(method='ffill', inplace=True)

df.loc[df['Typ'].isna(), 'Typ'] = df.loc[df['Typ'].isna(), 'bpm'].map(lambda x: 3 if x<50 else (1 if x<80 else (0 if x<100 else 2)))
print("Number of missing data for each variable is now:\n",df.isna().sum(axis=0))

df.info()

df.describe()

zoom = df#.loc['2020-11-11 00:00': '2020-11-12 00:00']  # '2020-11-10 '
fig, ax = plt.subplots(3,1, figsize=(15,15))
ax[0].plot(zoom.index, zoom['bpm'], linestyle='-', c='grey', linewidth = 0.2)
ax[0].scatter(zoom.index, zoom['bpm'], c=zoom['HF wenn inaktiv'],s=2, cmap='rainbow')
ax[1].plot(zoom.index, zoom['bpm'], linestyle='-', c='grey', linewidth = 0.2)
ax[1].scatter(zoom.index, zoom['bpm'], c=zoom['Gehen'], s=2, cmap='rainbow')
ax[2].plot(zoom.index, zoom['bpm'], linestyle='-', c='grey', linewidth = 0.2)
ax[2].scatter(zoom.index, zoom['bpm'], c=zoom['Typ'], s=2, cmap='rainbow')
ax[2].set_xlabel('Timestamp')
ax[0].set_title('Heart Rate with different conditions of "HF wenn inaktiv" (purple:0, red:1)')
ax[1].set_title('Heart Rate with different conditions of "Gehen (Going)" (purple:0, red:1)')
ax[2].set_title('Heart Rate with different conditions of "Typ" \n (hoher ruhefaktor:purple, ruhend:blue, erhöht:yellow, niedrig:red)')
plt.show()
fig.savefig(os.getcwd() + "/DEDA_HMM/Clean data visualization (regularized 5min interval).png", dpi = 300, transparent=True)

"""
3. Model training and prediction
"""

from hmmlearn import hmm

Obs = df['bpm'].values.reshape(-1, 1)

Hid_pre_list = []
logprob_list = []
model_list = []

max_components = 6
for s in range(2, max_components + 1):
    ##load model– Gaussian HMM which is Hidden Markov Model with multinomial (discrete) emissions
    model = hmm.GaussianHMM(n_components=s, covariance_type='diag', n_iter=1000, tol=0.001)
    ##Training and Prediction of Hidden states
    model.fit(Obs)

    Hid_pre = model.predict(Obs)
    Hid_pre_list.append(Hid_pre)

    logprob = model.score(Obs)  # log-probability of sequence Obs
    logprob_list.append(logprob)

    model_list.append(model)
    print("The log-probability of Obs. sequence given {} estimated hidden states is \t: {:.10f}".format(s, logprob))

s = 4
model = model_list[s-2]

#Initial state occupation distribution
print(f"The following result show parameter estimates with {s} hidden states: \n\n")
print("Estimated initial state occupation distribution: \n {} \n".format( model.startprob_))
#Matrix of transition probabilities between states.
print("Estimated matrix of transition probabilities between states: \n {} \n".format(model.transmat_ ))
#Probability dist. of emission given each state.
print("Mean parameters of Gaussian assumption for each state \n {}\n".format(model.means_))
print("Covariance parameters of Gaussian assumption for each state \n {}\n".format(model.covars_))

fig, ax = plt.subplots(figsize=(10,7))
ax.plot(list(range(2,max_components+1)),logprob_list)
ax.set_xticks(list(range(2,max_components+1)))
ax.set_xlabel('number of hidden states')
ax.set_ylabel('Largest log-probability of obs. sequence given the estimated model')
plt.show()

Hid_pre_df = np.array(Hid_pre_list).T
Hid_pre_df = pd.DataFrame(np.array(Hid_pre_list).T, columns =['Hid_pre'+str(s) for s in range(2,max_components+1)], index =  df.index)

df2 = pd.concat([df,Hid_pre_df], axis = 1)
df2.head(5)

zoom = df2#['2020-12-14 00:00': '2020-12-15 00:00']  # '2020-11-10 '

fig, ax = plt.subplots(max_components-1, 1, figsize=(15,25))
for s in range(2, max_components+1):
    ax[s-2].plot(zoom.index, zoom['bpm'], linestyle='-', c='grey', linewidth = 0.2)
    ax[s-2].scatter(zoom.index, zoom['bpm'], c=zoom['Hid_pre'+str(s)], s=2, cmap='rainbow')
    ax[s-2].set_xlabel('Timestamp')
    ax[s-2].set_title('GaussianHMM Results: Heart Rate with {} hidden states'.format(s))

plt.show()
plt.close()

Obs = df['bpm'].values.reshape(-1, 1)

Hid_pre_list = []
logprob_list = []

max_components = 6
n_mix = 5  # Number of states in the GMM
# (with considerable large numbers, it can simulate any distribution P({Obs.}|S))

for s in range(2, max_components + 1):
    ##load model– Gaussian HMM which is Hidden Markov Model with multinomial (discrete) emissions
    model = hmm.GMMHMM(n_components=s, n_mix=n_mix, covariance_type='diag', n_iter=500, tol=0.001)
    ##Training and Prediction of Hidden states
    model.fit(Obs)
    print(">> \t Does the algorithm converge? \t", model.monitor_.converged)  # True

    Hid_pre = model.predict(Obs)
    Hid_pre_list.append(Hid_pre)

    logprob = model.score(Obs)  # log-probability of sequence Obs
    logprob_list.append(logprob)
    print("The log-probability of Obs. sequence given {} estimated hidden states is \t: {:.10f}".format(s, logprob))

fig, ax = plt.subplots(figsize=(10,7))
ax.plot(list(range(2,max_components+1)),logprob_list)
ax.set_xticks(list(range(2,max_components+1)))
ax.set_xlabel('number of hidden states')
ax.set_ylabel('log-probability')
ax.set_title('Largest log-probability of obs. sequence given the estimated model')
plt.show()

s = 4
model = model_list[s-2]

#Initial state occupation distribution
print(f"The following result show parameter estimates with {s} hidden states: \n\n")
print("Estimated initial state occupation distribution: \n {} \n".format( model.startprob_))
#Matrix of transition probabilities between states.
print("Estimated matrix of transition probabilities between states: \n {} \n".format(model.transmat_ ))
#Probability dist. of emission given each state.
print("Mean parameters of GMM assumption for each state \n {}\n".format(model.means_))
print("Covariance parameters of GMM assumption for each state \n {}\n".format(model.covars_))

Hid_pre_df = np.array(Hid_pre_list).T
Hid_pre_df = pd.DataFrame(np.array(Hid_pre_list).T, columns =['Hid_pre'+str(s) for s in range(2,max_components+1)], index =  df.index)
df3 = pd.concat([df,Hid_pre_df], axis = 1)
df3.head(5)

zoom = df3#['2020-12-14 00:00': '2020-12-15 00:00']  # '2020-11-10 '

fig, ax = plt.subplots(max_components-1, 1, figsize=(15,25))
for s in range(2, max_components+1):
    ax[s-2].plot(zoom.index, zoom['bpm'], linestyle='-', c='grey', linewidth = 0.2)
    ax[s-2].scatter(zoom.index, zoom['bpm'], c=zoom['Hid_pre'+str(s)], s=2, cmap='rainbow')
    ax[s-2].set_xlabel('Timestamp')
    ax[s-2].set_title('GMM-HMM Results: Heart Rate with {} hidden states'.format(s))

plt.show()
plt.close()
fig.savefig(os.getcwd() + "/DEDA_HMM/GMM-HMM Results- Heart Rate with different number of hidden states.png", dpi = 300, transparent=True)