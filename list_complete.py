import sys
offset, n, l1, l2 = map(int, sys.stdin.readline().strip().split(" "))
# offset = 40000
# n = 40000
# l1 = 40000
# l2 = 0

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
    # s = [start1, end1, start2, end2]
    s = str(start1)+' '+str(end1)+' '+str(start2)+' '+str(end2)
print(s)