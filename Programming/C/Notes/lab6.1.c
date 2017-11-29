#include <stdio.h>

int i;

void showArray(const int *array, const int arrayLength) {
    printf("Array values: ");

    for (i = 0; i < arrayLength; ++i) {
        printf("%d ", array[i]);
    }

    printf("\n");
}

void readArray(int *array, const int arrayLength) {
    printf("Enter array values: ");

    for (i = 0; i < arrayLength; ++i) {
        scanf("%d", array + i);
    }
}

const char ArraySize = 4;

int main()
{
	int *firstArray, bufferArray[ArraySize];
    firstArray = bufferArray;

   /* readArray(firstArray, ArraySize);
    showArray(firstArray, ArraySize);*/


	getchar();
	return 0;
}