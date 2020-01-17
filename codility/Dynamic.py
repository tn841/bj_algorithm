A = [-1, -1, -1, -2, -3, -4, -5, -1, -1, 6, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9]
# A = [1, -2, 0, 9, -1, -2]

dp = [-1000000000] * len(A)
dp[0] = A[0]

for n in range(0, len(A)):
    print("n : {}".format(n))
    for i in range(1, 7):
        next_idx = n + i # 1~6

        if next_idx > len(A)-1:
            break
        print("A[{}] = {}".format(next_idx, A[next_idx]))
        sum = dp[n] + A[next_idx]
        if sum > dp[next_idx]:
            dp[next_idx] = sum
        print(dp)
        print ""

print dp[len(A)-1]

