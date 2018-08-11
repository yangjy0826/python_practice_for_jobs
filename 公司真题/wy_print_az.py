import itertools
# n, m, k = map(int, raw_input().strip().split(' '))
n = 3
m = 2
k = 6
x = 1
for i in range(m):
    x = x * (i+1)
# print(x)
y = 1
for j in range(n):
    y = y * (j+1)
# print(y)
z = 1
for w in range(n+m):
    z = z * (w+1)
# print(z)
# print(int(z/x/y))
# print(k)
if k > int(z/x/y):
    print('-1')
else:
    l = []
    i = 0
    j = 0
    for i in range(n):
        l.append(1)
    for j in range(m):
        l.append(2)
    # print(list)
l12 = set(list(itertools.permutations(l, m+n)))
l12 = list(l12)
# print(l12)
# print(l12[0])
i = 0
j = 0
lnum = []
for i in range(len(l12)):
    num = 0
    for j in range(m+n):
        num+=l12[i][j]*pow(10, m+n-1-j)
        # num = int(num)
    lnum.append(num)
lnum = sorted(lnum)
# print(lnum)
target = str(lnum[k-1])
# print(target)
i = 0
str = ''
for i in range(len(target)):
    if target[i] == '1':
        str += 'a'
    if target[i] == '2':
        str += 'z'
print(str)
