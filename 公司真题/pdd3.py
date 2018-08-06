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
