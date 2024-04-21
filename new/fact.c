#include <stdio.h>

void factorize(long long n) {
    if (n <= 1) {
        printf("%lld=%lld*%d\n", n, n, 1);
        return;
    }

    for (long long i = 2; i <= n / i; ++i) {
        while (n % i == 0) {
            printf("%lld=%lld*%lld\n", n, i, n / i);
            n /= i;
        }
    }

    if (n > 1) {
        printf("%lld=%lld*%d\n", n, n, 1);
    }
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <filename>\n", argv[0]);
        return 1;
    }

    FILE *file = fopen(argv[1], "r");
    if (file == NULL) {
        fprintf(stderr, "Error: Can't open file %s\n", argv[1]);
        return 1;
    }

    long long number;
    while (fscanf(file, "%lld", &number) != EOF) {
        factorize(number);
    }

    fclose(file);
    return 0;
}
