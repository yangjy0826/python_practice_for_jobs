# 输入一个整数，输出整数的位数，倒序输出它的每一位数字（数字
# 之间空格分开）和倒序的连续数值，而且题目限定了输入的整数不超过五位数。


def reverse(a):
    if a < -99999 or a > 99999:
        err = 'pls give a smaller number'
        return err
    elif a == 0:
        return str(a)
    elif a > 0:
        str_a = str(a)
        n = len(str_a)
        rev_a = 0
        for i in range(n):
            each_a = int(str_a[i])*10**i
            rev_a += each_a
        rev_a = str(rev_a)
        between_str = " "
        rev_a = between_str.join(rev_a)
        return rev_a
    else:
        a = -a
        str_a = str(a)
        n = len(str_a)
        rev_a = 0
        for i in range(n):
            each_a = int(str_a[i]) * 10 ** i
            rev_a += each_a
        rev_a = str(rev_a)
        between_str = " "
        rev_a = between_str.join(rev_a)
        rev_a = '-'+rev_a
        return rev_a


# test
m = -12345
print(reverse(m))