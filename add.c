#include "main.h"
void add(int a, int b)
{
	if (a == '\0' || b == '\0')
	{
		printf("You can only add integers\n");
		return;
	}
	printf("The addition of %d and %d is: %d\n", a, b, a + b);
}
