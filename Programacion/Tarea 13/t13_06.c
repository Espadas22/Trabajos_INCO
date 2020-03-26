#include <stdio.h>
#include <conio.h>
#include <ctype.h>
#include <string.h>

char contrasenia[300];//Se declara mas espacio en caso de que la contraseña ingresada sea mayor

int largo = 0, mayuscula = 0, especial = 0, numero = 0;
//Estas son banderas que nos indicaran si los requisitos son cumplidos
int total = 0;//Aqui sumaremos las condiciones

int main()
{   printf("Bienvenido al validador de contrasenias\n")

    do
    {
        printf("Dame una contrasenia que cumpla los parametros:\n");
        gets(contrasenia);



    } while (total < 4);//Si alguna condicion no se cumple el ciclo se reinicia

    getch();
    return(0);
}
