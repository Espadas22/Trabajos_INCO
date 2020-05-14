#espadas rodriguez anthony jonathan

def e1 (): #Simula la administracion de una fruteria
    import msvcrt;
    import os;
    from colorama import Back, Fore, init, Cursor;
    init(autoreset=True);
    
    #Parametros de letras para los titulos
    def parametros_A(eje_x, eje_y):
        if (eje_y == 0 and eje_x == 1) or (eje_y == 2) or (eje_y > 0 and eje_x % 2 == 0):
            return True;

    def parametros_B(eje_x, eje_y):
        if (eje_y % 2 == 0 and eje_x < 2) or (eje_y % 2 != 0 and (eje_x == 0 or eje_x == 2)):
            return True;

    def parametros_E(eje_x, eje_y):
        if (eje_y % 2 == 0) or (eje_y % 2 != 0 and eje_x == 0):
            return True;

    def parametros_F(eje_x, eje_y):
        if (eje_y == 0) or (eje_y == 2 and eje_x < 2) or (eje_x == 0):
            return True;

    def parametros_G(eje_x, eje_y):
        if (eje_y % 2 == 0) or (eje_y == 1 and eje_x % 2 == 0) or (eje_x == 2):
            return True;

    def parametros_I(eje_x, eje_y):
        if eje_y % 4 == 0 or eje_x == 1:
            return True;

    def parametros_J(eje_x, eje_y):
        if (eje_y % 4 == 0) or (eje_x == 2) or (eje_y == 3 and eje_x == 0):
            return True;
    
    def parametros_L(eje_x, eje_y):
        if eje_x == 0 or eje_y == 4:
            return True;

    def parametros_M(eje_x, eje_y):
        if eje_x % 2 == 0 or eje_y == 1:
            return True;

    def parametros_N(eje_x, eje_y):
        if eje_x % 2 == 0 or eje_y == 0:
            return True;

    def parametros_O(eje_x, eje_y):
        if (eje_y % 4 == 0 and eje_x == 1) or (eje_y % 4 != 0 and eje_x % 2 == 0):
            return True;

    def parametros_R(eje_x, eje_y):
        if (eje_y % 2 == 0 and eje_y < 3) or (eje_x == 0) or (eje_y == 1 and eje_x == 2) or (eje_y == 3 and eje_x == 1) or (eje_y == 4 and eje_x == 2):
            return True;

    def parametros_S(eje_x, eje_y):
        if (eje_y % 2 == 0) or (eje_y < 2 and eje_x == 0) or (eje_y > 2 and eje_x == 2):
            return True;

    def parametros_T(eje_x, eje_y):
        if eje_y == 0 or eje_x == 1:
            return True;

    def parametros_U(eje_x, eje_y):
        if eje_y == 4 or eje_x % 2 == 0:
            return True;

    def parametros_V(eje_x, eje_y):
        if (eje_y < 4 and eje_x % 2 == 0) or (eje_y == 4 and eje_x == 1):
            return True;
    
    #Diccionario que enlaza cada letra con sus parametros
    diccionario_letras = {"A": parametros_A, "B": parametros_B, "E": parametros_E, "F": parametros_F, "G": parametros_G, "I": parametros_I, "J": parametros_J, "L":parametros_L, "M": parametros_M, "N": parametros_N, "O": parametros_O, "R": parametros_R, "S": parametros_S, "T": parametros_T, "U": parametros_U, "V": parametros_V}

    def leerCaracter(): #Convierte la tecla ingresada en una instruccion para el programa
        primer_ingreso = ord(msvcrt.getch());
        #Detecta el codigo del caracter para determinar su instruccion
        if primer_ingreso == 49:
            return "uno";
        elif primer_ingreso == 50:
            return "dos";
        elif primer_ingreso == 51:
            return "tres";
        elif primer_ingreso == 52:
            return "cuatro";
        elif primer_ingreso == 13:
            return "enter";
        elif primer_ingreso == 27:
            return "escape";
        elif primer_ingreso == 224:#Detecta si se ingreso un caracter especial
            segundo_ingreso = ord(msvcrt.getch());
            #Y le asigna su accion
            if segundo_ingreso == 72:
                return "arriba";
            elif segundo_ingreso == 80:
                return "abajo";
            else:
                return "nada";
        else:
            return "nada"; #Se regresa el 'nada' para que el ciclo while tenga un resultado a comprar y evitar errores

    def escribirLetra(inicio_x, inicio_y, letra): #Usa los parametros para validar posiciones y escribir las letras del titulo
        for eje_y in range(0, 5):
            for eje_x in range(0, 3):
                if letra(eje_x, eje_y):
                    print(Cursor.POS(inicio_x + eje_x, inicio_y + eje_y) + Back.WHITE + " ");

    def impimirFondo(): #Dibuja el fondo verde de la aplicacion
        print('\x1b[2J', end = "");
        for renglon in range(2, 30):
            for columna in range(10, 112):
                print(Cursor.POS(columna, renglon) + Back.GREEN + " ");

    def fondoAmarillo(inicio, final): #Dibuja los fondos amarillos donde se muestra la informaicon al usuario
        for renglon in range(inicio, final):
            for columna in range(121):
                if (renglon > inicio and renglon < final) and (columna > 12 and columna < 108):
                    print(Cursor.POS(columna, renglon) + Back.YELLOW + " ");

    def escribirTitulo(inicio_x, inicio_y, mensaje): #Escribe los titulos de cada seccion
        cursor_x = inicio_x;
        cursor_y = inicio_y;
        while(True):
            for letra in mensaje:
                try:
                    escribirLetra(cursor_x, cursor_y, diccionario_letras[letra]);
                except:
                    cursor_x += 4;    
                else:
                    cursor_x += 4;
            break;

    def informacionMenu(seleccion): #Muestra las opciones de la pantalla de menu
        if (seleccion % 4) == 1: #Si una opcion es seleccionada la pinta en rojo
            print(Cursor.POS(50, 12) + Back.RED + "(1)  Ventas");
        else: #De no estarlo se pinta en amarillo
            print(Cursor.POS(50, 12) + Back.YELLOW + "(1)  Ventas");
        if (seleccion % 4) == 2:
            print(Cursor.POS(50, 16) + Back.RED + "(2)  Altas");
        else:
            print(Cursor.POS(50, 16) + Back.YELLOW + "(2)  Altas");
        if (seleccion % 4) == 3:
            print(Cursor.POS(50, 20) + Back.RED + "(3)  Bajas");
        else:
            print(Cursor.POS(50, 20) + Back.YELLOW + "(3)  Bajas");
        if (seleccion % 4) == 0:
            print(Cursor.POS(50, 24) + Back.RED + "(4)  Salir");
        else:
            print(Cursor.POS(50, 24) + Back.YELLOW + "(4)  Salir");

    def informacionAltasBajas(seleccion): #Muestra las opciones de la pantalla 'altas' y 'bajas'
        if (seleccion % 3) == 1: #Si una opcion esta seleccionada la pinta de rojo
            print(Cursor.POS(50, 12) + Back.RED + "(1) Datos de la fruteria");
        else: #De no estarlo se pinta en amarillo
            print(Cursor.POS(50, 12) + Back.YELLOW + "(1) Datos de la fruteria");
        if (seleccion % 3) == 2:
            print(Cursor.POS(50, 16) + Back.RED + "(2) Producto");
        else:
            print(Cursor.POS(50, 16) + Back.YELLOW + "(2) Producto");
        if (seleccion % 3) == 0:
            print(Cursor.POS(50, 20) + Back.RED + "(3) Empleados");
        else:
            print(Cursor.POS(50, 20) + Back.YELLOW + "(3) Empleados");

        print(Cursor.POS(40, 24) + Back.YELLOW + "Presiona 'Esc' para volver al menu anterior")

    def informacionVentas(seleccion): #Muestra las opciones para la pantallas de 'ventas'
        pass;

    def pantallaTitulo(): #Dibuja la pantalla de bienvenida al programa
        impimirFondo();
        fondoAmarillo(9, 15);

        mensaje = "FRUTERIA SIMULATOR";

        escribirTitulo(25, 10, mensaje);

        print(Cursor.POS(40, 18) + Back.YELLOW + "[Presiona cualquier tecla para comenzar]")

        input();

    def dibujarPantalla(titulo_de_pantalla): #Genera los recuadros amarillos y escribe el titulo para las pantallas de informacion
        impimirFondo();
        fondoAmarillo(2, 8);
        fondoAmarillo(9, 29);

        escribirTitulo(50, 3, titulo_de_pantalla);

    def implementarPantalla(pantalla_a_implementar, informacion_a_mostrar): #Se encarga de controlar los datos que se presentan en cada una de las pantalas
        seleccion = 19; #Variable que ayuda a controlar la seleccion dentro de las opciones
        dibujarPantalla(pantalla_a_implementar);
        while (True):
            if informacion_a_mostrar == "uno":
                informacionVentas(seleccion);
            else:
                informacionAltasBajas(seleccion);
            
            accion = leerCaracter();

            if accion == "arriba":
                seleccion -= 1;
            elif accion == "abajo":
                seleccion += 1;
            elif accion == "escape":
                break;

    pantallaTitulo();
    seleccion = 21; #Variable que sirve como control para la eleccion dentro de los menus
    
    while(True): #Ciclo principal, desde el que se implementan los demas
        dibujarPantalla("MENU");
        informacionMenu(seleccion);

        accion = leerCaracter(); 

        if accion == "arriba":
            seleccion -= 1;
        elif accion == "abajo":
            seleccion += 1;
        elif (accion == "enter" and (seleccion % 4 == 1)) or accion == "uno":
            accion = "uno";
            implementarPantalla("VENTAS", accion);
        elif (accion == "enter" and (seleccion % 4 == 2)) or accion == "dos":
            accion = "dos";
            implementarPantalla("ALTAS", accion);
        elif (accion == "enter" and (seleccion % 4 == 3)) or accion == "tres":
            accion = "tres";
            implementarPantalla("BAJAS", accion);
        elif (accion == "enter" and (seleccion % 4 == 0)) or accion == "cuatro":
            print('\x1b[2J', end = "");
            break;
        

def imprimir():
    e1();

imprimir();