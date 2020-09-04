# -*- coding:utf-8 -*-
# author:Karen time:2020/9/3
import numpy as np
import math

def path_matrix(a):
    # a为最短路径矩阵
    n = len(a)
    path = -1 * np.ones((n, n))  # 中间点矩阵/状态转移矩阵

    untested = []  # 待测点数组
    for i in range(n):
        for j in range(n):
            if i != j:
                untested.append((i, j))

    # 更新最短路径矩阵和状态转移矩阵
    for k in range(n):
        for m, n in untested:
            if a[m, n] > a[m, k] + a[k, n]:
                a[m, n] = a[m, k] + a[k, n]
                path[m, n] = k
    return a, path

def floyd(a):
    a, path = path_matrix(a)
    # print(a,path)
    n = len(a)
    for i in range(n):
        for j in range(n):
            if (i != j) & (not math.isinf(a[i, j])):
                trail = [i] # 路径记录
                temp = path[i, j]
                print('from ' + str(i) + ' to ' + str(j) + ', dist_min:' + str(a[i, j]) + '\npath: ')

                while temp != -1:
                    trail.append(temp)
                    temp = path[i, int(temp)]

                temp = path[int(trail[-1]), j]
                while temp != -1:
                    trail.append(temp)
                    temp = path[int(temp), j]
                trail.append(j)
                print(str(trail).replace(', ', '--').replace('.0', ''))


if __name__ == __main__:
    a = np.array([[0, 5, float('inf'), 7], [float('inf'), 0, 4, 2],
                  [3, 3, 0, 2], [float('inf'), float('inf'), 1, 0]])   # 邻接矩阵
    floyd(a)


