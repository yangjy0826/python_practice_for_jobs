# -*- coding: utf-8 -*-
# 递归输出下列长度为2^n的矩阵（每个矩阵由四部分组成），矩阵满足以下条件：
#
# 右下角部分全为0，其他部分等于上一阶段的矩阵
#
# N=0,            1
#
# N=1,            1 1
#                 1 0
#
# N=2,            1 1 1 1
#                 1 0 1 0
#                 1 1 0 0
#                 1 0 0 0

# 法1 调用numpy中的函数
import numpy as np
from numpy import *

def generate_matrix(N):
    if N== 0:
        matrix = [[1]]
    else:
        matrix1 = np.hstack((generate_matrix(N-1), generate_matrix(N-1)))
        zer = zeros([N, N], int8)
        matrix2 = np.hstack((generate_matrix(N-1), zer))
        matrix = np.vstack((matrix1, matrix2))
    return matrix

N = 2
print(generate_matrix(N))

# 法2 不调用numpy中的函数
def generate_matrix(N):
    if N== 0:
        matrix = [[1]]
    else:
        matrix = generate_matrix(N-1)
        matrix += generate_matrix(N-1)
        for i in range(0, N):
            matrix[i] += generate_matrix(N-1)[i]
        for j in range(N, 2*N):
            for k in range(N, 2*N):
                matrix[j].append(0)
    return matrix

N = 2
print(generate_matrix(N))
