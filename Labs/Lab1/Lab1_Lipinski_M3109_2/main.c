#include <stdio.h>
#include <stdlib.h>

int main()
{
	system("chcp 1251"); //кодировка русского €зыка
	system("cls");      //очистка консоли


	int a;
	printf("¬ведите целое число:\n");
	scanf("%d", &a);
	printf("÷елое число = %d\n\n", a);

	getchar();

	char b;
	printf("¬ведите символ:\n");
	scanf("%c", &b);
	printf("¬ведЄнный ¬ами символ : %c\n\n", b);



	return 0;
}




