#-*- coding:utf-8 -*-
"""
2019-10-15
- dp배열이용
- 부분 최적이 전체 최적
"""
dp_arr = [0]*1001
dp_arr[0] = 0
dp_arr[1] = 1
dp_arr[2] = 3
dp_arr[3] = 5
num = int(input())

for n in range(1, num+1):
    if n <= 3:
        continue
    else:
        dp_arr[n] = dp_arr[n-1] + dp_arr[n-2] + dp_arr[n-2]

print dp_arr[num] % 10007
