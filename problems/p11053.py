#-*- coding:utf-8 -*-
"""
2019-10-15
"""
num_list = [0]*1001
dp_list = [1]*1001

size = int(input())
num_str = raw_input()

tmp_list = num_str.split()
for n in range(size):
    num_list[n] = tmp_list[n]

# print '{}'.format(num_list)

for i in range(1, size+1):
    for j in range(0, i):
        # print "i:{}, j:{}".format(i, j)
        if int(num_list[i]) > int(num_list[j]) and int(dp_list[i]) < int(dp_list[j]) + 1:
            dp_list[i] = int(dp_list[j]) + 1
            # print "dp[{}] = {}".format(i, dp_list[i])

max = 0
for n in range(size+1):
    if max < dp_list[n]:
        max = dp_list[n]

# print "{}".format(dp_list)

print max