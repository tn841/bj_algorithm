from time import sleep

N = int(input())

group_list = []

visit_A = [[0] * N for i in range(N)]
Arr = []
for i in range(N):
    row_str = input()
    temp=[]
    for c in row_str:
        temp.append(int(c))
    Arr.append(temp)

# for row in Arr:
#     print(row)

def dfs(row, col):
    # print("start dfs at Arr[{}][{}]".format(row, col))
    dfs_stack = []
    dfs_stack.append((row, col))
    visit_A[row][col] = 1
    count = 0
    while len(dfs_stack) != 0:
        c_row, c_col = dfs_stack[-1]
        # print("c_row:{}, c_col:{}".format(c_row, c_col))
        # print("dfs_stack : {}".format(dfs_stack))
        # print("<<visit_A>>")
        # for row in visit_A:
        #     print(row)
        """
        1. left
        2. down
        3. right
        4. up
        """
        if c_col > 0 and Arr[c_row][c_col-1] == 1 and visit_A[c_row][c_col-1] == 0: # left
            # print("left")
            dfs_stack.append((c_row, c_col-1))
            # visit_A[c_row][c_col] = 1
        elif c_row < N - 1 and Arr[c_row + 1][c_col] == 1 and visit_A[c_row +1][c_col] == 0: # down
            # print("down")
            dfs_stack.append((c_row+1, c_col))
            # visit_A[c_row + 1][c_col] = 1
        elif c_col < N - 1 and Arr[c_row][c_col + 1] == 1 and visit_A[c_row][c_col + 1] == 0: #right
            # print("right")
            dfs_stack.append((c_row, c_col+1))
            # visit_A[c_row][c_col + 1] = 1
        elif c_row > 0 and Arr[c_row-1][c_col] == 1 and visit_A[c_row - 1][c_col] == 0:  # up
            # print("up")
            dfs_stack.append((c_row - 1, c_col))
            # visit_A[c_row - 1][c_col] = 1
        else:
            # print("pop")
            dfs_stack.pop()
            # visit_A[c_row][c_col] = 1
            count += 1
        visit_A[c_row][c_col] = 1
        # print("")
        # sleep(1)
    return count




for row in range(N):
    for col in range(N):
        # print("row:{}, col:{} => val:{}".format(row, col, Arr[row][col]))
        if Arr[row][col] == 1 and visit_A[row][col] == 0:
            group_list.append(dfs(row, col))
        elif Arr[row][col] == 0 and visit_A[row][col] == 0:
            visit_A[row][col] = 1


# print("="*50)
# print(group_list)
print(len(group_list))
group_list.sort()
for val in group_list:
    print(val)
# if len(group_list) < 1:
#     print(0)