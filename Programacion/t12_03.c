#include <stdio.h>
#include <conio.h>

int matriz[3][3], arreglo[9], valores[9], repeticiones[9];
int maximo, max_x, max_y, minimo, min_x, min_y;
int inicio = 1, contador = 0, desplazamiento = 0, moda = 0;

int main()
{
    printf("Introduce una matriz de 3x3\n");
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            scanf("%i", &matriz[i][j]);

            arreglo[contador] = matriz[i][j];
            contador++;

            if (inicio == 1)
            {
                maximo = matriz[i][j];
                minimo = matriz[i][j];
                inicio = 0;
            }

            if (matriz[i][j] > maximo)
            {
                maximo = matriz[i][j];
                max_x = i;
                max_y = j;
            }
            if (matriz[i][j] < minimo)
            {
                minimo = matriz[i][j];
                min_x = i;
                min_y = j;
            }
        }
    }

    printf("\nEl valor maximo fue %i, encontrado en la posicion (%i, %i)\n", maximo, max_x, max_y);
    printf("El valor minimo fue %i, encontrado en la posicion (%i, %i)\n",  minimo, min_x, min_y);


    for (int i = 0; i < 9; i++)
    {
        contador = 0;
        valores[i] = arreglo[0];

        for (int j = 0; j < 9 - desplazamiento; j++)
        {
            if (arreglo[j] == valores[i])
            {
                contador++;
                desplazamiento++;
                for(int n = j; n < 9 - desplazamiento; n++)
                {
                    arreglo[n] = arreglo [n+1];
                }
                j--;
            }

        }
        repeticiones[i] = contador;
        if (repeticiones[i] > moda)
            moda = repeticiones[i];
    }

    if (moda == 1)
        printf("\nEl conjunto no tiene moda");
    else if (moda > 1)
    {
        printf("\nLa moda es: ");

        for (int i = 0; i < 9; i++)
        {
            if (moda == repeticiones[i])
                printf("%i ", valores[i]);
        }
    }


    getch();
    return (0);
}
