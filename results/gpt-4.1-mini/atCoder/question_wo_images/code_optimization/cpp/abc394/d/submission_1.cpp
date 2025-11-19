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
        char c = S[i];
        if (top > 0) {
            char last = stack[top - 1];
            if ((last == '(' && c == ')') ||
                (last == '[' && c == ']') ||
                (last == '<' && c == '>')) {
                top--;  // pop the matching opening bracket
                continue;
            }
        }
        stack[top++] = c;
    }

    printf(top == 0 ? "Yes" : "No");
    return 0;
}
```