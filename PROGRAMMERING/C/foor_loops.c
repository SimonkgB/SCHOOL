#include <stdio.h>
/*
int main()
{   
    int vector[] = {1, 2, 3, 4, 5};
    int len = (sizeof(vector) / sizeof(vector[0]));
    for (int i = 0; i < len; i++)
    {
        printf("%d\n", vector[i]);
    }
    return 0;
}
*/

#include <string.h>
int main()
{   
    char string[] = "Hello, World!";

    int len = strlen(string);

    for (int i = 0; i < len; i++)
    {
        printf("%c\n", string[i]);
    }

    return 0;
}