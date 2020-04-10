#include <stdio.h>
#include <stdlib.h>

int *arreglo;
int tamanio;

int main ()
{
    printf("Que tamanio tendra el arreglo?\n");
    scanf("%i", &tamanio);

    arreglo = (int*)malloc(tamanio*sizeof(int));

    if (arreglo == NULL)
    {
        printf("Error al reservar memoria\n");
        return (0);
    }

    printf("Dame los %i elementos de arreglo:\n", tamanio);

    for (int i = 0; i < tamanio; i++)
    {
        scanf("%i",&arreglo[i]);
    }

    printf("\nTu arreglo es: ");

    for (int i = 0; i < tamanio; i++)
    {
        printf("%i ", arreglo[i]);
    }

    free(arreglo);

    printf("\n");
    system("pause");
    return (0);
}
