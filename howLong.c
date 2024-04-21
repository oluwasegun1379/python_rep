#include <stdio.h>
#include <time.h>
int main()
{
    clock_t start, end;
    double cpu_time_used ;

    start = clock();

    for (int i = 0; i < 1000000000; i++)   

    end = clock();
    cpu_time_used = end - start;
    double seconds = cpu_time_used / 1000;
    printf("CPU time used: %.2f\n", seconds);

    return 0;
}