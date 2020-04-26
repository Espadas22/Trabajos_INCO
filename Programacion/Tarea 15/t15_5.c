#include <stdio.h>
#include <stdlib.h>

void f(int *, float *);

int main ()
{
    int entero = 22;
    float real = 33.3;

    printf("Antes de llamas a f entero vale %d y real vale %6.2f\n", entero, real);

    f(&entero, &real);

    printf("\nDespues de volver de f entero vale %d y real vale %6.2f\n\n", entero, real);

    system("pause");
    return (0);
}

void f(int *p, float *q)
{
    printf("\nAl entrar en f *p (= entero) vale %d y *q (= real) vale %6.2f\n", *p, *q);

    *p = 7777;
    *q = 12345.67;

    printf("\nAl salir de f *p vale %d y *q vale %6.2f\n", *p, *q);
}
