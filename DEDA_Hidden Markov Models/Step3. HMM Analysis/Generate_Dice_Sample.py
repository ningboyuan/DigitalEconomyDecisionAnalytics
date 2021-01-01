#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 10:54:50 2020

@author: Jane Hsieh (Hsing-Chuan, Hsieh)

@article:
    Generate random sample of dice (with Faif and Loaded dice used interchangeably)
"""
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#0. ================================================ Functions ===============================================

def InitialState(pi_0=0.5):
    '''
    function to generate initial state S_0 out of {F,L} of the dice with prob-p(S_0=F) = p(F)=pi_0 (0:F; 1:L)
    Input: 
        pi_0: defaul= 0.5 which is the initial prob of hiddent state p(S_0 = 0)  [0: fair dice; 1: Loaded dice]
                (pi1 := p(S_0 = 1) = 1-pi_0)
    Output:
        S_0: initial generated hidden state
    ''' 
    S_0 = np.random.choice(2, 1, p=[pi_0, 1-pi_0])[0] #Default: replace=True
    return S_0
    

    
def EmitObs(S_t, Dice, pF, pL):
    '''
    function to generate observation O_t according to the mechanism of hidden state S_t --> Emit Observation
    Input:
        S_t: current hidden state
        Dice: face point of dice, e.g., [1,2,...,6]
        pF: distributions of Fair Dice, say, with point = [1,2,...,6]
        pL: distributions of Loaded Dice, say, with point = [1,2,...,6]
    '''
    if S_t == 0:
        #Fair dice state with prob = pF
        O_t = np.random.choice(Dice, 1, replace=True, p=pF)[0]
    if S_t == 1:
        #Loaded dice state with prob = pL
        O_t = np.random.choice(Dice, 1, replace=True, p=pL)[0]
    return O_t


def TransitState(S_t, p01, p10):
    '''
    function to generate the new hidden state S_t according to the mechanism of previous hidden state S_t
    Input:
        S_t: current hidden state
        p01: Transition prob from 0(F) to 1(L)); p00 =  1- p01
        p10: Transition prob from 1(L) to 0(F); p11 = 1-p10
    '''
    if S_t == 0:
        #Fair dice state with prob = pF
        S_new = np.random.choice(2, 1, replace=True, p=[1-p01, p01])[0]
    if S_t == 1:
        #Loaded dice state with prob = pL
        S_new = np.random.choice(2, 1, replace=True, p=[p10, 1-p10])[0]
    return S_new 
    


def GenerateFLDice(N, p01, p10, pL, pF=[1/6 for i in range(6)], Dice = [i+1 for i in range(6)], pi_0=0.5, seed=None):
    '''
    Generate random sample of dice (with predefined Fair(R) and Loaded(L) dice used interchangeably)
    
    Input:
        N: sample size
        seed: random seed– None or int
        Dice: face point of the dice; default = [1,2,...,6]
        pF, pL: distributions of Fair vs Loaded Dice (length of pF, pL must be the same with Dice)
        pi_0: initial probability of hidden state S_0 – p(S_0 = 0)  [0: fair dice; 1: Loaded dice]
        p01, p10: Transition prob of hidden state from 0(F) to 1(L)) & from 1(L) to 0(F), respectively
    Output:
        Sample_S: sequence of hidden states {S_t} from t=0,...,N-1
        Sample_O: sequence of observations {O_t} from t=0,...,N-1

    '''
    np.random.seed(seed) 
    Sample_S = []
    Sample_O = []
    
    t=0
    # Generate initial hidden state S_t & the Observed state O_t out of it
    S_t = InitialState(pi_0)
    O_t = EmitObs(S_t, Dice, pF, pL)
    
    Sample_S.append(S_t)
    Sample_O.append(O_t) 
    
    t += 1
    
    while t < N:        
        #Generate New S_t at next time (i.e., t+1) point according to previous mechanism of S_t; 
        #and O_t out of New S_t
        S_t = TransitState(S_t, p01, p10)
        O_t = EmitObs(S_t, Dice, pF, pL)
        
        Sample_S.append(S_t)
        Sample_O.append(O_t) 
        
        t += 1
        
    return Sample_S, Sample_O
        



