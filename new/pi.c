#include <stdio.h>
int main()
{
	int a, b, c, d, e, f, g, i;
	a = 22;
	b = 7;

	for (i = 0; i <= 1000; i++)
	{
		d = a / b;
		a = (a - (d * b)) * 10;
		if (i == 0)
			printf("%d. ", d);
		else
			printf("%d ", d);
	}

	printf("\npie infinite loop to 1000 decimal places\n");
	return (0);
}
