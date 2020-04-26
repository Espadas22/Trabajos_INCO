#include <stdio.h>
#include <stdlib.h>

void factorial(int n);

int main ()
{
    int n;

    printf("Dame un numero para calcular su factorial:\n");
    scanf("%i", &n);

    factorial(n);

    printf("\n");
    system("pause");
    return (0);
}

void factorial(int n)
{
    long int f = 1;

    for (int i = 2; i <= n; i++)
    f *= i;

    printf("El factorial de %i es %ld\n", n, f);
}

