#include <stdio.h>

int main ()
{
    printf("\t\t\t Task 1 \n");

    int masA[7] = {23, 5678, 2, 564, 365, 77, 443};

    int i = 1;
    for (i = 0; i < 7; i++)
    {
        printf("masA[%d] = ",i);
        printf("%d \n", masA[i]);
    }



    getchar();
    system("cls");
    printf("\t\t\t Task 2 \n");




    int Matrix_1[2][2] = { {1, 1}, {1, 4} };
    int Matrix_2[2][2] = { {1, 2}, {4, 1} };

    int Matrixmultiplication[2][2];

    for (d = 0; d < 2; d++)
    {
        for (t = 0; t < 2; t++)
        {
            for (i = 0; i < 2; i++) {
                Matrixmultiplication[d][t] += Matrix_1[d][i] * Matrix_2[i][t];
            }
        }
    }

    int d, t;
    for (d = 0; d < 2; d++)
    {
        for (t = 0; t < 2; t++)
        {
            printf("Matrixmultiplication[%d][%d] = ", d, t);
            printf("%d \n", Matrixmultiplication[d][t]);
        }
    }


    getchar();
    return 0;
}
