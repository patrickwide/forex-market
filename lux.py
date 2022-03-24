if not df['in_uptrend'][previous_row_index] and df['in_uptrend'][last_row_index]:
    print("changed to uptrend!")
    print("Checking for BUY signals")

    if df['ENGULFING'][last_row_index] == 100 or df['HAMMER'][last_row_index] == 100:  # FROM DOWN TREND TO UP TREND
        print("R1", df['R1'][last_row_index] - df['close'][last_row_index])
        print("S1", df['S1'][last_row_index] - df['close'][last_row_index])

        print('BUY here')

elif df['in_uptrend'][last_row_index]:  # UP TREND
    print("In uptrend!")
    print("Checking for BUY signals")

    if df['ENGULFING'][last_row_index] == 100 or df['HAMMER'][last_row_index] == 100:  # FROM DOWN TREND TO UP TREND
        print("R1", df['R1'][last_row_index] - df['close'][last_row_index])
        print("S1", df['S1'][last_row_index] - df['close'][last_row_index])

        print('BUY here')

if df['in_uptrend'][previous_row_index] and not df['in_uptrend'][last_row_index]:
    print("Change to downtrend!")
    print('Checking for SELL signals')

    if df['ENGULFING'][last_row_index] == 100 or df['HAMMER'][last_row_index] == 100:  # FROM DOWN TREND TO UP TREND
        print("R1", df['R1'][last_row_index] - df['close'][last_row_index])
        print("S1", df['S1'][last_row_index] - df['close'][last_row_index])

        print('SELL here')

elif not df['in_uptrend'][last_row_index]:
    print("In downtrend!")
    print('Checking for SELL signals')

    if df['ENGULFING'][last_row_index] == 100 or df['HAMMER'][last_row_index] == 100:  # FROM DOWN TREND TO UP TREND
        print(df['ENGULFING'][last_row_index])
        print(df['HAMMER'][last_row_index])
        print("R1", df['R1'][last_row_index] - df['close'][last_row_index])
        print("S1", df['S1'][last_row_index] - df['close'][last_row_index])

        print('SELL here')

# from pyine import convert
# _ = convert("pine.pine")
#
# print("done")
#
# #
# # length = 50
# # show_fcast = True
# #
# # dash_loc = "Top Left"
# #
# # texxt_size = 'Large'
# #
# # txt_col = 'red'
# #
# # barssince_ph = 0
# # barssince_pl = 0
# # rchange_ph = 0
# # rchange_pl = 0
# #
# #
# # n = 'bar_index'
# # dt = round(time-time[1])
# #
# #
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
