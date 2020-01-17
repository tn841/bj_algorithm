"""
- 백트래킹
- N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.
- 1 <= N <= 15
"""

N = int(input())
board = [[0] * (N+1) for i in range(N+1)]
count = 0

def is_possible(row, col):
    for idx in range(N + 1):
        if board[row][idx] == 1 or board[idx][col] == 1:
            return False

        if (row + idx) <= N and (col + idx) <= N:
            if board[row + idx][col + idx] == 1:
                return False
        if (row - idx) >= 0 and (col - idx) >= 0:
            if board[row - idx][col - idx] == 1:
                return False
        if (row + idx) <= N and (col - idx) >= 0:
            if board[row + idx][col - idx] == 1:
                return False
        if (row - idx) >= 0 and (col + idx) <= N:
            if board[row - idx][col + idx] == 1:
                return False
    return True
solutions = []
q_paths = []
def dfs(row):
    global count

    for col in range(1, N+1):
        if is_possible(row, col):
            if row == N:
                q_paths.append((row, col))
                solutions.append(q_paths)
                print("solution! : {}".format(q_paths))
                count += 1

                q_paths.clear()
                return

            print("dfs row:{}, col:{}".format(row, col))
            board[row][col] = 1
            q_paths.append((row, col))
            dfs(row+1)
            board[row][col] = 0
            if len(q_paths) > 0:
                top_row, top_col = q_paths[-1]
                q_paths.pop(-1)
            print("unpromissing.. row:{}, col:{}".format(row, col))
            print("")

dfs(1)
print(count)

print(solutions)