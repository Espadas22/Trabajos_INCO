#practica 08
#espadas rodriguez anthony jonathan
#mariscal cervantes diego maximiliano 

print("practica  08");
print("espadas rodriguez anthony jonathan");
print("mariscal cervantes diego maximiliano\n");

def e1(): #Calculo para el radio de una esfera
    radio = float(input("Dame el radio de una esfera\n"));
    while radio <= 0:
        print("El radio debe ser mayor que cero");
        radio = float(input("introduce un valor valido\n"));
    area = 4 * 3.1416 * radio;
    print("El area de una esfera de radio %.2f es: %.2f " % (radio, area));

def e2(): #Cacular volumen de una cantidad n de cubos
    arista = 1;
    contador = 1;

    while arista > 0:
        if contador == 1:
            arista = float(input("Dame la medida de la arista de un cubo\n"));
        else:
            arista = float(input("\nDame la medida de la arista de otro cubo\n(Para salir, presiona 0)\n"));

        while arista < 0:
            print("El valor debe ser positivo para calcular o 0 para salir");
            arista = float(input("Ingresa un valor valido\n"));
            
        contador += 1;
        volumen = arista**3;
        print("\nEl volumen del cubo", contador-1," con arista de %.2f es de: %.2f" % (arista, volumen));

def e3(): #Generador de tablas de multiplicar, desde 0 a n
    tabla = int(input("De cual numero quieres conocer la tabla?\n"));

    repeticiones = int(input("Hasta que valor quieres calcular?\n"));
    while repeticiones < 0:
        print("El numero de repeticiones debe ser mayor a cero");
        repeticiones = int(input("Ingresa un valor valido\n"));

    while repeticiones >= 0:
        resultado = tabla*repeticiones;
        print(tabla, "x", repeticiones, "=", resultado);
        repeticiones -= 1;

def e4(): #Inversor de signo de una cantidad n de numeros
    repeticiones = int(input("Cuantos numeros vamos a invertir?\n"));

    while repeticiones < 1:
        print("La cantidad de numeros debe ser al menos 1");
        repeticiones = int(input("Ingresa un valor valido\n"));
    
    contador = 0;
    conversion = "";

    while repeticiones > contador:
        numero = int(input("A que numero le vamos a cambiar el signo?\n"));
        contrario = str(numero*-1);
        conversion += contrario;
        conversion += ", "
        contador += 1;
    
    print("Los numeros invertidos son", conversion);


def e5(): #Promedia las calificaciones de un numero n de alumnos y menciona la mayor
    repeticiones = int(input("Cuantas calificaciones vamos a registrar\n"));
    contador = 0;
    suma = 0;
    calificacion_maxima = 0;

    while repeticiones < 1:
        print("Se debe registrar al menos una calificacion");
        repeticiones = int(input("Introduce un valor valido\n"));

    while repeticiones != contador:
        print("Dame la calificacion del alumno", contador+1);
        calificacion = float(input());

        while (calificacion > 100) | (calificacion < 0):
            print("Las calificaciones van de 0 a 100");
            calificacion = float(input("Introduce un valor valido\n"));

        if calificacion > calificacion_maxima:
            calificacion_maxima = calificacion;
            mejor_alumno = contador+1;

        suma += calificacion;
        contador += 1;

    promedio = suma/repeticiones;
    print("\nEl promedio fue", promedio);
    print("\nLa calificacion mas alta fue", calificacion_maxima,"del alumno", mejor_alumno);

def e6(): #Determina los colores de una cantidad n de autos
    repeticiones = int(input("Cuantos carros vamos a evaluar?\n"));

    while repeticiones < 1:
        print("El numero de carros debe ser al menos 1");
        repeticiones = int(input("Ingresa un valor valido\n"));

    contador = 1;
    amarillos = 0;
    rosas = 0;
    rojos = 0;
    verdes = 0;
    azules = 0;

    while contador <= repeticiones:
        print("Cual es el ultimo digito de las placas del carro", contador);
        digito = int(input());

        while (digito > 9) | (digito < 0):
            print("Los valores deben estar entre 0 y 9");
            digito = int(input("Ingresa un valor dentro del rango\n"));

        if (digito == 1) | (digito == 2):
            amarillos += 1;
        elif (digito == 3) | (digito == 4):
            rosas += 1;
        elif (digito == 5) | (digito == 6):
            rojos += 1;
        elif (digito == 7) | (digito == 8):
            verdes += 1;
        else:
            azules += 1;
            
        contador += 1;
        
    print("\nDe un total de", repeticiones, "autos");
    print(amarillos, "son amarillos");
    print(rosas, "son rosas");
    print(rojos, "son rojos");
    print(verdes, "son verdes");
    print(azules, "son azules");
    
            
def menu():
    eleccion = 11;
    while eleccion != 0:
        print("\nElije un ejercicio para ejecutar:");
        print("(1) Para calcular el radio de una esfera");
        print("(2) Para calcular el volumen de varios cubos");
        print("(3) Para calcular tablas de multiplicar");
        print("(4) Para invertir el signo de varias cifras");
        print("(5) Para calcular promedio de un grupode alumnos");
        print("(6) Para calcular el numero de autos de cada color");
        print("(0) Para salir\n");

        eleccion = int(input());

        while (eleccion < 0) | (eleccion > 6):
            print("El valor debe estar entre 0 y 6");
            eleccion = int(input("Ingresa un valor dentro del rango\n"));

        if eleccion == 1:
            e1();
        elif eleccion == 2:
            e2();
        elif eleccion == 3:
            e3();
        elif eleccion == 4:
            e4();
        elif eleccion == 5:
            e5();
        elif eleccion == 6:
            e6();

def imprimir():
    menu();

imprimir();
