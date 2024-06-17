import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd
from matplotlib import cm
import matplotlib.cbook as cbook
import matplotlib.colors as colors
import copy
from scipy.signal import find_peaks
from scipy.optimize import curve_fit
import scipy.stats as stats
from sklearn.metrics import r2_score
import random
my_cmap = copy.copy(cm.get_cmap('magma'))
my_cmap.set_bad(my_cmap.colors[0])
plt.rcParams['axes.labelsize'] = 18
plt.rcParams['axes.titlesize'] = 18
plt.rcParams['legend.fontsize'] = 16
plt.rcParams['xtick.labelsize'] = 16
plt.rcParams['ytick.labelsize'] = 16
plt.rcParams['figure.figsize'] = 12,7
plt.rcParams['figure.autolayout'] = True

#data_int = pd.read_csv('Test Sequence.csv', delimiter = ',', header = None)
#print(data_int)

data_int = pd.read_csv('RandomRun8_input_2.csv', delimiter = ',')
#print(data_int)

data_SA = data_int[data_int.iloc[:,0].str.contains('SA', regex = False)]
data_SA_array = np.array(data_SA)
SA_col = data_SA.columns
#print(data_SA)
#print("before reset index", data_SA)
data_SA = data_SA.reset_index()
#print("after reset index", data_SA)
#print(type(data_SA.iloc[:,0]))

    # For Paired Shuffling
# S=[[data_SA_array[z*2+y] for y in range(2)] for z in range(len(data_SA_array)//2)]
# random.shuffle(S)
# L2=[]
# for x in S:
#     for y in x:
#         L2.append(y)
# print(L2)
# data_SA_shuff_df = pd.DataFrame(L2)
# print(data_SA_shuff_df)

    # For Simple shuffling
data_SA_arr_list = [data_SA_array[k] for k in range(len(data_SA_array))]
random.shuffle(data_SA_arr_list)

data_SA_shuff_df = pd.DataFrame(data_SA_arr_list)
data_SA_shuff_df_conc = pd.concat([data_SA_shuff_df, data_SA.iloc[:,0]], axis = 1)
#print(data_SA_shuff_df_conc)
data_SA_indexed = data_SA_shuff_df_conc.set_index('index')
data_SA_indexed.columns = SA_col
#print(data_SA_indexed)


data_QC = data_int.iloc[:,0].str.contains('M|QC|BLK')
#print(data_QC)

data_QC_index = []
for k in range(len(data_QC)):
    if k <= len(data_QC) - 2:
        if data_QC[k] == data_QC[k+1] or data_QC[k] == data_QC[k-1]:
            if data_QC[k] == True:
                data_QC_index.append(k)
    else:
        if data_QC[k] == data_QC[k-1]:
            if data_QC[k] == True:
                data_QC_index.append(k)

#print(data_QC_index)
data_QC_df = data_int.iloc[data_QC_index]
#print(data_QC_df)


random_data = pd.concat([data_SA_indexed, data_QC_df])
rand_sorted_data = random_data.sort_index()
#print(rand_sorted_data)
rand_sorted_data.to_csv("RandomOrderRun8_output_test.csv")


    

# %%



