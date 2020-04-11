#include <stdlib.h>
#include <stdio.h>

int **matriz = NULL, *arreglo = NULL, columnas, filas;
int i, j, pivote, menores = 0;

int main ()
{
    printf("Cuantas filas tendra la matriz?\n");
    scanf("%i", &filas);

    matriz = (int**)malloc(filas*sizeof(int*));

    if (matriz == NULL)
    {
        printf("Error asignando memoria");
        return(0);
    }

    printf("\nCuantas columnas tendra?\n");
    scanf("%i", &columnas);

    for (i = 0; i < filas; i++)
    {
        matriz[i] = (int*)malloc(columnas*sizeof(int));

        if (matriz[i] == NULL)
        {
            printf("Error al asignar memoria");
            return (0);
        }
    }

    printf("\nDame los elementos de la matriz:\n");
    for (i = 0; i < filas; i++)
    {
        for (j = 0; j < columnas; j++)
        {
            scanf("%i", &matriz[i][j]);
        }
    }

    printf("\nTu matriz se ve asi:\n");
    for (i = 0; i < filas; i++)
    {
        for (j = 0; j < columnas; j++)
        {
            printf("%i ", matriz[i][j]);
        }
        printf("\n");
    }

    printf("\nDame un numero para comparar:\n");
    scanf("%i", &pivote);

    arreglo = (int*)malloc(menores*sizeof(int));

    for (i = 0; i < filas; i++)
    {
        for (j = 0; j < columnas; j++)
        {
            if (matriz[i][j] < pivote)
            {
                //Se agrega al contador
                menores++;
                //Se dimensiona el arreglo para la nueva cantidad de elementos
                arreglo = (int*)realloc(arreglo, menores*sizeof(int));
                //Se asigna el nuevo elemento
                arreglo[menores - 1] = matriz[i][j];
            }
        }
    }

    if (menores == 0)
    {
        printf("\nEste arreglo no cuenta con numeros menores a %i", pivote);
    }
    else
    {
        printf("\nLos numeros menores a %i son: ", pivote);
        for (i = 0; i < menores; i++)
        {
            printf("%i ", arreglo[i]);
        }
    }

    free(matriz);
    free(arreglo);
    printf("\n\n");
    system("pause");
    return (0);
}
