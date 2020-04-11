#include <stdio.h>
#include <stdlib.h>

int **matriz_original, **matriz_invertida, filas, columnas;

int main()
{
    printf("Cuantas columnas tendra tu matriz?\n");
    scanf("%i", &columnas);

    printf("\nY cuantas filas tendra?\n");
    scanf("%i", &filas);

    //Se inician ambas matrices
    matriz_original = (int**)malloc(columnas*sizeof(int*));
    matriz_invertida = (int**)malloc(filas*sizeof(int*));

    if (matriz_original == NULL || matriz_invertida == NULL)
    {
        printf("Error al asignar memoria");
        return (0);
    }

    //Se genenran las filas dentro de ellas
    for (int i = 0; i < columnas || i < filas; i++)
    {
        //Controla las filas que se incertan la matriz original
        if (i < columnas)
        {
            matriz_original[i] = (int*)malloc(filas*sizeof(int));
        }
        //Controla las filas que se insertan en la matriz invertida
        if (i < filas)
        {
            matriz_invertida[i] = (int*)malloc(columnas*sizeof(int));
        }

        if (matriz_original[i] == NULL || matriz_invertida == NULL)
        {
            printf("Error al asignar memoria");
            return (0);
        }
    }

    printf("\nIngresa los elementos de tu matriz:\n");
    for (int i = 0; i < columnas; i++)
    {
        for (int j = 0; j < filas; j++)
        {
            //Se registra la posicion en la matriz original y se
            //copia en su posicion analoga dentro de la invertida
            scanf("%i", &matriz_original[i][j]);
            matriz_invertida[j][i] = matriz_original[i][j];
        }
    }

    printf("\nsu forma invertida es:\n");
    for (int i = 0; i < filas; i++)
    {
        for (int j = 0; j < columnas; j++)
        {
            printf("%i ", matriz_invertida[i][j]);
        }
        printf("\n");
    }

    free(matriz_original);
    free(matriz_invertida);
    printf("\n");
    system("pause");
    return (0);
}
