N = int(input())

A = list(map(int, input().split(" ")))
dp = [0] * N
# print(A)
dp[0] = A[0]
for i in range(1, N):
    dp[i] = A[i]
    for j in range(0, i):
        if A[i] > A[j]:
            dp[i] = max(dp[j] + A[i], dp[i])

# print(dp)
print(max(dp))
