#include <stdio.h>
#include <stdlib.h>

int main()
{
    system("chcp 1251"); //кодировка русского языка
    system("cls");      //очистка консоли


    char s[256];    // массив, в который помещаем считываемая строка
   // char *str;
    printf ("Введите строку:\n");
    //str =
    gets(s);
    printf ("Введённая Вами строка:\n%s\n\n",s);

    float x;
    printf ("Теперь введите вещественное число:\n");
    scanf("%f", &x);
    printf ("Вещественное число = %.3f\n\n", x);


    system("pause");
    return 0;
}
