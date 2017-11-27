#include <stdio.h>
#include <stdlib.h>

int main()
{
	system("chcp 1251");
	system("cls");

	char string[256];
	// char *str;
	printf("Введите строку:\n");
	//str =
	gets(string);
	printf("Введённая Вами строка:\n%s\n", string);

	getchar();
	return 0;
}
