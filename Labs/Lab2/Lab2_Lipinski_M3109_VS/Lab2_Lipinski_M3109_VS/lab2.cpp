#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#pragma warning(disable : 4996)

#define PI 3.14159265

int main()
{
	system("chcp 1251");
	system("cls");

	double z1, z2;
	int a;

	printf("Введите в градусах аргумент а \n ");
	scanf("%d", &a);
	printf("Aгумент а = %d градусов \n\n ", a);

	sin(a * PI / 180);
	//printf("sin = %f\n", sin(a * PI / 180));
	tan(a * PI / 180);
	//printf("tan = %f\n\n", tan(a * PI / 180));

	z1 = (1 - 2 * pow(sin(a), 2)) / (1 + sin(2 * a));
	z2 = (1 - tan(a)) / (1 + tan(a));

	printf("Полученные значения функций:\n");
	printf("z1 = %.3f \n", z1);
	printf("z2 = %.3f \n", z2);



	getchar(); getchar();
	return 0;
}