#ifndef CIRCLE_H
#define CIRCLE_H

double calcSquare(int);
int calcLength(int);
struct Circle createCircle();

struct Circle
{
	
    int radius;
    int x, y;
    double square;
    int length;

};

#endif