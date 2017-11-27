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

    Matrixmultiplication[0][0] = Matrix_1[0][0] * Matrix_2[0][0] + Matrix_1[0][1] * Matrix_2[1][0];
    Matrixmultiplication[0][1] = Matrix_1[0][0] * Matrix_2[0][1] + Matrix_1[0][1] * Matrix_2[1][1];
    Matrixmultiplication[1][0] = Matrix_1[1][0] * Matrix_2[0][0] + Matrix_1[1][1] * Matrix_2[1][0];
    Matrixmultiplication[1][1] = Matrix_1[1][0] * Matrix_2[0][1] + Matrix_1[1][1] * Matrix_2[1][1];

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
