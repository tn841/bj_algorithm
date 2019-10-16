# -*- coding : utf-8 -*-

tc = int(input())
numbers = list()
for n in range(tc):
    numbers.append(int(input()))

# print numbers

d_arr = [0, 1, 2, 4]

def func1(idx):
    if idx <= 3:
        return d_arr[idx]
    else:
        return func1(idx-1) + func1(idx-2) + func1(idx-3)


for num in numbers:
    if num <= 3 :
        print d_arr[num]
    else:
        print func1(num)



