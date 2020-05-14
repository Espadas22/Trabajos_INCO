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
    
    #Diccionario que enlaza cada letra con sus parametros
    diccionario_letras = {"A": parametros_A, "B": parametros_B, "E": parametros_E, "F": parametros_F, "G": parametros_G, "I": parametros_I, "J": parametros_J, "L":parametros_L, "M": parametros_M, "N": parametros_N, "O": parametros_O, "R": parametros_R, "S": parametros_S, "T": parametros_T, "U": parametros_U}

    def colorearEspacio(posicion_x, posicion_y): #Da color a los espacios del titulo
        print(Cursor.POS(posicion_x, posicion_y) + Back.WHITE + " ");

    def escribirLetra(inicio_x, inicio_y, letra): #Se encarga de validar posiciones de las letras en el titulo
        for eje_y in range(0, 5):
            for eje_x in range(0, 3):
                if letra(eje_x, eje_y):
                    colorearEspacio(inicio_x + eje_x, inicio_y + eje_y)

    def impimirFondo(): #Dibuja el fondo de la aplicacion
        print('\x1b[2J', end = "");
        for renglon in range(2, 30):
            for columna in range(10, 112):
                print(Cursor.POS(columna, renglon) + Back.GREEN + " ");

    def fondoAmarillo(inicio, final): #Dibuja los fondos amarillos para mostrar informaicon al usuario
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

    def pantallaTitulo(): #Dibuja la pantalla de bienvenida al programa
        impimirFondo();
        fondoAmarillo(9, 15);

        mensaje = "FRUTERIA SIMULATOR";

        escribirTitulo(25, 10, mensaje);

        print(Cursor.POS(40, 18) + Back.YELLOW + "[Presiona cualquier tecla para comenzar]")

        input();

    def dibujarPantalla(nombre): #Genera los recuadros amarillos y escribe el titulo para las pantallas de informacion
        impimirFondo();
        fondoAmarillo(2, 8);
        fondoAmarillo(9, 29);

        escribirTitulo(50, 3, nombre);

    def informacionMenu(seleccion): #Muestra las opciones de la pantalla de menu
        if (seleccion % 4) == 1: 
            print(Cursor.POS(50, 12) + Back.RED + "(1)  Venta");
        else:
            print(Cursor.POS(50, 12) + Back.YELLOW + "(1)  Venta");
        if (seleccion % 4) == 2:
            print(Cursor.POS(50, 16) + Back.RED + "(2)  Alta");
        else:
            print(Cursor.POS(50, 16) + Back.YELLOW + "(2)  Alta");
        if (seleccion % 4) == 3:
            print(Cursor.POS(50, 20) + Back.RED + "(3)  Baja");
        else:
            print(Cursor.POS(50, 20) + Back.YELLOW + "(3)  Baja");
        if (seleccion % 4) == 0:
            print(Cursor.POS(50, 24) + Back.RED + "(4)  Salir");
        else:
            print(Cursor.POS(50, 24) + Back.YELLOW + "(4)  Salir");    

    def leerCaracter(): #Convierte la tecla ingresada en una instruccion para el programa
        primer_ingreso = ord(msvcrt.getch());

        if primer_ingreso == 49:
            return "uno";
        elif primer_ingreso == 50:
            return "dos";
        elif primer_ingreso == 51:
            return "tres";
        elif primer_ingreso == 52:
            return "cuatro";
        elif primer_ingreso == 27:
            return "enter";
        elif primer_ingreso == 13:
            return "escape";
        elif primer_ingreso == 224:
            segundo_ingreso = ord(msvcrt.getch());

            if segundo_ingreso == 72:
                return "arriba";
            elif segundo_ingreso == 80:
                return "abajo";
            elif segundo_ingreso == 75:
                return "izquierda";
            elif segundo_ingreso == 77:
                return "derecha"
            else:
                return "nada";
        else:
            return "nada";

    pantallaTitulo();
    seleccion = 21;
    
    while(True):
        dibujarPantalla("MENU");
        informacionMenu(seleccion);

        accion = leerCaracter(); 

        if accion == "arriba":
            seleccion -= 1;
        elif accion == "abajo":
            seleccion += 1;

def imprimir():
    e1();
    input();

imprimir();