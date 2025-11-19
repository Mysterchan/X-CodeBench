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
    
    int m;
    do {
        m = 0;
        for (int i = 0; i < len - 1; i++) {
            if ((S[i] == '(' && S[i + 1] == ')') ||
                (S[i] == '[' && S[i + 1] == ']') ||
                (S[i] == '<' && S[i + 1] == '>')) {
                
                memmove(&S[i], &S[i + 2], len - i - 1);
                len -= 2;
                m++;
                i--;
                break;
            }
        }
    } while (m != 0);
    
    printf(len == 0 ? "Yes" : "No");
    return 0;
}
