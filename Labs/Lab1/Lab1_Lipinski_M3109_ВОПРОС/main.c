#include <stdio.h>
#include <stdlib.h>

int main()
{
	system("chcp 1251");
	system("cls");

	char string[256];
	// char *str;
	printf("������� ������:\n");
	//str =
	gets(string);
	printf("�������� ���� ������:\n%s\n", string);

	getchar();
	return 0;
}
