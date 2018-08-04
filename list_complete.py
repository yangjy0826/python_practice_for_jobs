# 题目来自于2018拼多多笔试：
# 在商城的某个位置有一个商品列表，该列表是由L1、L2两个子列表拼接而成。当用户浏览并翻页时，需要从列表L1、L2中获取商品进行展示。展示规则如下：

# 1. 用户可以进行多次翻页，用offset表示用户在之前页面已经浏览的商品数量，比如offset为4，表示用户已经看了4个商品

# 2. n表示当前页面需要展示的商品数量

# 3. 展示商品时首先使用列表L1，如果列表L1长度不够，再从列表L2中选取商品

# 4. 从列表L2中补全商品时，也可能存在数量不足的情况

# 请根据上述规则，计算列表L1和L2中哪些商品在当前页面被展示了


# 输入描述:
# 每个测试输入包含1个测试用例，包含四个整数，分别表示偏移量offset、元素数量n，列表L1的长度l1，列表L2的长度l2。


# 输出描述:
# 在一行内输出四个整数分别表示L1和L2的区间start1，end1，start2，end2，每个数字之间有一个空格。
# 注意，区间段使用半开半闭区间表示，即包含起点，不包含终点。如果某个列表的区间为空，使用[0, 0)表示，如果某个列表被跳过，使用[len, len)表示，len表示列表的长度。

# 输入例子1:
# 2 4 4 4
# 1 2 4 4
# 4 1 3 3

# 输出例子1:
# 2 4 0 2
# 1 3 0 0
# 3 3 1 2
                                                                 
import sys
offset, n, l1, l2 = map(int, sys.stdin.readline().strip().split(" "))

if l1+l2-offset <= n: # length not enough
    if offset >= l1+l2:
        # s = [l1, l1, l2, l2]
        s = str(l1) + ' ' + str(l1) + ' ' + str(l2) + ' ' + str(l2)
    elif offset <= l1:
        s = str(offset) + ' ' + str(l1) + ' ' + str(0) + ' ' + str(l2)
    else:
        s = str(l1) + ' ' + str(l1) + ' ' + str(offset) + ' ' + str(l2)
else:
    if offset+n <= l1:  # all new items stored in list 1
        start1 = offset
        end1 = offset+n
        start2 = 0
        end2 = 0
    elif offset >= l1:  # all new items stored in list 2
        start1 = l1
        end1 = l1
        start2 = offset-l1
        end2 = offset-l1+n
    else:  # new items stored in both list 1 and list2
        start1 = offset
        end1 = l1
        start2 = 0
        end2 = n-l1+offset
    s = str(start1)+' '+str(end1)+' '+str(start2)+' '+str(end2)
print(s)
