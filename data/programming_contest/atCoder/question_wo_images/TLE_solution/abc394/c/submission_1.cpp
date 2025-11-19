#include <stdio.h>
#include <string.h>

int main() {
    char S[300001];
    
    if (scanf("%300000s", S) != 1) {
        return 1;
    }

    int len = strlen(S);
    int found;
    
    do {
        found = 0;
        for (int i = 0; i < len - 1; i++) {
            if (S[i] == 'W' && S[i+1] == 'A') {
                S[i] = 'A';
                S[i+1] = 'C';
                found = 1;
                break;
            }
        }
    } while (found);

    printf("%s\n", S);
    return 0;
}
