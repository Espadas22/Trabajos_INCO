#include <stdio.h>
#include <conio.h>
#include <string.h>

char frase[300];
int longitud;

int main()
{
    printf("Dame la frase a traducir:\n");
    gets(frase);

    longitud = strlen(frase) + 1;//Se suma 1 porque lens no considera el caracter NULL

    char inverso[longitud];//para que el espacio NULL se respeta al hacer el cambio

    for (int i = 0; i < longitud; i++)
    {
        inverso[i] = frase[longitud-2-i];
    }//Se le resta dos a longitud porque un espacio corresponde al aumentado y otro al caracter nulo

    printf("\nLa frase traducida es:\n%s", inverso);

    getch();
    return (0);
}
