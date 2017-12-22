#include <stdio.h>
#include <math.h>

//Наибольший общий делитель
int NOD(int a, int b)
{
    int c;
    while (a) 
    {
        c = a;
        a = b % a;
        b = c;
    }
    return b;
}

//Наименьшее общее кратное
int NOK(int a, int b) 
{
    return a * (b / NOD(a, b));
}

//Cумма цифр натурального числа
int SumOfDigits(int number) 
{
    if (number < 10) 
    {
        return number;
    }
    else 
    {
        return number % 10 + SumOfDigits(number / 10);
    }
}


int main()
{
    printf("\t\t\t Task 1.\n\tHighest common factor and heast common multiple.\n\n");

    
    int Number_1, Number_2;

    printf("Enter first number: ");
    scanf("%d", &Number_1);

    printf("Enter second number: ");
    scanf("%d", &Number_2);

    printf("\nHighest common factor: %d", NOD(Number_1, Number_2));
    printf("\nHeast common multiple: %d\n\n", NOK(Number_1, Number_2));



    getchar();getchar();
    system("cls");
    printf("\t\t Task 4. Sum of digits of a natural number.\n\n");



    int Number_3;
    printf("Enter number: ");
    scanf("%d", &Number_3);

    printf("\nSum of digits: %d\n", SumOfDigits(Number_3));


    getchar();
    return 0;
}