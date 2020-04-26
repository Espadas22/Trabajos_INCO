#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

char *cadena;
int largo;

void superMushroom(char *, int largo);

int main()
{
    cadena = (char*)malloc(100*sizeof(char));

    if (cadena == NULL)
        printf("Error asignando memoria\n");

    printf("Dame una frase para convertir a mayuscula:\n");
    gets(cadena);

    largo = strlen(cadena);

    cadena = (char*)realloc(cadena, (largo+1)*sizeof(char));

    if (cadena == NULL)
        printf("Error asignando memoria\n");

    superMushroom(cadena, largo);

    printf("%s\n", cadena);

    printf("\n");
    system("pause");
    return (0);
}

void superMushroom(char *cadena, int largo)
{
    for (int i = 0; i < largo; i++)
        cadena[i] = toupper(cadena[i]);//Se cambia el caracyer de la cadena por su equivalente en mayuscula
}
