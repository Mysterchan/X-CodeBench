#include<stdio.h>


int main()
{
    int t;
    scanf("%d",&t);
    while(t>0)
    {
        int n,s;
        scanf("%d %d",&n,&s);
        int arr[n][4];
        int c = 0;
        for(int i=0;i<n;i++)
        {
            scanf("%d %d %d %d",&arr[i][0],&arr[i][1],&arr[i][2],&arr[i][3]);
            if(arr[i][2]+arr[i][3]==s)
            {
                c++;
            }
        }

        printf("%d\n",c);

        t--;
    }

}