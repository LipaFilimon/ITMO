#include <stdio.h>
#include <stdbool.h>

int main()
{
	printf("\t\t Task 1\n\n");


	int Numbers=0, Capital=0, Cursive=0;
    char str[300]={"\0"};

    printf("String: ");
    gets(str);

    int n;
    for (n = 0; n < sizeof(str) / sizeof(char) - 1; n++)
    {
        if (str[n] >= '0' && str[n] <= '9')
        {
        	Numbers++;
        }        
        else 
        	{
        		if (str[n] >= 'A' && str[n] <= 'Z')
        		{
        			Capital++;
        		} 
                else
                    {
                	    if (str[n] >= 'a' && str[n] <= 'z')
                	    {
                		    Cursive++;
                	    }          
                    } 
        	}
    }

    printf("\nNumbers: %d\n", Numbers);
    printf("Capital letters: %d\n", Capital);
    printf("Cursive letters: %d\n\n", Cursive);


    getchar();
    system("cls");
    printf("\t\t Task 4\n\n");


    int i, j;
    bool flag;
    Numbers=0;

    printf("Enter the number\n");
    scanf("%d", &Numbers);
    for (i = 2; i <= Numbers; i++)
    {
        flag = true;
        for (j = 2; j <= (i - 1); j++)
        {
            if (i % j == 0)
            {
                flag = false;
            }
        }
        if (flag == true)
        {
            printf("%d ", i);
        }
    }

    return 0;
}
