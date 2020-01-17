N = int(input())
A = list(map(int, input().split(" ")))

M = int(input())
A2 = list(map(int, input().split(" ")))

# print("N : {}".format(N))
# print("A : {}".format(A))
#
# print("M : {}".format(M))
# print("A2 : {}".format(A2))

result_list = [0] * N
A.sort()

# print("A.sort() : {}".format(A))
for idx, m in enumerate(A2):

    beg = 0
    end = N-1
    # print("m:{}, beg:{}, end:{}".format(m, beg, end))

    while beg <= end:
        mid = int((beg + end) / 2)
        # print("mid : {}".format(mid))


        if A[mid] == m:
            # print("A[{}] == m => {} == {}".format(mid, A[mid], m))
            # result_list[idx] = 1
            print(1)
            break
        elif beg == end:
            print(0)
            break
        elif A[mid] > m:
            end = mid
        else:
            beg = mid + 1
    # print("")

# for num in result_list:
#     print(num)