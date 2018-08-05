# 题目来自2018拼多多校招：
# 给出平面上的n个点，现在需要你求出，在这n个点里选3个点能构成一个三角形的方案有几种。


# 输入描述:

# 第一行包含一个正整数n，表示平面上有n个点（n <= 100)
# 第2行到第n + 1行，每行有两个整数，表示这个点的x坐标和y坐标。(所有坐标的绝对值小于等于100，且保证所有坐标不同）

 
# 输出描述:

# 输出一个数，表示能构成三角形的方案数。

 
# 输入例子1:

# 4
# 0 0
# 0 1
# 1 0
# 1 1

 
# 输出例子1:

# 4

 
# 例子说明1:

# 4个点中任意选择3个都能构成三角形


###############################################################解法1
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


###############################################################解法2
import sys
import math
import copy


def combine(l, n):
    answers = []
    one = [0] * n

    def next_c(li=0, ni=0):
        if ni == n:
            answers.append(copy.copy(one))
            return
        for lj in range(li, len(l)): # python2和python3一个用range，一个用xrange
            one[ni] = l[lj]
            next_c(lj + 1, ni + 1)
    next_c()
    return answers


n = int(sys.stdin.readline().strip())  # read the 1st line
index = []
if n < 3:
    print('Error')
for i in range(n):
    index.append(i)
else:
    x = []
    y = []
    for i in range(n):
        x_new, y_new = map(int, sys.stdin.readline().strip().split(" "))
        x.append(x_new)
        y.append(y_new)
    index = combine(index, 3)
    count = 0
    for i in range(len(index)):
        p0 = index[i][0]
        p1 = index[i][1]
        p2 = index[i][2]
        # a = math.sqrt(pow(x[p0] - x[p1], 2) + pow(y[p0] - y[p1], 2))  # 错误的判断三角形
        # b = math.sqrt(pow(x[p0] - x[p2], 2) + pow(y[p0] - y[p2], 2))
        # c = math.sqrt(pow(x[p1] - x[p2], 2) + pow(y[p1] - y[p2], 2))
        # if a+b>c and abs(a-b)<c and a+c>b and abs(a-c)<b and b+c>a and abs(b-c)<a :
        #     count += 1
        if ((x[p0] - x[p1])*(y[p2] - y[p1])-(x[p2] - x[p1])*(y[p0] - y[p1])) != 0:  # 判断三角形
            count += 1
print(count)

