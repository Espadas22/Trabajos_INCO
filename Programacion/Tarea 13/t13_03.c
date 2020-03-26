#include <stdio.h>
#include <conio.h>
#include <ctype.h>
#include <string.h>

char nombre[50], apellido_P[50], apellido_M[50];
int lon_N, lon_P, lon_M; //variables que guardaran la longitud de las cadenas

int main()
{
    printf("Dame tu nombre:\n");
    scanf("%s", &nombre);

    printf("\nDame tu apellido paterno:\n");
    scanf("%s", &apellido_P);

    printf("\nDame tu apellido materno:\n");
    scanf("%s", &apellido_M);

    lon_N = strlen(nombre);
    lon_P = strlen(apellido_P);
    lon_M = strlen(apellido_M);

    for (int i = 0; i <= lon_N; i++)
    {
        if (i == 0)//Cambia el primer caracter a mayuscula
            nombre[i] = toupper(nombre[i]);
        else if (i == lon_N)
            nombre[i] = ' ';//Agrega el espacio al final
        else
            nombre[i] = tolower(nombre[i]);//cambia todo lo demas a minuscula
    }

    for (int i = 0; i <= lon_P; i++)
    {
        if (i == 0)
            apellido_P[i] = toupper(apellido_P[i]);
        else if (i == lon_P)
            apellido_P[i] = ' ';
        else
            apellido_P[i] = tolower(apellido_P[i]);
    }

    for (int i = 0; i < lon_M; i++)
    {
        if (i == 0)
            apellido_M[i] = toupper(apellido_M[i]);
        else
            apellido_M[i] = tolower(apellido_M[i]);
    }

    strcat(nombre, apellido_P);//Se le agrega el apellido paterno al nombre
    strcat(nombre, apellido_M);//Se le agrega el apellido materno a lo anterior

    printf("\nTu nombre completo es %s\n", nombre);

    getch();
    return(0);
}
