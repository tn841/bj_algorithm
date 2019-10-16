#-*- coding:utf-8 -*-

num = int(input())

d_arr = [0] * 1001
d_arr[0] = 0
d_arr[1] = 1
d_arr[2] = 2
d_arr[3] = 3

for n in range(0, num+1):
    if n <= 3:
        continue
    d_arr[n] = d_arr[n-2] + d_arr[n-1]

print d_arr[num] % 10007