#include <stdio.h>
#include <stdlib.h>

int main()
{
    system("chcp 1251"); //��������� �������� �����
    system("cls");      //������� �������


    char s[256];    // ������, � ������� �������� ����������� ������
   // char *str;
    printf ("������� ������:\n");
    //str =
    gets(s);
    printf ("�������� ���� ������:\n%s\n\n",s);

    float x;
    printf ("������ ������� ������������ �����:\n");
    scanf("%f", &x);
    printf ("������������ ����� = %.3f\n\n", x);


    system("pause");
    return 0;
}
