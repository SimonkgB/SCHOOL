
#include <stdio.h>
/*
int main()
{   
    int matrix[2][3] = 
    {
        {1,2,3},
        {4,5,6}
    };
    
    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            printf("%d ", matrix[i][j]);
        }
        printf("\n");
    }

    return 0;
}
*/

/*
int main()
{   
    int vector[]= {1,2,3,4,5};

    int len = sizeof(vector)/sizeof(vector[0]);

    int ans = 0;

    for (int i = 0; i < len; i++)
    {
        ans += vector[i];
    }
    printf("sum = %d",ans);

    return 0;
}
*/
#include <stdio.h>

int main()
{   
    int vector[] = {4,2,5,3,1};

    int len = (sizeof(vector)/sizeof(vector[0]));

    //buble sort algorythm

    for (int i = 0; i < len-1; i++)
    {
        for (int j = 0; j < len-1; j++)
        {
            if (vector[j]>vector[j+1])
            {
                int temp = vector[j];
                vector[j]=vector[j+1];
                vector[j+1] = temp;
            }
        }
    }
    for (int i = 0; i < len; i++)
    {
        printf("%d\n",vector[i]);
    }
    return 0;
}

