for index, row in df.iterrows():

    # no pattern found
    if len(row[candle_names]) - sum(row[candle_names] == 0) == 0:
        # df.loc[index,'candlestick_pattern'] = "NO_PATTERN"
        # df.loc[index, 'candlestick_match_count'] = 0
        print('NO candle found')

    # single pattern found
    elif len(row[candle_names]) - sum(row[candle_names] == 0) == 1:

        # bull pattern 100 or 200
        if any(row[candle_names].values > 0):
            print('1 BULL candle found')

        # bear pattern -100 or -200
        else:
            print('1 BEAR candle found')

            # multiple patterns matched -- select best performance
    else:
        # filter out pattern names from bool list of values
        patterns = list(compress(row[candle_names].keys(), row[candle_names].values != 0))
        container = []
        for pattern in patterns:
            if row[pattern] > 0:
                # container.append(pattern + '_Bull')
                print('multiple BULL candles found')
            else:
                # container.append(pattern + '_Bear')
                print('multiple BEAR candles found')

        rank_list = [candle_rankings[p] for p in container]

# # //@version=4
# # study("MACD")
# # fast = 12, slow = 26
# # fastMA = ema(close, fast)
# # slowMA = ema(close, slow)
# # macd = fastMA - slowMA
# # signal = sma(macd, 9)
# # plot(macd, color=color.blue)
# # plot(signal, color=color.orange)
#
#
#
# fast = 12
# slow = 26
