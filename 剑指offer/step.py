# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

import math
def jumpFloor(number):
    # write code here
    n = number
    if n % 2 != 0:
        count = 1
        for i in range(1, int(math.floor(n / 2))+1):
            n2 = i
            n1 = n - i * 2
            # a = n1!
            a = 1
            for j in range(1, n1 + 1):
                a = a * j
            # b = n2!
            b = 1
            for k in range(1, n2 + 1):
                b = b * k
            # c = (n1+n2)!
            c = 1
            for w in range(1, n1 + n2 + 1):
                c = c * w
            count += int(c/(a*b))
        return count
    else:
        count = 2
        for i in range(1, int(n/2)):
            n2 = i
            n1 = n - i * 2
            # a = n1!
            a = 1
            for j in range(1, n1 + 1):
                a = a * j
            # b = n2!
            b = 1
            for k in range(1, n2 + 1):
                b = b * k
            # c = (n1+n2)!
            c = 1
            for w in range(1, n1 + n2 + 1):
                c = c * w
            count += int(c / (a * b))
        return count
number = 7
count = jumpFloor(number)
print(count)
