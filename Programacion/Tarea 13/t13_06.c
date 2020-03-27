#include <stdio.h>
#include <conio.h>
#include <ctype.h>
#include <string.h>

char contrasenia[300];//Se declara mas espacio en caso de que la contraseña ingresada sea mayor

int largo, mayuscula, especial, numero;
//Estas son banderas que nos indicaran si los requisitos son cumplidos
int total = 0;//Aqui sumaremos las condiciones

int main()
{   printf("Bienvenido al validador de contrasenias\n");
    printf("\nNecesitas:\n8 caracteres\nAl menos una mayuscula\n");
    printf("Al menos un caracter especial\nAl menos un digito\n");

    do
    {
        largo = 0, mayuscula = 0, especial = 0, numero = 0;
        printf("\nDame una contrasenia que cumpla los parametros:\n");
        gets(contrasenia);

        if (strlen(contrasenia) == 8)//solo se hace si cumple con la longitud
        {
            largo = 1;//se valida la longitud

            for (int i = 0; i < 8; i++)
            {
                if(isupper(contrasenia[i]))
                    mayuscula = 1;//se valida la mayuscula
                if(ispunct(contrasenia[i]))
                    especial = 1;//se valida el caracter especial
                if(isdigit(contrasenia[i]))
                    numero = 1;//se valida el numero
            }

            total = largo + mayuscula + especial + numero;

            if (total < 4)//en caso de no cumplir los parametros
            {
                printf("\nContrasenia invalida:\n");
                //revisamos que falto
                if(mayuscula == 0)
                    printf("No tiene al menos una mayuscula\n");
                if(especial == 0)
                    printf("Falto al menos un caracter especial\n");
                if(numero == 0)
                    printf("Falto al menos un numero\n");

                printf("\nIntentalo de nuevo\n");
                fflush(stdin);//evita que se lea basura
            }
        }
        else
            printf("\nLa contrasenia debe tener 8 caracteres\n");

    } while (total < 4);//Si alguna condicion no se cumple el ciclo se reinicia

    printf("\nContrasenia valida\n");

    getch();
    return(0);
}
