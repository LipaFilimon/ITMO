#include <stdio.h>
#include <stdlib.h>

/*int SumNumbers(int a, int b) {
    return a + b;
}
*/

int main(int argCount, int *argv[])
{
    printf("\t\t Task 1.\n\n");

    freopen("../NewFile.txt", "w", stdout);

    int a = atoi(argv[1]);
    int b = atoi(argv[2]);
    int sum = a + b;
    printf("%d + %d = %d", argv[1], argv[2], sum);






    /*FILE *output = fopen("NewFile.txt", "w");

    int i;
    for(i = 0; i < 2; i++)
    {
        printf("argv[%d]=",i);
        scanf("%d", &argv[i]);
    }



    int sumNumber = SumNumbers(argv[0], argv[1]);

    printf("%d + %d = %d", argv[0], argv[1], sumNumber);
    fprintf(output, "%d + %d = %d", argv[0], argv[1], sumNumber);

    fclose(output);
*/

   // getchar();
    return 0;
}
