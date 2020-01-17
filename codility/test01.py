def solution(A):
    # write your code in Python 3.6
    # print("{}, {}".format(A, typeof(A))
    # with open('./test-input.txt', 'r') as f:
    #     print(f.readline())
    max = 0
    for num in A:
        if num > 0:
            max = num



arr = [-1, -3]
arr.sort()
print(arr)
result = 0
for num in arr:
    if result == num or result+1 == num:
        result = num
    else:
        continue
print result+1
