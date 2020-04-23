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

    def dibujar_A(inicio_x, inicio_y):
        for eje_y in range(0, 5):
            for eje_x in range(0, 3):
                if eje_y == 0 and eje_x == 1:
                    asterisco(inicio_x + eje_x, inicio_y + eje_y);
                elif eje_y == 2:
                    asterisco(inicio_x + eje_x, inicio_y + eje_y);
                elif eje_y > 0 and (eje_x == 0 or eje_x == 2):
                    asterisco(inicio_x + eje_x, inicio_y + eje_y);
    
    def dibujar_B(inicio_x, inicio_y):
        for eje_y in range(0, 5):
            for eje_x in range(0, 3):
                if (eje_y % 2 == 0) and (eje_x < 2):
                    asterisco(inicio_x + eje_x, inicio_y + eje_y);
                elif (eje_y % 2 != 0) and (eje_x == 0 or eje_x == 2):
                    asterisco(inicio_x + eje_x, inicio_y + eje_y);
    
    def dibujar_C(inicio_x, inicio_y):
        for eje_y in range(0, 5):
            for eje_x in range(0, 3):
                if (eje_y == 0 or eje_y == 4) and (eje_x > 0):
                    asterisco(inicio_x + eje_x, inicio_y + eje_y);
                elif (eje_y > 0 and eje_y < 4) and (eje_x == 0):
                    asterisco(inicio_x + eje_x, inicio_y + eje_y);

    def dibujar_D(inicio_x, inicio_y):
        for eje_y in range(0, 5):
            for eje_x in range(0, 3):
                if (eje_y == 0 or eje_y == 4) and (eje_x < 2):
                    asterisco(inicio_x + eje_x, inicio_y + eje_y);
                elif (eje_y > 0 and eje_y < 4) and (eje_x == 0 or eje_x == 2):
                    asterisco(inicio_x + eje_x, inicio_y + eje_y);

    def dibujar_E(inicio_x, inicio_y):
        for eje_y in range(0, 5):
            for eje_x in range(0, 3):
                if (eje_y % 2 == 0):
                    asterisco(inicio_x + eje_x, inicio_y + eje_y);
                elif (eje_y % 2 != 0) and (eje_x == 0):
                    asterisco(inicio_x + eje_x, inicio_y + eje_y);

    def dibujar_F(inicio_x, inicio_y):
        for eje_y in range(0, 5):
            for eje_x in range(0, 3):
                if eje_y == 0:
                    asterisco(inicio_x + eje_x, inicio_y + eje_y);
                elif eje_y == 2 and eje_x < 2:
                    asterisco(inicio_x + eje_x, inicio_y + eje_y);
                elif eje_x == 0:
                    asterisco(inicio_x + eje_x, inicio_y + eje_y);
    
    def dibujar_G(inicio_x, inicio_y):
        for eje_y in range(0, 5):
            for eje_x in range(0, 3):
                if eje_y % 2 == 0:
                    asterisco(inicio_x + eje_x, inicio_y + eje_y);
                elif eje_y == 1 and eje_x % 2 == 0 :
                    asterisco(inicio_x + eje_x, inicio_y + eje_y);
                elif eje_x == 2:
                    asterisco(inicio_x + eje_x, inicio_y + eje_y);

    def dibujar_H(inicio_x, inicio_y):
        for eje_y in range(0, 5):
            for eje_x in range(0, 3):
                if eje_x % 2 == 0:
                    asterisco(inicio_x + eje_x, inicio_y + eje_y);
                elif eje_y == 2:
                    asterisco(inicio_x + eje_x, inicio_y + eje_y);

    def dibujar_I(inicio_x, inicio_y):
        for eje_y in range(0, 5):
            for eje_x in range(0, 3):
                if eje_y % 4 == 0:
                    asterisco(inicio_x + eje_x, inicio_y + eje_y);
                elif eje_x == 1:
                    asterisco(inicio_x + eje_x, inicio_y + eje_y);

    def dibujar_J(inicio_x, inicio_y):
        for eje_y in range(0, 5):
            for eje_x in range(0, 3):
                if eje_y % 4 == 0:
                    asterisco(inicio_x + eje_x, inicio_y + eje_y);
                elif eje_x == 2:
                    asterisco(inicio_x + eje_x, inicio_y + eje_y);
                elif eje_y == 3 and eje_x == 0:
                    asterisco(inicio_x + eje_x, inicio_y + eje_y);

    def dibujar_K(inicio_x, inicio_y):
        for eje_y in range(0, 5):
            for eje_x in range(0, 3):
                if eje_y % 4 == 0 and eje_x % 2 == 0:
                    asterisco(inicio_x + eje_x, inicio_y + eje_y);
                elif eje_y % 2 != 0 and eje_x == 1:
                    asterisco(inicio_x + eje_x, inicio_y + eje_y);
                elif eje_x == 0:
                    asterisco(inicio_x + eje_x, inicio_y + eje_y);
    
    def dibujar_L(inicio_x, inicio_y):
        for eje_y in range(0, 5):
            for eje_x in range(0, 3):
                if eje_x == 0 or eje_y == 4:
                    asterisco(inicio_x + eje_x, inicio_y + eje_y);

    def dibujar_M(inicio_x, inicio_y):
        for eje_y in range(0, 5):
            for eje_x in range(0, 3):
                if eje_x % 2 == 0 or eje_y == 1:
                    asterisco(inicio_x + eje_x, inicio_y + eje_y);

    def dibujar_N(inicio_x, inicio_y):
        for eje_y in range(0, 5):
            for eje_x in range(0, 3):
                if (eje_x % 2 == 0 and eje_y > 0) or eje_y == 1:
                    asterisco(inicio_x + eje_x, inicio_y + eje_y);

    def dibujar_O(inicio_x, inicio_y):
        for eje_y in range(0, 5):
            for eje_x in range(0, 3):
                if (eje_y % 4 == 0 and eje_x == 1) or (eje_y % 4 != 0 and eje_x % 2 == 0):
                    asterisco(inicio_x + eje_x, inicio_y + eje_y);

    def dibujar_P(inicio_x, inicio_y):
        for eje_y in range(0, 5):
            for eje_x in range(0, 3):
                if (eje_y % 2 == 0 and eje_y < 3) or (eje_y < 3 and eje_x % 2 == 0) or (eje_x == 0):
                    asterisco(inicio_x + eje_x, inicio_y + eje_y);

    def dibujar_Q(inicio_x, inicio_y):
        for eje_y in range(0, 5):
            for eje_x in range(0, 3):
                if (eje_y % 2 == 0 and eje_y < 3) or (eje_y < 3 and eje_x % 2 == 0) or (eje_x == 2):
                    asterisco(inicio_x + eje_x, inicio_y + eje_y);

    def dibujar_R(inicio_x, inicio_y):
        for eje_y in range(0, 5):
            for eje_x in range(0, 3):
                if (eje_y % 2 == 0 and eje_y < 3) or (eje_x == 0) or (eje_y == 1 and eje_x == 2):
                    asterisco(inicio_x + eje_x, inicio_y + eje_y);
                elif eje_y == 3 and eje_x == 1:
                    asterisco(inicio_x + eje_x, inicio_y + eje_y);
                elif eje_y == 4 and eje_x == 2:
                    asterisco(inicio_x + eje_x, inicio_y + eje_y);

    def dibujar_S(inicio_x, inicio_y):
        for eje_y in range(0, 5):
            for eje_x in range(0, 3):
                if (eje_y % 2 == 0) or (eje_y < 2 and eje_x == 0) or (eje_y > 2 and eje_x == 2):
                    asterisco(inicio_x + eje_x, inicio_y + eje_y);

    def dibujar_T(inicio_x, inicio_y):
        for eje_y in range(0, 5):
            for eje_x in range(0, 3):
                if eje_y == 0 or eje_x == 1:
                    asterisco(inicio_x + eje_x, inicio_y + eje_y);

    def dibujar_U(inicio_x, inicio_y):
        for eje_y in range(0, 5):
            for eje_x in range(0, 3):
                if eje_y == 4 or eje_x % 2 == 0:
                    asterisco(inicio_x + eje_x, inicio_y + eje_y);

    def dibujar_V(inicio_x, inicio_y):
        for eje_y in range(0, 5):
            for eje_x in range(0, 3):
                if (eje_y < 4 and eje_x % 2 == 0) or (eje_y == 4 and eje_x == 1):
                    asterisco(inicio_x + eje_x, inicio_y + eje_y);

    def dibujar_W(inicio_x, inicio_y):
        for eje_y in range(0, 5):
            for eje_x in range(0, 3):
                if eje_y == 3 or eje_x % 2 == 0:
                    asterisco(inicio_x + eje_x, inicio_y + eje_y);

    def dibujar_X(inicio_x, inicio_y):
        for eje_y in range(0, 5):
            for eje_x in range(0, 3):
                if (eje_y != 2 and eje_x % 2 == 0) or (eje_y == 2 and eje_x == 1):
                    asterisco(inicio_x + eje_x, inicio_y + eje_y);

    def dibujar_Y(inicio_x, inicio_y):
        for eje_y in range(0, 5):
            for eje_x in range(0, 3):
                if (eje_y < 2 and eje_x % 2 == 0) or (eje_y > 1 and eje_x == 1):
                    asterisco(inicio_x + eje_x, inicio_y + eje_y);

    def dibujar_Z(inicio_x, inicio_y):
        for eje_y in range(0, 5):
            for eje_x in range(0, 3):
                if (eje_y % 4 == 0) or (eje_y == 1 and eje_x == 2) or (eje_y == 2 and eje_x == 1) or (eje_y == 3 and eje_x == 0):
                    asterisco(inicio_x + eje_x, inicio_y + eje_y);

    imprimirDatos();
    dibujar_Z(puntero_x, puntero_y);

def imprimir():
    e1(); 
    input();

imprimir(); 
