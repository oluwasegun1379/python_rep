#include <stdio.h>
#include <string.h>
int main()
{
    printf("\n***************String Length*****************\n");
    printf("This program generates the length of a string\n");
    char str[100];
    printf("Enter a string: ");
    scanf("%[^\n]", str);

    // int len = strlen(str);
    int len;
    for (len = 0; str[len] != '\0'; ++len);

    printf("The length of the string is: %d\n", len);

    return 0;
}