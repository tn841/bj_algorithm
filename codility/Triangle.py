A=[1000000, 1000001, 1000002]
if len(A) < 3:
    print 0
A.sort()
# print(A)

for i in range(len(A) - 2):
    # print(i)
    P = i
    Q = i + 1
    R = i + 2

    # print(((A[P] + A[R]) / 2))
    # if ((A[P] + A[R]) / 2) < A[Q]:
    #     return 1
    if A[P] + A[Q] > A[R] and A[Q] + A[R] > A[P] and A[R] + A[P] > A[Q]:
        return 1

if i == len(A) - 3:
    return 0