# 本题为拼多多2018/8/5笔试题目

# 第三题
# 找出指定的那个人和谁关系最好，具体表现为共同好友最多。

# 输入的第一行的两个数分别是总共多少人，指定的那个人的位置。

# 从第二行开始依次为每个人的好友（用数字表示）。

# 因此输入：

# 5 0
# 1 2 3
# 3 4
# 3 4
# 3 4
# 1 2 3

# 会得到：
# 4

import sys
[n, deter] = map(int, sys.stdin.readline().strip().split(' '))
friend = []
length = []
for i in range(n):
    # print(sys.stdin.readline().strip().split(' '))
    friend.append(sys.stdin.readline().strip().split(' '))
for i in range(n):
    if i == deter:
        length.append(-1)
    else:
        incommon = set(friend[i]) & set(friend[deter])
        length.append(len(incommon))
        # print(length)
big = 0
for i in range(n):
    if length[i] > length[big]:
        big = i
print(big)
