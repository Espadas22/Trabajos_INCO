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
    def validarPeso(): #centra el peso de las gallinas en un rango definido
        try:
            peso = float(input("Introduce un valor dentro de rango\n"));

            if (peso < 1) | (altura > 2.3):
                print("Las gallinas entre 1 y 2.3 kg");
                peso = validarPeso();

        except:
            print("El peso debe ser un numero");
            peso = validarPeso();

        return peso;
            

    def validarAltura():#centra la altura de las gallianas en un rango definido
        try:
            altura = float(input("Introduce un valor dentro de rango\n"));

            if (altura < 25) | (altura > 40):
                print("Las gallinas miden entre 25 y 40 cm");
                altura = validarAltura();
        except:
            print("La altura debe ser un numero");
            altura = validarAltura();

        return altura;

    def validarHuevos():#centra el numero de huevos por semana en un rango definido
        try:
            huevos = int(input("Cuantos huevos pone a la semana?\n"));

            if (huevos < 0) | (huevos > 7):
                print("Las gallinas no pueden poner mas de un huevo al dia");
                huevos =ValidarHuevos();
        except:
            print("La cantidad de huevos debe ser un numero");
            huevos = validarHuevos();

        return huevos;

    try:
        gallinas = int(input("Cuantas gallinas vamos a evaluar?\n"));

        if gallinas < 1:
            print("Se debe avaluar por lo menos una gallina");
            gallinas = validarPositivo();

    except:
        print("La cantidad de gallinas debe ser un numero");
        gallinas = validarPositivo();

    promedio = 0;

    for i in range(gallinas):
        try:#Bloque try/except que captura la altura
            print("Dame la altura de la gallina", i+1, "en centimetros");
            altura = float(input());

            if (altura < 25) | (altura > 40):
                print("Las gallinas miden entre 25 y 40 cm");
                altura = validarAltura();
        except:
            print("La altura debe ser un numero");
            altura = validarAltura();

        try:#Bloque try/except que captura el peso
            print("Introduce el peso de la gallina", i+1,"en kg");
            peso = float(input());

            if (peso < 1) | (peso > 2.3):
                print("Las gallinas entre 1 y 2.3 kg");
                peso = validarPeso();

        except:
            print("El peso debe ser un numero");
            peso = validarPeso();

        try:#Bloque try/except que captura la cantidad de huevos que pone la gallina
            huevos = int(input("Cuantos huevos pone a la semana?\n"));

            if (huevos < 0) | (huevos > 7):
                print("Las gallinas no pueden poner mas de un huevo al dia");
                huevos =ValidarHuevos();
        except:
            print("La cantidad de huevos debe ser un numero");
            huevos = validarHuevos();

        calidad = peso*altura/huevos;

        print("La calidad de la gallina %.0f es %.2f" % (i+1, calidad));
                                                         
        promedio += calidad;

    promedio = promedio /gallinas;

    if promedio <= 8:
        precio = promedio*.8;
    elif promedio < 15:
        precio = promedio;
    elif promedio > 15:
        precio = promedio*1.2;

    print("El promedio de caliad de las gallinas es de %.2f, el precio por kilo podra darse en %2.f peso" % (promedio, calidad));
        

def e04(): #Calcula la postura de los diputados ante el TLC.
    def validarRespuesta():
        respuesta = str(input("Responda solo con 'si', 'no' o 'paso'\n"));

        if (respuesta != "si") & (respuesta != "no") & (respuesta != "paso"):
            respuesta = validarRespuesta();

        return respuesta;

    def capturarDiputado():#Funcion que captura la respuesta del diputado
        diputados_r = 1;
        favor_r = 0;#variables auxiliares que registran el cambio
        contra_r = 0;#cada que se llama a la funcion
        abstemios_r = 0;
        
        print("Esta a favor de El Tratado de Libre Comercio?");
        respuesta = str(input("Responder solo con 'si', 'no' o 'paso'\n"));

        if (respuesta != "si") & (respuesta != "no") & (respuesta != "paso"):
            respuesta = validarRespuesta();

        if respuesta == "si":
            favor_r += 1;
        elif respuesta == "no":
            contra_r += 1;
        elif respuesta == "paso":
            abstemios_r += 1;

        eleccion = str(input("Quieres registrar otra respuesta?\n"));

        if (eleccion != "si") & (eleccion != "no"):
            print("responde solo 'si o 'no'");
            eleccion = validarEleccion();

        if eleccion == "si":
            diputados_rr, favor_rr, contra_rr, abstemios_rr = capturarDiputado();
            diputados_r += diputados_rr;#Se almacena toda la recurrencia
            favor_r += favor_rr;#En las variables 'rr'
            contra_r += contra_rr;#Y se suma a las locales
            abstemios_r += abstemios_rr;#Para ser regresadas al final de la recurrencia.
            return diputados_r, favor_r, contra_r, abstemios_r;
        elif eleccion == "no":
            return diputados_r, favor_r, contra_r, abstemios_r;

    diputados, favor, contra, abstemios = capturarDiputado();#Estas variables reciben todos losa datos
    favor = favor*100/diputados;
    contra = contra*100/diputados;
    abstemios = abstemios*100/diputados;

    print("De los", diputados, "diputados:");
    if favor > 0:
        print("%2.f %% estan a favor del TLC" % (favor));
    if contra > 0:
        print("%2.f %% estan en contra del TLC" % (contra));
    if abstemios > 0:
        print("%2.f %% se abstuvieron de opinar" % (abstemios));
        

def e05(): #realiza una sumas usando el sistema hexadecimal
    pass;

def e06(): #compara calificaciones de alumnos
    alumnos = int(input("Agrega la cantidad de alumnos en el grupo\n"));
    promedio = 0;
    promedio_maximo = 0;
    str_maximo = "";
    str_alumnos = "";
    mejor_alunmo = 0;
    empate = 0;
    

    if alumnos < 1:
        print("Se debe registrar al menos una calificacion");
        alumnos = validarPositivo();

    for i in range(alumnos):
        promedio = 0;
        
        for j in range(3):
            print("Dame la calificacion", j+1, "del alumno", i+1);

            try:
                calificacion = float(input());

                if (calificacion < 0) | (calificacion > 100):
                    print("La calificacion debe estar entre 0 y 100");
                    calificacion = validarCalificacion();
            except:
                print("La calificacion debe ser un numero");
                calificacion = validarCalificacion();

            promedio += calificacion;

        promedio = promedio/3;

        print("\nEL promedio del alumno %.0f es %.2f" % (i+1, promedio));

        if promedio > promedio_maximo:
            empate = 0;
            promedio_maximo = promedio;
            mejor_alumno = i+1;
            str_maximo = "";
            str_alumnos = str(i+1) + ", ";
        elif promedio == promedio_maximo:
            empate = 1;
            str_maximo = str(promedio_maximo);
            str_alumnos += str(i+1) + ", ";

    if empate == 0:
        print("\nEl mayor promedio fue %.2f del alumno %.0f" % (promedio_maximo, mejor_alumno));
    elif empate == 1:
        print("\nEmpate!")
        print("El mayor promedio fue", str_maximo, "de los alumnos", str_alumnos);

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
