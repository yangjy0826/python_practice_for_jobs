import sys
import math
n = int(sys.stdin.readline().strip())  # read the 1st line
if n < 3:
    print('Error')
else:
    x = []
    y = []
    for i in range(n):
        x_new, y_new = map(int, sys.stdin.readline().strip().split(" "))
        x.append(x_new)
        y.append(y_new)
    c = []
    for i in range(len(x)):  # 去掉重复坐标
        c.append((x[i], y[i]))
    c = list(set(c))
    x = []
    y = []
    for i in range(len(c)):
        x.append(c[i][0])
        y.append(c[i][1])
    count = 0
    for i in range(len(x)):
        for j in range(len(x)):
            if j == i:
                continue
            else:
                for k in range(len(x)):
                    if k == j or k == i:
                        continue
                    else:
                        if ((x[i] - x[j]) * (y[k] - y[j]) - (x[k] - x[j]) * (y[i] - y[j])) != 0:  # 判断三角形
                            count += 1
    count = int(count/6)
    print(count)

# import copy
#
#
#
# def combine(l, n):
#     answers = []
#     one = [0] * n
#
#     def next_c(li=0, ni=0):
#         if ni == n:
#             answers.append(copy.copy(one))
#             return
#         for lj in range(li, len(l)): # python2 和python3一个用range，一个用xrange
#             one[ni] = l[lj]
#             next_c(lj + 1, ni + 1)
#     next_c()
#     return answers
#
#
# print(combine([1, 2, 3, 4, 5], 3))


# from itertools import combinations # 组合函数
# print(list(combinations([1,2,3,4,5], 3)))
