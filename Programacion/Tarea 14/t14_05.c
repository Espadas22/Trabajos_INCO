#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *cadena = NULL;
char *descodificada = NULL;
int registro = 0;

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
        //Ciclo for que agrega la letra seuun marque la posicion
        for (int j = 0; j < cadena[i] - 48; j++)
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
