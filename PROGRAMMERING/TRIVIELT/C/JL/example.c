#include <stdio.h>

void myswitch(int direction)
{
    switch (direction)
    {
    case 1:
        printf("Go North\n");
        break;
    case 2:
        printf("Go South\n");
        break;
    case 3:
        printf("Go East\n");
        break;
    case 4:
        printf("Go West\n");
        break;
    
    default:
        printf("Stay Still\n");
        break;
    }
}