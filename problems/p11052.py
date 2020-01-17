#-*- coding:utf-8 -*-
"""
2019-10-16
- 부분의 최적이 전체의 최적이다.
- o(n^2)
- 해설먼저 보고 풀었음
"""
dp_list = [0]*1001

card_N = int(input())

pack_str = raw_input()
pack_list = map(int, pack_str.split())
pack_list.insert(0, 0)
# print pack_list

for i in range(0, card_N+1):
    # print ">> i:{}".format(i)
    temp_list = []
    for j in range(0, (i/2)+1):
        if j == 0:
            # print "list[{}]".format(i)
            temp_list.append(pack_list[i])
        else:
            temp_list.append(dp_list[i-j] + dp_list[j])
            # print "dp[{}] + dp[{}]".format(i-j, j)
    dp_list[i] = max(temp_list)
    # print "max:{}".format(dp_list[i])
    # print ""

    # print ""

print dp_list[card_N]