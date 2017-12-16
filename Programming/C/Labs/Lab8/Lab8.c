#include<stdio.h>
#include<string.h>

int String(char str[100])
{
    gets(str);
    printf("Your string: ");
    puts(str);
}


int main()
{
	printf("\t\t Task 1.The concatenation of two strings.\n\n");

	printf("Enter the first string: ");
	char str1[100];
	String(str1);
	printf("Enter the second string: ");
	char str2[100];
	String(str2);
	printf("\n");

	strcat(str1, str2);
	puts(str1);


	getchar();
    system("cls");
    printf("\t\t Task 2.The comparison of two strings.\n\n");


    printf("Enter the first string: ");
	char str3[100];
	String(str3);
	printf("Enter the second string: ");
	char str4[100];
	String(str4);
	printf("\n");

    int i = strcmp(str3, str4);
    if (i == 0)
	{
		printf("Strings are the same\n");
	}
	else
	{
		printf("Strings are different\n");
	}


	getchar();
    system("cls");
    printf("\t\t Task 3.The copying one string to another string.\n\n");


    char str5[100];
	char str6[100];
    printf("Enter the first string: ");
    gets(str5);
    printf("Enter the second string: ");
	gets(str6);
	printf("\nString 1: %s\n", str5);
	printf("String 2: %s\n", str6);

	int n;
	printf("\nEnter the number of characters \n");
	scanf("%d", &n);
	strncpy(str5, str6, n);
	printf("\nString 1: %s\n", str5);
	printf("String 2: %s\n", str6);


	getchar();getchar();
    system("cls");
    printf("\t\t Task 4.Determine the length of a string.\n\n");

    printf("Enter first string: ");
	char str7[100];
	String(str7);
    printf("The length of a string: %d",strlen(str7));


    getchar();
    system("cls");
    printf("Task 5.Determine the length of a segment of one string that doesn't contain the characters of the second string.\n\n");

    printf("Enter first string: ");
	char str8[20];
	gets(str8);
	printf("Enter first string: ");
	char str9[20];
	gets(str9);

    printf("Length of a segment: %d\n",strcspn(str8, str9));



	getchar();
	return 0;
}
