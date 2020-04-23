#practica 11
#espadas rodriguez anthony jonathan
#mariscal cervantes diego maximiliano


#Limpia pantallas print('\x1b[2J', end = "");

def e1():
    from colorama import init, Fore, Style, Cursor;
    init(autoreset=True); 
    
    #Guardan la posicion del puntero
    puntero_x = 1;
    puntero_y = 5;

    def imprimirDatos():
        print(Cursor.POS(1,1) + Fore.WHITE + "practica 11");
        print(Cursor.POS(1,2) + Fore.WHITE + "espadas rodriguez anthony jonathan");
        print(Cursor.POS(1,3) + Fore.WHITE + "mariscal cervantes diego maximiliano\n");
    
    def asterisco(posicion_x, posicion_y):
        print(Cursor.POS(posicion_x, posicion_y) + "*");

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
        if (eje_x % 2 == 0 and eje_y > 0) or eje_y == 1:
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

    def dibujar(inicio_x, inicio_y, letra):
        for eje_y in range(0, 5):
            for eje_x in range(0, 3):
                if letra(eje_x, eje_y):
                    asterisco(inicio_x + eje_x, inicio_y + eje_y)
    
    imprimirDatos();
    dibujar(puntero_x, puntero_y, parametros_A);

def imprimir():
    e1(); 
    input();

imprimir(); 
