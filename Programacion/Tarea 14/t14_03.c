#include <stdio.h>
#include <stdlib.h>

int **matriz, filas, columnas;

int main ()
{
    printf("Cuantas columnas tendra la matriz?\n");
    scanf("%i", &columnas);

    printf("\nY cuantas filas tendra?\n");
    scanf("%i", &filas);

    matriz = (int**)malloc(columnas*sizeof(int*));

    if (matriz == NULL)
    {
        printf("Error al asignar memoria");
        return (0);
    }

    for(int i = 0; i < columnas; i++)
    {
        matriz[i] = (int*)malloc(filas*sizeof(int));

        if (matriz[i] == NULL)
        {
            printf("Error al asignar memoria");
            return (0);
        }
    }

    printf("\nDame los elementos de la matriz:\n");

    for (int i = 0; i < columnas; i++)
    {
        for (int j = 0; j < filas; j++)
        {
            scanf("%i", &matriz[i][j]);
        }
    }

    printf("\nLa forma de tu matriz es:\n");

    for (int i = 0; i < columnas; i++)
    {
        for (int j = 0; j < filas; j++)
        {
            printf("%i ", matriz[i][j]);
        }
        printf("\n");
    }

    free(matriz);
    printf("\n");
    system("pause");
    return (0);
}
