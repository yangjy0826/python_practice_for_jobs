# 华为笔试真题
# When the two inputs are integers between [1:7000],
# first reverse each of them, then sum up


def reverse_sum(a, b):
    if a < 1 or a > 70000 or b < 1 or b > 70000:
        return -1
    else:
        str_a = str(a)
        str_b = str(b)
        na = len(str_a)
        rev_a = 0
        nb = len(str_b)
        rev_b = 0
        # for i in range(0, na):
        for i in range(na):
            print(i)
            each_a = int(str_a[i])*10**i
            rev_a += each_a
        for j in range(0, nb):
            each_b = int(str_b[j])*10**j
            rev_b += each_b
        rev_sum = rev_a + rev_b
    return rev_sum


# test
in_1 = 4321
in_2 = 5678
rev_sum12 = reverse_sum(in_1, in_2)
print(rev_sum12)
