import pandas as pd
import warnings
import numpy as np
warnings.filterwarnings('ignore')



data = pd.Series([1,2,3],index=['a',',b','c'])
try:
    print(data[:1])
except:
    print('no data found')



















#
# data = pd.Series()
# #
# print(data)
#
# data = np.array(['a','b','c','d'])
# data = pd.Series(data,index=[5,4,3,2])
#
# print(data)



# data = {'a':1.,
#         'b':2.,
#         "c":3.
#         }
#
# print(pd.Series(data,index=['d','c','a']))


