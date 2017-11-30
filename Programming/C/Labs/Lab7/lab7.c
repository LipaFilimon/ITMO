#include <stdio.h>
#include <math.h>

enum Months
{
	January = 1,
	February,
	March,
	April,
	May,
	June,
	July,
	August,
	September,
	October,
	November,
	December
};

struct LineSegment
{
	int A;
	int B;
} AB;

void length_LineSegment (int A,int B)
{
	int length = B - A;
	printf("Length of line segment AB is %d \n", length);	
}

union Modem 
{
    unsigned short status;
    struct 
    {
        unsigned short DSL : 1;
        unsigned short PPP : 1;
        unsigned short Link : 1;
    } bitStatus;
} modem;

char *sModem (int status) 
{
    return status == 1 ? "On" : "Off";
}


int main ()
{
	printf("\t\t\t Task 1 \n");

	printf("July = %d\n", July );


	getchar();
    system("cls");
    printf("\t\t\t Task 2 \n\n");


    AB.A = 5;
    AB.B = 8;
    length_LineSegment(AB.A, AB.B);



    getchar();
    system("cls");
    printf("\t\t\t Task 3 \n\n");


    printf("Enter modem status (hex): ");
    scanf("%x", &modem.status);

    printf("DSL is %s\n", sModem(modem.bitStatus.DSL));
    printf("PPP is %s\n", sModem(modem.bitStatus.PPP));
    printf("Link is %s\n", sModem(modem.bitStatus.Link));

    getchar();
	return 0;
}
