#include <stdio.h>
#include <stdlib.h>

void cubiton(long int *);

int main()
{
    long int cubo;

    printf("Dame un numero para elevar al cubo\n");
    scanf("%ld", &cubo);

    printf("El cubo de %ld ", cubo);

    cubiton(&cubo);

    printf("es %ld", cubo);

    printf("\n");
    system("pause");
    return (0);
}

void cubiton(long int *valor)
{
    *valor = (*valor)*(*valor)*(*valor);
}
