#include <stdio.h>
#include <string.h>

int main() {
    char S[300001];
    
    if (scanf("%300000s", S) != 1) {
        return 1;
    }

    int len = strlen(S);
    int writeIndex = 0;

    for (int i = 0; i < len; i++) {
        if (i < len - 1 && S[i] == 'W' && S[i + 1] == 'A') {
            S[writeIndex++] = 'A';
            S[writeIndex++] = 'C';
            i++;  // Skip the next character since we've replaced "WA" with "AC"
        } else {
            S[writeIndex++] = S[i];
        }
    }
    
    S[writeIndex] = '\0'; // Null-terminate the new string
    printf("%s\n", S);
    return 0;
}