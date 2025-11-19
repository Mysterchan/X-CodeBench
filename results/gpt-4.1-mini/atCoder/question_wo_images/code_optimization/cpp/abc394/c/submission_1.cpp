```c
#include <stdio.h>
#include <string.h>

int main() {
    char S[300001];
    if (scanf("%300000s", S) != 1) {
        return 1;
    }

    int len = strlen(S);
    int i = 0;

    while (i < len - 1) {
        if (S[i] == 'W' && S[i + 1] == 'A') {
            S[i] = 'A';
            S[i + 1] = 'C';
            if (i > 0) i--;
            else i = 0;
        } else {
            i++;
        }
    }

    printf("%s\n", S);
    return 0;
}
```