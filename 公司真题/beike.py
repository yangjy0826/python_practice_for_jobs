import sys

list1 = map(int, sys.stdin.readline().strip().split(' '))

n = list1[0]
start = []
end = []
for i in range(n):
    list_n = map(int, sys.stdin.readline().strip().split(' '))
    start.append(list_n[0])
    end.append(list_n[1])
p1 = list1[1]
p2 = list1[2]
p3 = list1[3]
t1 = list1[4]
t2 = list1[5]
# print(start)
# print(end)
sum = 0
for i in range(n):
    sum += p1 * (end[i]-start[i])
# print(sum)
for i in range(n-1):
    gap = start[i+1]-end[i]
    if gap <= t1:
        add = gap*p1
        # print(add)
        sum += add
    elif t1<gap<=t1+t2:
        add = (t1 * p1 + (gap - t1) * p2)
        sum += add
        # print(add)
    else: # gap>t1+t2
        add = (t1 * p1 + t2 * p2 + (gap - t1 - t2) * p3)
        sum += add
        # print(add)
print(sum)