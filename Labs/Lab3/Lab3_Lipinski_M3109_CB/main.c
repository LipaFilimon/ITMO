#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main()
{
system("chcp 1251"); //переход в консоли на русский
system("cls");       //чистка консоли

printf("\t\t\t Задание 1 и 2 \n\n\n");
int iNum16;
printf("Введите число в 16ой СС\n");
scanf("%x", &iNum16);
system("cls");
printf("\t\t\t Задание 1 и 2 \n\n\n");
printf("Введённое число в 16ой СС = %x \n\n", iNum16);
printf("Введённое число в 8ой СС = %o \n\n", iNum16);


system("pause");
system("cls");


printf("\t\t\t Задание 3 \n\n\n");
printf("Введённое число в 16ой СС = %x \n\n", iNum16);
int iSdvinBit = iNum16 << 4;
printf("Сдвинутое на 4 бита влево число в 16ой СС = %x \n\n", iSdvinBit);


system("pause");
system("cls");


printf("\t\t\t Задание 4 \n\n\n");
printf("Введённое число в 16ой СС = %x \n\n", iNum16);
int iNegBit = ~iNum16;
printf("То же число после битовой операции отрицания = %x \n\n", iNegBit);


system("pause");
system("cls");


printf("\t\t\t Задание 5 \n\n\n");
int iNum16_2;
printf("Введите число в 16ой СС\n");
scanf("%x", &iNum16_2);
printf("Введённое число = %x \n", iNum16_2);
printf("Число введённое в 1ом задании = %x \n\n", iNum16);
int iIBit16 = iNum16_2 & iNum16;
printf("Результат И указанных выше числе = %x \n\n",  iIBit16);



system("pause");
}
