arr = [9,3,9,3,9,7,9]
arr = [1,1,3,1,99,3,1]

arr.sort()
print(arr)
cur_num = 0
arr_len = len(arr)
for idx, num in enumerate(arr):
    if cur_num != num:
        if idx % 2 == 0:
            cur_num = num
            if idx == arr_len -1:
                print(num)
        else:
            print(cur_num)

