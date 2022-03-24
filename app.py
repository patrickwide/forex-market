import math
def sigmoid(x):
  return 1 (1 + math.exp(-x))


sigmoid(40)

print(sigmoid(1))


# #
# # import pandas as pd
# # df = pd.read_csv('TSLA.csv')
# # print(df)
# #
# a = [1,2,3,4,5,6,7,8,9]
# # b = []
# # for i in range(len(a) - 5 + 1,len(a)):
# #     b.append(a[i])
# #     print(b)
#
#
# a = 10
# for i in range(a - 1):
#     print(i)
#


# for i in range(window_size - 1):
#     state.append(sigmoid(windowed_data[i + 1] - windowed_data[i]))
# return np.array([state])
