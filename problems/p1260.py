import copy
from time import sleep

N, M, V = map(int, input().split())
# print("{}, {}, {}".format(N, M, V))

vertex_list = [[0] * (N+1) for i in range((N+1))]
visit_list = [0] * (N+1)
visit_list[V] = 1
# print(vertex_list)
# print(visit_list)
for i in range(int(M)):
    a, b = map(int, input().split())
    vertex_list[a][b] = 1
    vertex_list[b][a] = 1

dfs_result = []
bfs_result = []


# for row in vertex_list:
#     print(row)

# print("")
# for row in visit_list:
#     print(row)
# print("")

def DFS(v):
    dfs_stack = []
    # print(vertex_list[v])
    dfs_stack.append(v)
    dfs_result.append(v)
    # print("Start dfs_stack : {}".format(dfs_stack))
    while len(dfs_stack) != 0:
        # cur_v = dfs_stack.pop()
        cur_v = dfs_stack[-1]
        visit_list[cur_v] = 1
        # print("cur_v : {}".format(cur_v))
        # print("visit_list : {}".format(visit_list))

        temp_list = []
        for idx, val in enumerate(vertex_list[cur_v]):
            # print("idx : {}".format(idx))
            # if val == 1 and visit_list[idx] == 0:
            #     # dfs_stack.insert(0, idx)
            #     # dfs_stack.append(idx)
            #     temp_list.insert(0, idx)
            #     visit_list[idx] = 1
            if val == 1 and visit_list[idx] == 0:
                dfs_stack.append((idx))
                dfs_result.append(idx)
                # visit_list[idx] = 1
                break
            if idx == len(vertex_list) -1:
                dfs_stack.pop()


        dfs_stack.extend(temp_list)

        # sleep(0.5)
        # print("dfs_stack : {}".format(dfs_stack))
        # print("")

    for k in dfs_result:
        print(k, end=' ')


def BFS(v):
    bfs_queue = []
    bfs_queue.append(v)
    # print("Start bfs_queue : {}".format(bfs_queue))
    while len(bfs_queue) != 0:
        cur_v = bfs_queue.pop(0)
        bfs_result.append(cur_v)
        visit_list[cur_v] = 1
        # print("cur_v : {}".format(cur_v))
        # print("visit_list : {}".format(visit_list))
        for idx, val in enumerate(vertex_list[cur_v]):
            if val == 1 and visit_list[idx] == 0:
                bfs_queue.append(idx)
                visit_list[idx] = 1
        #
        # sleep(1)
        # print("bfs_queue : {}".format(bfs_queue))
        # print("")
    for k in bfs_result:
        print(k, end=' ')

DFS(V)
#
# print("=" * 50)
print("")
visit_list = [0] * (N+1)
visit_list[V] = 1
BFS(V)