#include <stdio.h>
#include <string.h>

int main() {
    static char S[200005];
    if (scanf("%200004s", S) != 1) return 0;
    int n = strlen(S);
    if (n % 2) {
        printf("No");
        return 0;
    }
    static char st[200005];
    int top = 0;
    for (int i = 0; i < n; i++) {
        char c = S[i];
        if (c == '(' || c == '[' || c == '<') {
            st[top++] = c;
        } else {
            if (top == 0) {
                printf("No");
                return 0;
            }
            char d = st[top - 1];
            if ((c == ')' && d == '(') ||
                (c == ']' && d == '[') ||
                (c == '>' && d == '<')) {
                top--;
            } else {
                printf("No");
                return 0;
            }
        }
    }
    printf(top == 0 ? "Yes" : "No");
    return 0;
}