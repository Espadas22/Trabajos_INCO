#include <stdio.h>
#include <stdlib.h>

//Prototipo de la funcion

void funcion1(void);

void main()
{
    int conta;

    funcion1();

    for (conta = 0; conta < 10; conta++)
    {
        funcion1();
    }

    system("pause");
}

//Cuerpo de la funcion
void funcion1()
{
    printf("Funcion que imprime un mensaje\n");
}
