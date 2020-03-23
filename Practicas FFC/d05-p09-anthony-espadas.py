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

def validarPositivo():
    try:
        valor = int(input("Introduce un valor valido\n"));
        if valor < 1:
            print("El valor debe ser un numero positivo");
            valor = validarPositivo();
    except:
        print("Los valores deben ser numeros enteros");
        valor = validarPositivo();
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
    

def e02(): #Calculador de masa promedio de aire en neumaticos
    def validarVehiculo():#funcion que valida la eleccion a los vehiculos disponibles
        eleccion = str(input("\nIngresa una opcion valida\n"));

        if(eleccion != "moto") & (eleccion != "auto"):
            print("Los resgistros solo pueden ser 'moto' o 'auto'");
            eleccion = validarVehiculo();

        return eleccion;

    def validarTemperatura(): #se encarga de que la temperatura este dentro de un rango funcional
        try:
            temperatura = float(input("Dame un valor valido\n"));

            if temperatura < -273.14:
                print("La temperatura no puede estar por debajo del cero absoluto");
                temperatura = validarTemperatura();
            elif temperatura > 150:
                print("Los neumatucos no pueden mantenerse a esa temperatura");
                temperatura = validarTemperatura();

        except:
            print("La temperatura debe ser un numero\n");
            temperatura = validarTemperatura();

        return temperatura;
    
    def capturarLlanta(): #Registra la masa de aire en cada neumatico
        try:
            presion = float(input("Ingresa la presion:\n"));
            if presion < 0:
                print("La presion no puede ser menor que 0");
                presion = validarValor();
        except:
            print("La presion debe ser u  numero");
            presion = validarvalor();

        try:
            volumen = float(input("Ingresa su volumen:\n"));

            if volumen < 1:
                print("El columen debe ser positivo");
                volumen = validarPositivo();
        except:
            print("El volumen tiene que ser un numero");
            volumen = validarPositivo();

        try:
            temperatura = float(input("Ingresa su temperatura (en escala celsius):\n"));

            if temperatura < -273.14:
                print("La temperatura no puede estar por debajo del cero absoluto");
                temperatura = validarTemperatura();
            elif temperatura > 150:
                print("Los neumaticos no pueden mantenerse a esa temperatura");
                temperatura = validartemperatura();
        except:
            print("La temperatura debe ser un numero");
            temperatura = validarTemperatura();

        masa = (presion*volumen)/(.37*(temperatura + 460));

        return masa;

    def capturarVehiculo():#funcion principal del ejercicio, encargada de ejecutar las anteriores
        vehiculo = str(input("\nQue vehiculo vamos a calcular? (moto/auto)\n"));

        if (vehiculo != "moto") & (vehiculo != "auto"):
            print("\nLos registros solo pueden ser 'moto' o 'auto'");
            vehiculo = validarVehiculo();

        if vehiculo == "moto": #Se asigna el numero de veces que el ciclo correra
            repeticiones = 2;
        elif vehiculo == "auto":
            repeticiones = 4;

        promedio = 0; #Guarda la masa de todas las llantas

        for i in range(repeticiones): #cada ciclo registra el valor de una llanta y lo acumula
            print("\nVamos a registrar la llanta", i+1);
            promedio += capturarLlanta();

        promedio = promedio / (repeticiones); #Se divide entre el numero de llantas para tener el promedio

        print("\nEl promedio de masa de aire en los neumaticos de este vehiculo es: %.2f" % (promedio))

        continuar = str(input("\nQuieres capturar otro vehiculo? (si/no)\n"));

        if (continuar!= "si") & (continuar != "no"):
            print("\nLas respuestas solo pueden ser 'si' o 'no'");
            continuar = validarEleccion();

        if continuar == "si":
            capturarVehiculo();

    capturarVehiculo();

def e03(): #calcula el precio de kilo de huevo segun sea la calidad de las gallinas
    pass;

def e04(): #Calcula la postura de los diputados ante el TLC.
    pass;

def e05(): #realiza una sumas usando el sistema hexadecimal
    pass;

def e06(): #compara calificaciones de alumnos
    pass;

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

        if eleccion == 0:
            print("Que tengas un buen dia.")
        elif eleccion == 1:
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
