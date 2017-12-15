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
	int Ax1, Ay1;                // Длинна отрезка
	int Bx2, By2;
} AB;

union Modem 
{
    unsigned status;
    struct 
    {
        unsigned short DSL : 1;
        unsigned short PPP : 1;
        unsigned short Link : 1;
    } bitStatus;
} modem;

/*char *sModem (int status) 
{
    return status == 1 ? "On" : "Off";
}*/


int main ()
{
	printf("\t\t\t Task 1 \n");

	printf("July = %d\n", July );


	getchar();
    system("cls");
    printf("\t\t\t Task 2 \n\n");


    // Вычисление длины отрезка на плоскости по заданным 
    // координатам двух точек
    AB.Ax1 = 5;
    AB.Ay1 = 4;
    AB.Bx2 = 8;
    AB.By2 = 8;
    int length = sqrt((pow(AB.Bx2-AB.Ax1,2))+(pow(AB.By2-AB.Ay1,2)));
    printf("A (5;4)\n");
    printf("B (8;8)\n");
	printf("Length of line segment AB is %d \n", length);


    getchar();
    system("cls");		
    printf("\t\t\t Task 3 \n\n");


    printf("Enter modem status (hex): ");
    scanf("%x", &modem.status);

    printf("DSL is %s\n", modem.bitStatus.DSL == 1 ? "On":"Off");
    printf("PPP is %s\n", modem.bitStatus.PPP == 1 ? "On":"Off");
    printf("Link is %s\n", modem.bitStatus.Link == 1 ? "On":"Off");

   /* printf("DSL is %s\n", sModem(modem.bitStatus.DSL));
    printf("PPP is %s\n", sModem(modem.bitStatus.PPP));
    printf("Link is %s\n", sModem(modem.bitStatus.Link));
*/
    getchar();
	return 0;
}
