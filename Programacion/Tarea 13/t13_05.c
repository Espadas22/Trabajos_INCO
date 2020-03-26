#include <stdio.h>
#include <conio.h>
#include <string.h>

char frase[300];
int longitud, paso;

int main()
{
    printf("Dame la frase a traducir:\n");
    gets(frase);

    longitud = strlen(frase);
    //se divide la longitud entre 2 para intercambiar las variables
    for(int i = 0; i < longitud/2; i++)
    {
        paso = frase[i];//Se cambia la primera
        frase[i] = frase[longitud-1-i];//Con la ultima
        frase[longitud-1-i] = paso;//Hasta llegar al centro
    }

    printf("\nLa frase traducida es:\n%s", frase);


    getch();
    return(0);
}
