#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>

int main()
{
	printf("\t\t\t Task 1 \n");

	int i;
    const char ArraySize = 4;

	float *Array, TransitArray[ArraySize];
    Array = TransitArray;

    printf("Enter array values: \n");
    for (i = 0; i < ArraySize; ++i) {
        scanf("%f", Array + i);
    }

    printf("\nArray values: \n");
    for (i = 0; i < ArraySize; ++i) {
        printf("Array[%d] = %.1f \n",i, Array[i]);
    }


    getchar();getchar();
    system("cls");
    printf("\t\t\t Task 2 \n\n");


    float *array;
    array = (float*)malloc(ArraySize * sizeof(float));

    printf("Enter array values: \n");
    for (i = 0; i < ArraySize; i++)
    {
      scanf("%f", &array[i]);
    }

    printf("\nArray values: \n");
    for (i = 0; i < ArraySize; i++)
    {
      printf("array[%d] = %.1f \n",i , array[i]);
    }
    free(array);
    *array = 0;



	getchar();
	return 0;
}
