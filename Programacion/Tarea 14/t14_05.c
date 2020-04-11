#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *cadena = NULL;
char *descodificada = NULL;
int registro = 0;
int repeticiones;

int main ()
{
    //Se asigna a las cadenas su tamanio maximo
    cadena = (char*)malloc(30*sizeof(char));
    descodificada = (char*)malloc(95*sizeof(char));

    if (cadena == NULL || descodificada == NULL)
    {
        printf("Error asignando memoeria\n");
        return (0);
    }

    printf("Dame la cadena a descodificar:\n");
    gets(cadena);

    //Se calcula su longitud
    int longitud = strlen(cadena);

    //Se redimensiona
    cadena = (char*)realloc(cadena, longitud*sizeof(char));

    if (cadena == NULL)
    {
        printf("Error al reasignar memoria");
        return (0);
    }

    //ciclo for que recorre la cadena
    for (int i = 0; i < longitud; i += 2)
    {
        //Evaluamos las repeticiones indicadas en la cadena
        switch (cadena[i])
        {
            case '1':
                repeticiones = 1;
                break;
            case '2':
                repeticiones = 2;
                break;
            case '3':
                repeticiones = 3;
                break;
            case '4':
                repeticiones = 4;
                break;
            case '5':
                repeticiones = 5;
                break;
            case '6':
                repeticiones = 6;
                break;
            case '7':
                repeticiones = 7;
                break;
            case '8':
                repeticiones = 8;
                break;
            case '9':
                repeticiones = 9;
                break;
            default:
                repeticiones = 0;
        }
        //Ciclo for que agrega la letra seguun marque la posicion
        for (int j = 0; j < repeticiones; j++)
        {

            //Se guarda la letra en la cadena descodificada
            descodificada[registro] = cadena[i+1];
            registro++; //Se mueve a la siguiente posicion
        }
    }

    //Se agrega el caracter nulo al final de la cadena
    descodificada[registro] = '\0';

    //Se reasigna longitud a la cadena descodificada
    descodificada = (char*)realloc(descodificada, (registro+1)*sizeof(char));

    printf("\nLa cadena descodificada es:\n%s\n", descodificada);

    free(descodificada);
    free(cadena);
    printf("\n");
    system("pause");
    return (0);
}
