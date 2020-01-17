N = int(input())

board = [ [0] * (N+1) for i in range(N+1) ]
for row in board:
    print(row)
solution = [0] * (N+1)
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

def is_possible2(row):

    for col in range(1, N+1):
        if solution[col] == solution[row] :  # 같은 열
            return False
        if abs(solution[col] - solution[row]) == abs(col-row):
            return False
    return True

def dfs(row):
    global count
    for j in range(1, N+1):
        if row == N:
            count += 1
            return

        if is_possible2(row+1):
            print("dfs : i:{}, j:{}".format(row+1, j))
            solution[row] = j
            dfs(row+1)


dfs(0)
print(count)