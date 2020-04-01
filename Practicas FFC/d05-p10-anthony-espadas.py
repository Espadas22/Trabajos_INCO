#practica 10
#espadas rodriguez anthony jonathan
#mariscal cervantes diego maximiliano

def e1():
    def imprimirDatos():
        from colorama import init, Fore;
        init();
        print(Fore.MAGENTA + "practica 10");
        print("espadas rodriguez anthony jonathan");
        print("mariscal cervantes diego maximiliano\n" + Fore.RESET);
        print(Fore.CYAN + "Selecciona: ", end="");
        print("\b (1)Triangulo ", end=""); 
        print("\b (2)Cuadrado ", end=""); 
        print("\b (3)Circulo ", end=""); 
        print("\b (0)Salir ", end="" + Fore.RESET);
        print("\b ||", end=" ");
        print(Fore.CYAN + "Usa las flechas para mover la figura seleccionada\n" + Fore.RESET); 
    
    def dibujarArea(): #Dibuja el cuadrado que delimita las figuras
        from colorama import init, Fore, Style, Cursor;
        init(autoreset=True); 
        
        for i in range(7, 30):
            for j in range(120):
                if i == 7 or i == 29 or j == 0 or j == 119: #Valida estar en la primer o ultima linea
                    print(Fore.WHITE + Style.BRIGHT + Cursor.POS(j,i) + "*");
                    
    #Funciones que se encargan de dibujar el asterisco del color corresponiente
    def asteriscoVerde(i, j): 
        from colorama import init, Fore, Style, Cursor;
        init(autoreset=True); 
             
        print(Fore.GREEN + Style.BRIGHT + Cursor.POS(j, i) + "*"); 

    def asteriscoRojo(i, j): 
        from colorama import init, Fore, Style, Cursor;
        init(autoreset=True); 
             
        print(Fore.RED + Style.BRIGHT + Cursor.POS(j, i) + "*");   

    def asteriscoAmarillo(i, j): 
        from colorama import init, Fore, Style, Cursor;
        init(autoreset=True); 
             
        print(Fore.YELLOW + Style.BRIGHT + Cursor.POS(j, i) + "*"); 

    def moverTriangulo(x, y, c): #Se encarga de dibujar al triangulo en consola
        distancia = 0; #Genera la separacion entre los bordes

        for i in range(y, y + 11):#Genera una altura de 10 lineas
            for j in range(x - distancia, x + distancia): #Abre distancia de los lados segun se acerca a la base
                if i == y or i == y + 10: #Valida estar en la primer o ultima linea 
                    if c == 1:
                        asteriscoVerde(i, j); 
                    elif c == 2:
                        asteriscoAmarillo(i, j); 
                    elif c == 3:
                        asteriscoRojo(i, j); 
                elif j == x - distancia or j == x + distancia -1: #Valida estar en los extremos
                    if c == 1:
                        asteriscoVerde(i, j); 
                    elif c == 2:
                        asteriscoAmarillo(i, j); 
                    elif c == 3:
                        asteriscoRojo(i, j); 
            
            distancia += 1; 

    def moverCuadrado(x, y, c): #Se encarga de dibujar al cuadrado en consola
        for i in range(y, y + 11): #Genera lado de 10 lineas
            for j in range(x, x + 21): #Genera lado de 20 columnas
                if i == y or i == y + 10: #Revisa que nos encontremos en los bordes
                    if c == 1:
                        asteriscoVerde(i, j); 
                    elif c == 2:
                        asteriscoAmarillo(i, j); 
                    elif c == 3:
                        asteriscoRojo(i, j); 
                elif j == x or j == x + 20: #E imprime el asterisco
                    if c == 1:
                        asteriscoVerde(i, j); 
                    elif c == 2:
                        asteriscoAmarillo(i, j); 
                    elif c == 3:
                        asteriscoRojo(i, j); 

    def moverCirculo(x, y, c):
        for i in range(y, y + 11):
            for j in range(x, x + 21):
                if (i == y or i == y + 10) and (j > x + 2 and j < x + 17): #Verificamos estar en borde horizontal
                    if c == 1:
                        asteriscoVerde(i, j); 
                    elif c == 2:
                        asteriscoAmarillo(i, j); 
                    elif c == 3:
                        asteriscoRojo(i, j); 
                elif (j == x or j == x + 19) and (i > y + 1 and i < y + 9): #Verifcamos estar en un borde vertical
                    if c == 1:
                        asteriscoVerde(i, j); 
                    elif c == 2:
                        asteriscoAmarillo(i, j); 
                    elif c == 3:
                        asteriscoRojo(i, j); 
                elif (j == x + 1 and i == y + 1) or (j == x + 1 and i == y + 9) or (j == x + 18 and i == y + 1) or (j == x + 18 and i == y + 9): #Verificamos estar en una esquina
                    if c == 1:
                        asteriscoVerde(i, j); 
                    elif c == 2:
                        asteriscoAmarillo(i, j); 
                    elif c == 3:
                        asteriscoRojo(i, j); 


    imprimirDatos(); #Imprime los datos de referencia al usuario
    
    #Posiciones en X y Y de las figuras
    triangulo_x = 59; 
    triangulo_y = 12; 
    
    cuadrado_x = 10; 
    cuadrado_y = 12; 

    circulo_x = 85; 
    circulo_y = 12; 

    dibujarArea(); #Dibujamos el area del programa
    
    #Mostramos las figuras en su posicion y color por defecto
    moverTriangulo(triangulo_x, triangulo_y, 1); 
    moverCuadrado(cuadrado_x, cuadrado_y, 2); 
    moverCirculo(circulo_x, circulo_y, 3); 

    input(); 

def imprimir():
    e1(); 

imprimir(); 
