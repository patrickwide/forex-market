import talib
import yfinance as yf
import panda_learn as pd

data = pd.read_csv('TRY_DATA.csv')#yf.download("SPY", start="2020-01-01", end="2020-08-01")

morning_star = talib.CDLMORNINGSTAR(data['Open'], data['High'], data['Low'], data['Close'])

engulfing = talib.CDLENGULFING(data['Open'], data['High'], data['Low'], data['Close'])
doji = talib.CDLDRAGONFLYDOJI(data['Open'], data['High'], data['Low'], data['Close'])

data['Morning Star'] = morning_star
data['Engulfing'] = engulfing
data['Doji'] = doji

engulfing_days = data[data['Engulfing'] != 0]
morning_star = data[data['Morning Star'] != 0]
doji = data[data['Doji'] != 0]



print(doji.head(-1))