#include <stdio.h>
#include <stdlib.h>

int main()
{
	system("chcp 1251"); //��������� �������� �����
	system("cls");      //������� �������


	int a;
	printf("������� ����� �����:\n");
	scanf("%d", &a);
	printf("����� ����� = %d\n\n", a);

	getchar();

	char b;
	printf("������� ������:\n");
	scanf("%c", &b);
	printf("�������� ���� ������ : %c\n\n", b);



	return 0;
}




