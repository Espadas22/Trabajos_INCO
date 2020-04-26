#include <stdlib.h>
#include <stdio.h>
#include <conio.h>

void suma();
void resta();
void multiplicacion();
void division();
void potencia();

int main()
{
    int continuar = 1;
    int eleccion;

    while (continuar != 0)
    {
        printf("\nQue operacion quieres realizar?\n");
        printf("(1) Suma\n(2) Resta\n(3) Multiplicacion\n");
        printf("(4) Division\n(5) Potencia\n\n");

        scanf("%i", &eleccion);

        switch(eleccion)
        {
            case 1:
                suma();
                break;
            case 2:
                resta();
                break;
            case 3:
                multiplicacion();
                break;
            case 4:
                division();
                break;
            case 5:
                potencia();
                break;
            default:
                printf("Error capturando eleccion\n");
        }

        printf("\nQuieres realizar otra operacion?\n(1) Si (0) No\n");
        scanf("%i", &continuar);
    }

    printf("\n");
    system("pause");
    return(0);
}
void suma()
{
    int a, b;

    printf("\nDame el primer numero:\n");
    scanf("%i", &a);

    printf("Cual le vamos a sumar?\n");
    scanf("%i", &b);

    int suma = a + b;

    printf("La suma de %i y %i es %i\n", a, b, suma);
    fflush(stdin);
}

void resta()
{
    int a, b;

    printf("\nDame el primer numero:\n");
    scanf("%i", &a);

    printf("Cual le vamos a restar?\n");
    scanf("%i", &b);

    int resta = a - b;

    printf("La resta de %i y %i es %i\n", a, b, resta);
    fflush(stdin);
}

void multiplicacion()
{
    int a, b;

    printf("\nDame el primer numero:\n");
    scanf("%i", &a);

    printf("Por cuanto lo vamos a multiplicar?\n");
    scanf("%i", &b);

    int producto = a * b;

    printf("El producto de %i y %i es %i\n", a, b, producto);
    fflush(stdin);
}

void division()
{
    float a, b;

    printf("\nDame el dividendo:\n");
    scanf("%f", &a);

    printf("Ahora el divisor\n");
    scanf("%f", &b);

    float cociente = a / b;

    printf("El cociente de %.0f entre %.0f es %.2f\n", a, b, cociente);
    fflush(stdin);
}

void potencia()
{
    int a, b;
    long int resultado = 1;

    printf("\nDame la base:\n");
    scanf("%i", &a);

    printf("Ahora el exponente?\n");
    scanf("%i", &b);

    for (int i = 0; i < b; i++)
        resultado *= a;

    printf("El resultado de elevar %i a la %i potencia es %ld\n", a, b, resultado);
    fflush(stdin);
}
