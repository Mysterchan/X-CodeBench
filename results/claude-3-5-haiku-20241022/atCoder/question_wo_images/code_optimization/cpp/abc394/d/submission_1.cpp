```c
#include <stdio.h>
#include <string.h>

int main() {
    char S[200001];
    
    if (scanf("%200000s", S) != 1)
        return 1;
    
    int len = strlen(S);
    
    if (len % 2 == 1) {
        printf("No");
        return 0;
    }
    
    char stack[200001];
    int top = 0;
    
    for (int i = 0; i < len; i++) {
        if (top > 0) {
            char prev = stack[top - 1];
            char curr = S[i];
            
            if ((prev == '(' && curr == ')') ||
                (prev == '[' && curr == ']') ||
                (prev == '<' && curr == '>')) {
                top--;
                continue;
            }
        }
        stack[top++] = S[i];
    }
    
    printf(top == 0 ? "Yes" : "No");
    return 0;
}
```