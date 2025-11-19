#include <stdio.h>
#include <string.h>

#define MAX_SIZE 200001

int main() {
    char S[MAX_SIZE];
    scanf("%200000s", S);
    
    char stack[MAX_SIZE];
    int top = -1;
    int len = strlen(S);
    
    for (int i = 0; i < len; i++) {
        char c = S[i];
        
        if (c == '(' || c == '[' || c == '<') {

            stack[++top] = c;
        } else {

            if (top == -1) {
                printf("No");
                return 0;
            }
            
            char top_char = stack[top];
            if ((c == ')' && top_char == '(') ||
                (c == ']' && top_char == '[') ||
                (c == '>' && top_char == '<')) {
                top--;
            } else {
                printf("No");
                return 0;
            }
        }
    }
    
    printf(top == -1 ? "Yes" : "No");
    return 0;
}
