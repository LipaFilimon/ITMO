#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#define PI 3.14159265

int main()
{
	system("chcp 1251");
	system("cls");

	float z1, z2;
	int a;

	printf("������� � �������� �������� � \n ");
	scanf("%d", &a);
	printf("A������ � = %d �������� \n\n ", a);

	sin(a * PI / 180);

	tan(a * PI / 180);

	z1 = (1 - 2 * pow(sin(a), 2)) / (1 + sin(2 * a));
	z2 = (1 - tan(a)) / (1 + tan(a));

	printf("���������� �������� �������:\n");
	printf("z1 = %.3f \n", z1);
	printf("z2 = %.3f \n", z2);



	getchar();//getchar();
	return 0;
}
