#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main()
{
system("chcp 1251"); //������� � ������� �� �������
system("cls");       //������ �������

printf("\t\t\t ������� 1 � 2 \n\n\n");
int iNum16;
printf("������� ����� � 16�� ��\n");
scanf("%x", &iNum16);
system("cls");
printf("\t\t\t ������� 1 � 2 \n\n\n");
printf("�������� ����� � 16�� �� = %x \n\n", iNum16);
printf("�������� ����� � 8�� �� = %o \n\n", iNum16);


system("pause");
system("cls");


printf("\t\t\t ������� 3 \n\n\n");
printf("�������� ����� � 16�� �� = %x \n\n", iNum16);
int iSdvinBit = iNum16 << 4;
printf("��������� �� 4 ���� ����� ����� � 16�� �� = %x \n\n", iSdvinBit);


system("pause");
system("cls");


printf("\t\t\t ������� 4 \n\n\n");
printf("�������� ����� � 16�� �� = %x \n\n", iNum16);
int iNegBit = ~iNum16;
printf("�� �� ����� ����� ������� �������� ��������� = %x \n\n", iNegBit);


system("pause");
system("cls");


printf("\t\t\t ������� 5 \n\n\n");
int iNum16_2;
printf("������� ����� � 16�� ��\n");
scanf("%x", &iNum16_2);
printf("�������� ����� = %x \n", iNum16_2);
printf("����� �������� � 1�� ������� = %x \n\n", iNum16);
int iIBit16 = iNum16_2 & iNum16;
printf("��������� � ��������� ���� ����� = %x \n\n",  iIBit16);



system("pause");
}
