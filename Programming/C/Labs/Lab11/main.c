#include "circle.h"
#include <stdio.h>
#include <math.h>

struct Circle createCircle()
{
    struct Circle circ;

    printf("Enter coordinates of the center of the circle:\n\n ");
    printf("x:");
    scanf("%d", &circ.x );
    printf("y:");
    scanf("%d", &circ.y);
    printf("Enter radius: ");
    scanf("%d", &circ.radius);
    printf("\n");

    circ.square = calcSquare(circ.radius);
    printf("Square of the circle is %lf\n", circ.square);

    circ.length = calcLength(circ.radius);
    printf("Length of the circle is %d\n", circ.length);

    return circ;
};

double calcSquare(int rad)
{
    return pow(rad, 2) * M_PI;
}

int calcLength(int rad)
{
    return 2 * M_PI *rad;
}