import pandas as pd
import talib as ta
import csv
import warnings
import numpy as np
warnings.filterwarnings('ignore')


marketData = pd.read_csv('TRY_DATA.csv')
df = pd.DataFrame(marketData)
