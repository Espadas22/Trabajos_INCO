#include <stdio.h>
#include <conio.h>
#include <ctype.h>
#include <string.h>

char frase[300]; //Declaracion del arreglo que contendra la frase

int main()
{
    printf("Dame una frase\n");
    gets(frase);//Guarda la frase, incluyendo los espacios

    int limite = strlen(frase);//Se determina hasta donde hay que leer

    printf("\nVamos a cambiar su espacios por '*'\n\n");

    for (int i = 0; i < limite; i++)
    {
        if (!(isgraph(frase[i]))) //Determina cuando la posicion no es un caracter imprimible
        {
            frase[i] = '*';//Y se cambia por asterisco
        }
        printf("%c", frase[i]);
    }

    getch();
    return (0);
}
