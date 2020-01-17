#-*- coding:utf-8 -*-
"""
2019-10-14
- 피보나치
- for문과 dp배열 이용하여 단일 for문으로 해결해야 시간초과가 안난다.
"""
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