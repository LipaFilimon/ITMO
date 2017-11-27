#include <stdio.h>

int main()
{
    printf("\t\t\tTask 1\n\n");

	printf("Enter the number\n");
	int iNum;
    scanf("%d", &iNum);
    printf("%d\n",21<=iNum && iNum<=56);



    getchar();getchar();
    system("cls");
    printf("\t\t\tTask 2\n\n");



    short int shiNum;
    const short int sConst = 2048; //= 1000 0000 0000

    printf("Enter the number\n");
    scanf("%hd",&shiNum);

    short int BitMultiplication = shiNum & sConst;
    //printf("%hd\n",BitMultiplication);

    if (BitMultiplication==2048)
    {
        printf("12 bit = 1 \n");
    }
    else
    {
        printf("12 bit = 0 \n");
    }



    system("pause");
	return 0;
}
