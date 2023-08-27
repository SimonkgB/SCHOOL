#include <stdio.h>
#include <math.h>

#define PI 3.14159265358979323846

int main() {
    double x, y;
    FILE *f = fopen("data.txt", "w");

    for (x = 0; x < 2 * PI; x += 0.1) {
        y = sin(x);
        fprintf(f, "%lf %lf\n", x, y);
    }

    fclose(f);
    return 0;
}