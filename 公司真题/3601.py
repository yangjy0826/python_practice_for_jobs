# -*- coding:utf-8 -*-
# 题目来自360 2019校招
# 时间限制：C/C++语言 1000MS；其他语言 3000MS
# 内存限制：C/C++语言 65536KB；其他语言 589824KB
# 题目描述：
# 有一个城市需要修建，给你N个民居的坐标X,Y，问把这么多民居全都包进城市的话，城市所需最小面积是多少（注意，城市为平行于坐标轴的正方形）
#
# 输入
# 第一行为N，表示民居数目（2≤N≤1000）
#
# 下面为N行，每行两个数字Xi，Yi，表示该居民的坐标（-1e9≤xi,yi≤1e9）
#
# 输出
# 城市所需最小面积
#
#
# 样例输入
# 2
# 0 0
# 2 2
# 样例输出
# 4
#
# Hint
# 补充样例
# 输入样例2
# 2
# 0 0
# 0 3
# 输出样例2
# 9
import sys

n = int(sys.stdin.readline().strip())
x = []
y = []
for i in range(n):
    p = map(int, sys.stdin.readline().strip().split(' '))
    x.append(p[0])
    y.append(p[1])
# print(x)
# print(y)
# print(max(x)-min(x))
# print(max(y)-min(y))
# print(max(max(x)-min(x), max(y)-min(y)))
print(pow((max(max(x)-min(x), max(y)-min(y))),2))
