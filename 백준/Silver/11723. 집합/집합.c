#include <stdio.h>
#include <string.h>

int main() {
    int m;
    scanf("%d", &m);

    int set[21] = {0}; 
    char cmd[10];
    int x;

    while (m--) {
        scanf("%s", cmd);

        if (strcmp(cmd, "add") == 0) {
            scanf("%d", &x);
            set[x] = 1;
        }
        else if (strcmp(cmd, "remove") == 0) {
            scanf("%d", &x);
            set[x] = 0;
        }
        else if (strcmp(cmd, "check") == 0) {
            scanf("%d", &x);
            printf("%d\n", set[x]);
        }
        else if (strcmp(cmd, "toggle") == 0) {
            scanf("%d", &x);
            set[x] = !set[x];
        }
        else if (strcmp(cmd, "all") == 0) {
            for (int i = 1; i <= 20; i++) set[i] = 1;
        }
        else if (strcmp(cmd, "empty") == 0) {
            for (int i = 1; i <= 20; i++) set[i] = 0;
        }
    }

    return 0;
}