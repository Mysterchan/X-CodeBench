def binary_search(lis,val):
    N = len(lis)
    l = 0
    r = N-1
    if val < lis[0]:
        return -1
    elif val == lis[0]:
        return -1
    elif val == lis[r]:
        return N-1
    elif lis[r] < val:
        return N
    else:
        while r-l > 1:
            mid = l+(r-l)//2
            if lis[mid] == val:
                while True:
                    if lis[mid-1] == val:
                        mid -= 1
                    else:
                        return mid-1
            elif lis[mid] < val:
                l = mid
            else:
                r = mid
    return l

def main():
    N = int(input())
    lis = list(map(int,input().split()))

    ans = 0
    for i in range(len(lis)):
        val = lis[i]
        val2 = 2*val
        ind = binary_search(lis,val2)
        if ind == N:
            continue
        else:
            ans += N-1-ind
    print(ans)

if __name__ == '__main__':
    main()