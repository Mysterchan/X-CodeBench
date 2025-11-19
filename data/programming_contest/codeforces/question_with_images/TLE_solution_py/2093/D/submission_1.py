no_of_in=int(input())
for m in range(no_of_in):
    n=int(input())

    matrix=[[0]*(2**n) for _ in range(2**n)]
    count=1
    def grid(n,i=0,j=0):
        global matrix
        global count
        if n==1:
            x,y=i,j
            matrix[i][j]= count

            count+=1
            i+=1
            j+=1
            matrix[i][j]= count

            count+=1
            j-=1
            matrix[i][j]= count

            count+=1
            j+=1
            i-=1
            matrix[i][j]= count
            count+=1
            i,j=x,y

        else:
            return grid(n-1,i,j),grid(n-1,i+2**(n-1),j+2**(n-1)), grid(n-1,i+2**(n-1),j), grid(n-1,i,j+2**(n-1))

    grid(n)

    q=int(input())

    for i in range(q):
        x=input().split()
        if x[0]=='->':
            print(matrix[int(x[1])-1][int(x[2])-1])
        else:
            for i in matrix:
                if int(x[1]) in i:

                    print (matrix.index(i)+1, i.index(int(x[1]))+1)
