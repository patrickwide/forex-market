import matplotlib.pyplot as plt
import numpy as np
from home import supertrend
from home import technical_analisis
from home import pattern
from home import label
import pandas as pd


def run(df=data):
    df=df
    supertrend(df)
    technical_analisis(df)
    pattern(df)
    label(df)
    df.to_csv('final_3.csv')
    return df
data = pd.read_csv('tesla.csv')

print(run(data))






























# df = pd.read_csv('final_2.csv')
#
# # df.loc[df['label'] == 1, "foo"] = df['close']
# # print(df['foo'])
# #
#
#
# # df.loc[(df['label'] == 1) | (df['label'] == -1), 'foo'] = df['close']
# # df.loc[(df['label'] == 0), 'foo'] = 0
# #
# #
# # print(df['foo'])
#
