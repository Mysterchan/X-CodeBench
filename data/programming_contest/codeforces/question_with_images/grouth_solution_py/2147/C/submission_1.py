import re
for _ in range(int(input())) :
    n = int(input())
    pattern = re.compile('11(0101)*011')
    s = '1' + input() + '1'
    if re.search(pattern, s):
        print("NO")
    else:
        print("YES")
