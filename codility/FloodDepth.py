# A = [1, 3, 2, 1, 2, 1, 5, 3, 3, 4, 2]
# A = [5, 8, 9]
# A = [1, 3, 2, 1, 2, 1, 5, 3, 3, 4, 2, 10, 2, 10, 20, 5, 21]
# A = [2, 1, 3]
A = [3, 1, 2]
# A = [1, 2, 3]

left_wall_idx = -1
deepest_idx = 0
deepest_val = -1

for idx in range(1, len(A)):
    print(idx)
    prev_idx = idx -1

    if left_wall_idx == -1: # init create left wall
        if A[idx] < A[prev_idx]:
            left_wall_idx = prev_idx
            deepest_idx = idx

    else:
        if A[idx] > A[prev_idx]:
            if A[left_wall_idx] <= A[idx]: # new left wall
                prev_left_wall_idx = left_wall_idx
                left_wall_idx = idx
                surface_val = min(A[prev_left_wall_idx], A[left_wall_idx])

                # calc deepest val
                deepest_val = max(deepest_val, surface_val - A[deepest_idx])
                deepest_idx = idx
            else:
                # calc deepest val
                deepest_val = max(deepest_val, A[idx] - A[deepest_idx])


        elif A[idx] < A[prev_idx]:  # flood site
            if deepest_idx == -1:
                deepest_idx = idx
            else:
                cur_deepest_val = deepest_val
                new_deepest_val = A[prev_idx] - A[idx]
                if new_deepest_val > cur_deepest_val:
                    deepest_idx = idx
                else:
                    deepest_idx = idx if A[idx] <= A[deepest_idx] else deepest_idx
    print("A[{}]:{}, deepest_idx : {}, deepest_val : {}, left_wall_idx: {}".format(idx, A[idx], deepest_idx, deepest_val, left_wall_idx))
    print("")
print(deepest_val)


