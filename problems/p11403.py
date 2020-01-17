N = int(input())

Arr = []
result_arr = [[0] * N for i in range(N)]

for i in range(N):
    Arr.append(list(map(int, input().split(" "))))


#
# for row in Arr:
#     print(row)


def dfs(i, j):
    # print(">> dfs start : ({}, {})".format(i, j))
    stack = [i]  # save vertex's idx
    visit = [0] * N
    visit[i] = 1

    # dfs를 하면서, j까지 도달 가능 한지 체크
    while len(stack) != 0:
        top = stack[-1]
        # print("top:{}, stack : {}".format(top, stack))
        success_flag = False
        pop_flag = True  # 현재 top에서는 인접노드가 없음

        # top의 인접 노드 확인
        for j_idx, j_val in enumerate(Arr[top]):
            if j_val == 1:
                pop_flag = False
                if j_idx == j:  # success
                    # print("success: {} -> {}".format(i, j_idx))
                    result_arr[i][j_idx] = 1
                    success_flag = True
                    break

                if j_idx == top:  # loop
                    # print("loop..")
                    stack.pop()
                    break

                if visit[j_idx] == 0:
                    # print("stack add : {}".format(j_idx))
                    stack.append(j_idx)
                    visit[j_idx] = 1
                else:
                    if len(stack) > 0:
                        pop_tmp = stack.pop()
                        # print("stack pop : {}".format(pop_tmp))

            else:
                if pop_flag and j_idx == (N - 1):
                    pop_val = stack.pop()
                    # print("pop : {}".format(pop_val))

        if success_flag:
            break

        # print("")
        # sleep(0.5)


for i in range(N):
    for j in range(N):
        dfs(i, j)

# print("")
for row in result_arr:
    for c in row:
        print(c, end=' ')
    print("")
