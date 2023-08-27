#include <stdio.h>



int main()
{   
    int direction = 1;

    switch (direction)  // this whole thing is the same as an if statement so if direction =1 go north 
    {
    case 1:
        printf("Go north");
        break;
    case 2:
        printf("Go south");
        break;
    case 3:
        printf("Go west");
        break;
    case 4:
        printf("Go east");
        break;
    
    default:
        printf("Stay still"); // same as else
        break;
    }
    return 0;
}

