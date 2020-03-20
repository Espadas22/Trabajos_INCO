#practica 09
#espadas rodriguez anthony jonathan
#mariscal cervantes diego maximiliano 

print("practica  09");
print("espadas rodriguez anthony jonathan");
print("mariscal cervantes diego maximiliano\n");

def validarValor():
    try:
        valor = int(input("Introduce un valor valido\n"));
        if valor < 0:
            print("El valor no puede ser menor que cero");
            valor = validarValor();
    except:
        print("Los valores deben ser numeros enteros");
        valor = validarValor();
    return valor;

def validarEleccion():
    eleccion = str(input("Ingresa una respuesta valida\n"));
    if (eleccion != "si") & (eleccion != "no"):
        print("Las respuestas solo pueden ser 'si' o 'no'");
        eleccion = validarEleccion();
    return eleccion;

def validarCalificacion():
    try:
        calificacion = float(input("Ingresa un valor dentro del rango\n"));
        if (calificacion < 0) | (calificacion > 100):
            print("Las calificaciones deben estar entre 0 y 100");
            calificacion = validarCalificacion();
    except:
        print("La calificacion debe ser un numero entre 0 y 100");
        calificacion = validarCalificacion();
    return calificacion;

def e01(): #Calculo de descuentos en un teatro segun edad
    for i in range(1):
        def capturarCliente(): #funcion que se ejecuta cada que el usuario decida ingresar un nuevo cliente
            contador_r = 0; #contador axuliar para registrar cambios dentro de la funcion
            perdidas_r = 0; #contenedor auxuliar que guarda los descuentos aplicados dentro de la funcion;
            boleto = 80;
            
            try:
                edad = int(input("\nIngresa la edad del cliente:\n"));

                if edad < 0:
                    print("La edad no puede ser menor que cero");
                    edad = validarValor();
            except:
                print("\nLa edad solo puede ser un numero entero");
                edad = validarValor();

            if edad < 5:
                print("\nLo sentimos, no ingresan menores de 5 años");
            elif edad < 15:
                precio = boleto*.65;
                print("\nCategoria 1, tienes 35%% de descuento, paga solo %.2f" % (precio));
                perdidas_r += boleto - precio;
                contador_r += 1;
            elif edad < 20:
                precio = boleto*.75
                print("\nCategoria 2, tienes 25%% de descuento, paga solo %.2f" % (precio));
                perdidas_r += boleto - precio;
                contador_r += 1;
            elif edad < 46:
                precio = boleto*.90;
                print("\nCategoria 3, tienes 10%% de descuento, paga solo %.2f" % (precio));
                perdidas_r += boleto - precio;
                contador_r += 1;
            elif edad < 65:
                precio = boleto*.75
                print("\nCategoria 4, tienes 25%% de descuento, paga solo %.2f" % (precio));
                perdidas_r += boleto - precio;
                contador_r += 1;
            elif edad < 125:
                precio = boleto*.65;
                print("\nCategoria 5, tienes 35%% de descuento, paga solo %.2f" % (precio));
                perdidas_r += boleto - precio;
                contador_r += 1;
            else:
                print("\nNadie ha vivido tanto, verifique sus datos")

            eleccion = str(input("\nQuieres ingresar otro usuario? (si/no)\n"));

            if (eleccion != "si") & (eleccion != "no"):
                print("Las respuestas solo pueden ser 'si' o 'no'")
                eleccion = validarEleccion();

            if eleccion == "si":
                contador_rr, perdidas_rr = capturarCliente(); #dentro cada llamado a la funcion se genera un contador y un descuento
                contador_r += contador_rr; #que se suman a los anteriores
                perdidas_r += perdidas_rr;
                return contador_r, perdidas_r;
            elif eleccion == "no":
                return contador_r, perdidas_r; #y se regresan al metodo principal

    contador, perdidas = capturarCliente();#aqui se reciben todas las variables acumuladas en la recurrencia
    
    #y se imprimen    
    print("\nSe ingresaron un total de", contador, "clientes");
    print("El total de descuentos otorgado por el teatro fue de %.2f pesos" % (perdidas))
    

def e02(): #Calculador de masa de aire en n vehiculos
    dsds


def menu():
    eleccion = 11;
    while eleccion != 0:
        print("\nElije un ejercicio para ejecutar:");
        print("(1) Para determinar las perdidas de ingreso en un teatro segun la edad de sus clientes");
        print("(2) Para calcular el promedio de masa de aire de los neumaticos de n vehiculos");
        print("(3) Para calcular el precio del kilo de huevo segun sea la calidad de la gallina");
        print("(4) Para conocer la inclinacion de los diputados ante en TLC");
        print("(5) Realizar una suma de 2 en 2 (usando hexadecimal)");
        print("(6) Comprar la califiacion de n cantidad de alumnos");
        print("(0) Para salir\n");

        try:
            eleccion = int(input());
        except:
            print("La eleccion solo puede ser un numero entero");

        while (eleccion < 0) | (eleccion > 6):
            print("El valor debe estar entre 0 y 6");
            try:
                eleccion = int(input("Ingresa un valor dentro del rango\n"));
            except:
                print("La eleccion solo puede ser un numero entero");

        if eleccion == 1:
            e01();
        elif eleccion == 2:
            e02();
        elif eleccion == 3:
            e03();
        elif eleccion == 4:
            e04();
        elif eleccion == 5:
            e05();
        elif eleccion == 6:
            e06();

def imprimir():
    menu();

imprimir();
