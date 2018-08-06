import sys

# str = sys.stdin.readline().strip()
str = 'abcdefghijklmnop'
n = len(str)

if n%4 !=0:
    print('Error')
else:
    l_line = int(n/4)
    # print(str[:n/4])
    middle = ''
    for i in range (l_line-1):
        line = str[n-(i+1)]
        for j in range(l_line - 1):
            line += ' '
        line += str[l_line + (i + 1)]
        middle += line
        middle += '\n'
    last = ''
    for i in range(l_line+1):
        last += str[n-i-l_line]
    print(str[0:l_line+1]+'\n'+middle + last)
    # print(str[5])