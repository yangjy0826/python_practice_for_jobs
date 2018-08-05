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

