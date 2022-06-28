# -*- coding: utf-8 -*-
"""
function repository

"""
#%% Import libraries


import numpy as np
import pandas as pd

def fatigue_strength_calc(df, choice_material):

    temp_df = df.reset_index()
    # temp_df.reset_index(inplace=True)
    temp_df = temp_df.rename(columns = {'index':'exposure time'})

    #make lists
    list_exposure_time = list(temp_df['exposure time'])
    list_fatigue_strength = []

    for t in list_exposure_time:
      #Material specific evaluation
        if choice_material == "S355":
            a6 = 0.0637
            a5 = -1.6301
            a4 = 16.426
            a3 = -82.866
            a2 = 221.02
            a1 = -307.38
            list_fatigue_strength.append(a6*np.power(t,6)
                                         + a5*np.power(t,5)
                                         + a4*np.power(t,4)
                                         + a3*np.power(t,3)
                                         + a2*np.power(t,2)
                                         + a1*np.power(t,1) + 343.12)
            
        elif choice_material == "Carbon steel":
            a6 = 0.0563
            a5 = -1.4789
            a4 = 15.279
            a3 = -78.475
            a2 = 209.13
            a1 = -281.56
            list_fatigue_strength.append(a6*np.power(t,6)
                                         + a5*np.power(t,5)
                                         + a4*np.power(t,4)
                                         + a3*np.power(t,3)
                                         + a2*np.power(t,2)
                                         + a1*np.power(t,1) + 278.45)

    temp_df['Fatigue strength'] = list_fatigue_strength
    
    return list_fatigue_strength
