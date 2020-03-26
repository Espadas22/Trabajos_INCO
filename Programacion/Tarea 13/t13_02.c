#include <stdio.h>
#include <conio.h>
#include <ctype.h>
#include <string.h>

char frase[300];
int limite, palabras = 1;//Palabras se inicia en uno, pues es la minima cantidad posible en la frase

int main()
{
    printf("Vamos a contar palabras. Escribe una frase y ponle punto al terminar:\n");

    do
    {
        gets(frase);

        limite = strlen(frase);

        if (frase[limite-1] != '.') //Revisamos que termine en punto
        {
            printf("\nEsta frase no termina en punto, ingresala de nuevo\n");
            fflush(stdin);//Limpiamos entrada para evitar tomar basura
        }
    } while (frase[limite-1] != '.'); //Ciclamos hasta que la frase ingresada termine en punto

    for (int i = 0; i<limite; i++)
    {
        if (!(isgraph(frase[i])) && isgraph(frase[i-1]) && isgraph(frase[i+1]))
            palabras++;//La validacion para saber si se tiene una palabra consta de verificar
            //si antes y despues de un espacio podemos encontrar un caracter imprimible
    }

    printf("\nEsta frase tiene %i palabras\n", palabras);

    getch();
    return(0);
}
