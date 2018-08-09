import sys
import math
n = []
while 1:
    n.append(int(sys.stdin.readline().strip()))
    if n[len(n)-1] == 0:
        break

for j in range(len(n)):
    if n[j] == 0:
        break
    else:
        add = 0
        count = 0
        while n[j] > 0:
            add = math.floor(n[j] / 3)
            n[j] = n[j] - add * 3 + add
            count += add
            if n[j] < 3:
                if n[j] == 2:
                    count += 1
                else:
                    pass
                break
        print(str(count))


# while 1:
#     try:
#         n=input()
#         if n==0:
#             break
#         cnt=0
#         def func(n,cnt):
#             if n==2:
#                 return cnt+1
#             if n==1:
#                 return cnt
#             cnt+=n/3
#             n=n/3+n%3
#             cnt=func(n,cnt)
#             return cnt
#         print (func(n,cnt))
#     except:
#         break