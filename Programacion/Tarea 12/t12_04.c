#include <stdio.h>
#include <conio.h>

float matriz[4][4], promedio, divisor;

int main ()
{
    printf("Vamos a calcular promedio, ingresa los 3 elementos de cada fila\n");

    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            scanf("%f", &matriz[i][j]);

            if (j == 2)
            {
                promedio = 0;
                for (int n = j; n >= 0; n--)
                {
                    promedio += matriz[i][n];
                }
                divisor = j+1;
                matriz[i][j+1] = promedio/(divisor);
            }
        }
    }

    printf("\nLa matriz con promedios es:\n");
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            if (j < 3)
                printf("%.0f ", matriz[i][j]);
            else if (j == 3)
                printf("%.2f\n", matriz[i][j]);
        }
    }

    getch();
    return (0);
}
