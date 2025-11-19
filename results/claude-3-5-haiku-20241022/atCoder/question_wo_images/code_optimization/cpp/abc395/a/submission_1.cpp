Looking at the original code, I can see it's trying to be clever with minimal code but is inefficient due to:
1. Multiple scanf calls in a loop condition
2. Complex nested ternary operators that are evaluated repeatedly
3. Unnecessary variable updates

Here's the optimized version:

```c
#include<stdio.h>
int main(){
    int n,a,b,i=1;
    scanf("%d%d",&n,&a);
    for(;i<n;i++){
        scanf("%d",&b);
        if(b<=a){puts("No");return 0;}
        a=b;
    }
    puts("Yes");
}
```

This optimization:
1. Reads N first, then uses it to control the loop (O(N) instead of repeated scanf attempts)
2. Exits immediately upon finding a violation (early termination)
3. Uses simple comparison instead of nested ternary operators
4. Eliminates redundant operations and increments