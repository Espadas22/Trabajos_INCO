#include <stdlib.h>
#include <stdio.h>

void cubiton(int n);

int main()
{
    for (int i = 1; i < 6; i++)
        cubiton(i);

    printf("\n");
    system("pause");
    return (0);
}

void cubiton(int n)
{
    int cubo = n*n*n;
    printf("El cubo de %i es %i\n", n, cubo);
}
