#include <stdio.h>
#include <conio.h>

int matriz_A[4][4], matriz_B[4][4], eleccion;

int main ()
{
    printf("Ejercicio con 2 matrices 4*4\n");
    printf("\nDame la matriz A\n");

    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            scanf("%i", &matriz_A[i][j]);
        }
    }

    printf("\nDame la matriz B\n");

    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            scanf("%i", &matriz_B[i][j]);
        }
    }

    fflush(stdin);

    printf("\nQue Operacion quieres hacer?\n");
    printf("(1) Sumar A y B\n");
    printf("(2) Multiplicar A y B\n");
    printf("(3) Sumar 2A + 5B\n");
    printf("(4) Transponer A\n");

    do {
        scanf("%i", &eleccion);
        fflush(stdin);
        if (eleccion > 4 || eleccion < 1)
        {
            printf("Esa opcion no es valida, intenta de nuevo\n");
        }
    }while (eleccion > 4 || eleccion < 1);

    switch(eleccion)
    {
        case 1:
            for (int i = 0; i < 4; i++)
            {
                for (int j = 0; j < 4; j++)
                {
                    matriz_A[i][j] = matriz_A[i][j] + matriz_B[i][j];
                }
            }

            printf("\nLa suma de las matrices es:\n");
            for (int i = 0; i < 4; i++)
            {
                for (int j = 0; j < 4; j++)
                {
                    printf("%i ", matriz_A[i][j]);
                    if (j == 3)
                        printf("\n");
                }
            }
            break;
        case 2:
            for (int i = 0; i < 4; i++)
            {
                for (int j = 0; j < 4; j++)
                {
                    matriz_A[i][j] = matriz_A[i][j] * matriz_B[i][j];
                }
            }

            printf("\nLa multiplicacion de las matrices es:\n");
            for (int i = 0; i < 4; i++)
            {
                for (int j = 0; j < 4; j++)
                {
                    printf("%i ", matriz_A[i][j]);
                    if (j == 3)
                        printf("\n");
                }
            }

            break;
        case 3:
            for (int i = 0; i < 4; i++)
            {
                for (int j = 0; j < 4; j++)
                {
                    matriz_A[i][j] = 2*matriz_A[i][j] + 5*matriz_B[i][j];
                }
            }

            printf("\nLa suma 2A + 5B es:\n");
            for (int i = 0; i < 4; i++)
            {
                for (int j = 0; j < 4; j++)
                {
                    printf("%i ", matriz_A[i][j]);
                    if (j == 3)
                        printf("\n");
                }
            }
            break;
        case 4:
            for (int i = 0; i < 4; i++)
            {
                for (int j = 0; j < 4; j++)
                {
                    matriz_B[j][i] = matriz_A[i][j];
                }
            }

            printf("\nLa transpolacion de A es:\n");
            for (int i = 0; i < 4; i++)
            {
                for (int j = 0; j < 4; j++)
                {
                    printf("%i ", matriz_B[i][j]);
                    if (j == 3)
                        printf("\n");
                }
            }
    }

    getch();
    return (0);
}
