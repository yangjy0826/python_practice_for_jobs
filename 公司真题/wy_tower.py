def main():
    n, k = map(int, raw_input().strip().split(' '))
    list = map(int, raw_input().strip().split(' '))
    # print(list)
    m = 0
    x = []
    y = []
    while True:
        if m == k or max(list)-min(list)<=1:
            break
        else:
            p_max = list.index(max(list))
            p_min = list.index(min(list))
            x.append(p_max)
            y.append(p_min)
            list[p_max] -= 1
            list[p_min] += 1
            m+=1
            s = max(list)-min(list)
            # print(list)
    print(str(max(list)-min(list)) +' '+ str(m))
    for i in range(len(x)):
        print(str(x[i]+1)+' '+str(y[i]+1))
while True:
    try:
        main()
    except:
        break