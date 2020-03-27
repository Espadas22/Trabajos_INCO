#include <stdio.h>
#include <conio.h>
#include <ctype.h>
#include <string.h>

char cadena[300];
int conteo = 0;//Se usara para llevar el conteo de los parentesis
int desbalance = 0;//Bandera para indicar que el balance no es correcto

int main()
{
    printf("Dame una cadena para evaluar sus parentesis:\n");
    gets(cadena);

    int limite = strlen(cadena);
    //validamos que la cadena abra/cierre correctamente
    if (cadena[0] == ')' || cadena[limite-1] == '(')
        printf("\nLa cadena tiene un orden erroneo de parentesis");
    else//Si abre/cierra bien, procedemos a analizar el interior
    {
        for (int i = 0; i < limite; i++)
        {
            if (cadena[i] == '(')
                conteo++;//toda llave que se abra sumara un punto
            else if (cadena[i] == ')')
                conteo--;//toda llave que se cierre restara un punto

            if (conteo < 0)//si en algun punto el conteo es menor a 0
                desbalance = 1;//Una llave cerro sin ninguna que abriera
        }

        //Damos el veredicto de la cadena
        if (desbalance == 1)
            printf("\nLa cadena tiene un orden erroneo de parentesis");
        else if (conteo > 0)//Algun parentesis abrio y no cerro
            printf("\nLa cadena tiene un orden erroneo de parentesis");
        else if (conteo == 0)//Sabemos que el conteo esta bien, pues validamos la excepcion al inicio
            printf("\nLa cadena tiene un orden correcto en sus parentesis");
    }

    getch();
    return(0);
}
