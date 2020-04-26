#include <stdio.h>
#include <stdlib.h>

void clonar(int repeticiones, char caracter);

int main()
{
    int repeticiones;
    char caracter;

    printf("Dame un caracter:\n");
    scanf("%c", &caracter);

    printf("\nCuantas veces quieres que se repita?\n");
    scanf("%i", &repeticiones);

    clonar(repeticiones, caracter);

    printf("\n");
    system("pause");
    return (0);
}

void clonar(int repeticiones, char caracter)
{
    printf("\n");

    for(int i = 0; i < repeticiones; i++)
        printf("%c", caracter);

    printf("\n");
}
