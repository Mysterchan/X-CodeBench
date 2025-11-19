#include <stdio.h>

int main() {
    char S[200001];
    
    if (scanf("%200000s", S) != 1)
        return 1;
    
    int stack[200001], top = -1;
    
    for (int i = 0; S[i] != '\0'; i++) {
        char c = S[i];
        // Push to stack if it's an opening bracket
        if (c == '(' || c == '[' || c == '<') {
            stack[++top] = c;
        } 
        // Check for matching closing brackets
        else {
            if (top == -1) {
                printf("No");
                return 0;
            }
            char last = stack[top--];
            if ((c == ')' && last != '(') ||
                (c == ']' && last != '[') ||
                (c == '>' && last != '<')) {
                printf("No");
                return 0;
            }
        }
    }
    
    printf(top == -1 ? "Yes" : "No");
    return 0;
}
