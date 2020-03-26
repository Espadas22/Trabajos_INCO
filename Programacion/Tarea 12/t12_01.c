#include <stdio.h>
#include <conio.h>

int matriz [5][8], renglon, columna;

int main ()
{
    printf("Dame los elementos de una matriz de 5x8\n");

    for (int i = 0; i < 5; i ++)
    {
        for (int j = 0; j < 8; j++)
        {
            scanf("%i", &matriz[i][j]);
        }
    }
    fflush(stdin);

    printf("\nAsi se ve la matriz:\n");

    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 8; j++)
        {
            printf("%i ", matriz[i][j]);
            if (j == 7)
                printf("\n");
        }
    }

    printf("\nDame una posicion para cambiar (columna)\n");

    do
    {
        scanf("%i", &columna);
        fflush(stdin);
        if (columna > 8 || columna < 1)
        {
            printf("El valor de columna esta fuera de rango (1 a 8)\n");
            printf("Introducelo nuevamente\n");
        }
    } while (columna > 8 || columna < 1);

    printf("\nDame una posicion para cambiar (renglon)\n");

    do
    {
        scanf("%i", &renglon);
        fflush(stdin);
        if (renglon > 5 || renglon < 1)
        {
            printf("El valor de renglon esta fuera de rango (1 a 5)\n");
            printf("Introducelo nuevamente\n");
        }
    } while (renglon > 5 || renglon < 1);


    printf("\nDame el nuevo valor de la posicion (%i, %i)\n", columna, renglon);
    scanf("%i", &matriz[5-renglon][columna-1]);
    fflush(stdin);

    printf("\nLa nueva matriz se ve asi:\n");

    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 8; j++)
        {
            printf("%i ", matriz[i][j]);
            if (j == 7)
                printf("\n");
        }
    }

    getch();
    return (0);
}
