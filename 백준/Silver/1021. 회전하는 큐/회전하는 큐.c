#include <stdio.h>

#define MAX 10000

int deque[MAX];
int front = 0;
int rear = 0;

void push_back(int x) {
    deque[rear++] = x;
}

void pop_front() {
    for (int i = 0; i < rear - 1; i++) {
        deque[i] = deque[i + 1];
    }
    rear--;
}

void rotate_left() {
    int temp = deque[0];
    for (int i = 0; i < rear - 1; i++) {
        deque[i] = deque[i + 1];
    }
    deque[rear - 1] = temp;
}

void rotate_right() {
    int temp = deque[rear - 1];
    for (int i = rear - 1; i > 0; i--) {
        deque[i] = deque[i - 1];
    }
    deque[0] = temp;
}

int main() {
    int n, m;
    scanf("%d %d", &n, &m);

    for (int i = 1; i <= n; i++) {
        push_back(i);
    }

    int total = 0;

    for (int i = 0; i < m; i++) {
        int target;
        scanf("%d", &target);

        int idx;
        for (idx = 0; idx < rear; idx++) {
            if (deque[idx] == target) break;
        }

        if (idx <= rear / 2) {
            while (deque[0] != target) {
                rotate_left();
                total++;
            }
        } else {
            while (deque[0] != target) {
                rotate_right();
                total++;
            }
        }

        pop_front();
    }

    printf("%d\n", total);
    return 0;
}