#practica 11
#espadas rodriguez anthony jonathan
#mariscal cervantes diego maximiliano

def e1(): #Programa que recorre una frase resaltando la letra seleccionada
    from colorama import init, Fore, Cursor, Back;
    from msvcrt import getch;
    init(autoreset=True); 
    
    #Guardan la posicion del puntero
    puntero_x = 1;
    puntero_y = 5;

    def imprimirDatos():
        print(Cursor.POS(1,1) + Fore.WHITE + "practica 11");
        print(Cursor.POS(1,2) + Fore.WHITE + "espadas rodriguez anthony jonathan");
        print(Cursor.POS(1,3) + Fore.WHITE + "mariscal cervantes diego maximiliano\n");
    
    #Se encarga de dibujar los simbolos
    def gato(posicion_x, posicion_y, colorear):
        if colorear == True: #valida que la letra sea la seleccionada
            print(Cursor.POS(posicion_x, posicion_y) + Back.GREEN + Fore.GREEN + "#");
        else:    
            print(Cursor.POS(posicion_x, posicion_y) + "#");

    #Determinamos los parametros para imprimir cada una de las letras
    def parametros_A(eje_x, eje_y):
        if (eje_y == 0 and eje_x == 1) or (eje_y == 2) or (eje_y > 0 and eje_x % 2 == 0):
            return True;
    
    def parametros_B(eje_x, eje_y):
        if (eje_y % 2 == 0 and eje_x < 2) or (eje_y % 2 != 0 and (eje_x == 0 or eje_x == 2)):
            return True;
    
    def parametros_C(eje_x, eje_y):
        if (eje_y % 4 == 0 and eje_x > 0) or (eje_y % 4 != 0 and eje_x == 0):
            return True;

    def parametros_D(eje_x, eje_y):
        if (eje_x == 0) or (eje_y % 4 == 0 and eje_x == 1) or (eje_y % 4 != 0 and eje_x == 2):
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

    def parametros_H(eje_x, eje_y):
        if eje_x % 2 == 0 or eje_y == 2:
            return True;

    def parametros_I(eje_x, eje_y):
        if eje_y % 4 == 0 or eje_x == 1:
            return True;

    def parametros_J(eje_x, eje_y):
        if (eje_y % 4 == 0) or (eje_x == 2) or (eje_y == 3 and eje_x == 0):
            return True;

    def parametros_K(eje_x, eje_y):
        if (eje_y % 4 == 0 and eje_x % 2 == 0) or (eje_y % 2 != 0 and eje_x == 1) or (eje_x == 0):
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

    def parametros_Ñ(eje_x, eje_y):
        if (eje_y == 0 or eje_y == 2) or (eje_x % 2 == 0 and eje_y > 2):
            return True;

    def parametros_O(eje_x, eje_y):
        if (eje_y % 4 == 0 and eje_x == 1) or (eje_y % 4 != 0 and eje_x % 2 == 0):
            return True;

    def parametros_P(eje_x, eje_y):
        if (eje_y % 2 == 0 and eje_y < 3) or (eje_y < 3 and eje_x % 2 == 0) or (eje_x == 0):
            return True;

    def parametros_Q(eje_x, eje_y):
        if (eje_y % 2 == 0 and eje_y < 3) or (eje_y < 3 and eje_x % 2 == 0) or (eje_x == 2):
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

    def parametros_W(eje_x, eje_y):
        if eje_y == 3 or eje_x % 2 == 0:
            return True;

    def parametros_X(eje_x, eje_y):
        if (eje_y != 2 and eje_x % 2 == 0) or (eje_y == 2 and eje_x == 1):
            return True;

    def parametros_Y(eje_x, eje_y):
        if (eje_y < 2 and eje_x % 2 == 0) or (eje_y > 1 and eje_x == 1):
            return True;

    def parametros_Z(eje_x, eje_y):
        if (eje_y % 4 == 0) or (eje_y == 1 and eje_x == 2) or (eje_y == 2 and eje_x == 1) or (eje_y == 3 and eje_x == 0):
             return True;

    def dibujar(inicio_x, inicio_y, letra, colorear):
        for eje_y in range(0, 5):
            for eje_x in range(0, 3):
                if letra(eje_x, eje_y):
                    gato(inicio_x + eje_x, inicio_y + eje_y, colorear)

    #Ligamos cada letra a sus parametros
    letras = {"A": parametros_A, "B": parametros_B, "C": parametros_C, "D": parametros_D, "E": parametros_E, "F": parametros_F, "G": parametros_G, "H": parametros_H, "I": parametros_I, "J": parametros_J, "K": parametros_K, "L": parametros_L, "M": parametros_M, "N": parametros_N, "Ñ": parametros_Ñ, "O": parametros_O, "P": parametros_P, "Q": parametros_Q, "R": parametros_R, "S": parametros_S, "T": parametros_T, "U": parametros_U, "V": parametros_V, "W": parametros_W, "X": parametros_X, "Y": parametros_Y, "Z": parametros_Z};
    
    imprimirDatos();
    print(Cursor.POS(puntero_x, puntero_y) + "Introduce una frase:");
    mensaje = (str(input()));  #Se hace es casteo de tipo
    mensaje = mensaje.upper(); #Cambiamos a mayusculas para comprar en el diccionario
    mensaje = tuple(mensaje); #Se vuelve una tupla para conservar el orden en las iteraciones
    seleccionada = 1; #Primera letra en aparecer seleccionada
    contador = 0; #Lleva registro de las letras iteradas

    print('\x1b[2J', end = "");
    imprimirDatos();

    for i in mensaje:
        colorear = False; #variable que indica cuando una letra debe ser resaltada 
        contador += 1;

        try:
            if seleccionada == contador:
                colorear = True; #Si la letra seleccionada coincide con el contador, entonces se resalta

            dibujar(puntero_x, puntero_y, letras[i], colorear); #Se compara la posicion en i de la tupla con el diccionario

        except:
            puntero_x += 4; #De no encontrarse en el diccionario se deja el espacio vacio
            contador -= 1; #Mueve el contador para que no se seleccionen los espacios
        
        else:
            puntero_x += 4; #Se mueve el puntero para comenzar el dibujado de la siguiente letra
        
        if puntero_x > 120: #Cuando se alcance el borde de la pantalla
            puntero_x = 1; #Se regresa el puntero X al inicio de la consola
            puntero_y +=7; #Y nos desplazamos un renglon abajo

def imprimir():
    e1(); 
    input();

imprimir(); 
