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
        print(Fore.CYAN + "Usa las flechas para mover la figura seleccionada" + Fore.RESET); 
    
    def dibujarArea(): #Dibuja el cuadrado que delimita las figuras
        from colorama import init, Style, Cursor;
        init(autoreset=True); 
        
        for i in range(7, 30):
            for j in range(120):
            
                if i == 7 or i == 29: #Valida estar en la primer o ultima linea
                    print(Style.BRIGHT + Cursor.POS(j,i) + "*", end=""); 
                elif j == 1 or j == 119: #Valida estar en los extremos
                     print(Style.BRIGHT + Cursor.POS(j,i) + "*", end=""); 

    def moverTriangulo(x, y, c): #Se encarga de dibujar al triangulo en consola
        from colorama import init, Fore, Cursor;
        init(); 
        
        distancia = 0; #Genera la separacion entre los bordes

        for i in range(x, x + 11):#Genera una altura de 10 lineas
            for j in range(y - distancia, y + distancia): #Abre distancia de los lados segun se acerca a la base
                if i == x or i == x + 10: #Valida estar en la primer o ultima linea
                    print(Cursor.POS(j, i) + "*", end=""); 
                elif j == y - distancia or j == y + distancia -1: #Valida estar en los extremos
                    print(Cursor.POS(j, i) + "*", end=""); 
            
            distancia += 1; 

    def moverCuadrado(x, y, c): #Se encarga de dibujar al cuadrado en consola
        from colorama import init, Fore, Cursor;
        init(); 

        for i in range(x, x + 11): #Genera lado de 10 lineas
            for j in range(y, y + 21): #Genera lado de 20 columnas
                if i == x or i == x + 10: #Revisa que nos encontremos en los bordes
                    print(Cursor.POS(j, i) + "*", end=""); 
                elif j == y or j == y + 20: #E imprime el asterisco
                    print(Cursor.POS(j, i) + "*", end=""); 

    def moverCirculo(x, y, c):
        from colorama import init, Fore, Cursor;
        init(); 
        
        for i in range(y, y + 11):
            for j in range(x, x + 21):
                if (i == y or i == y + 10) and (j > x + 2 and j < x + 17): #Verificamos estar en borde horizontal
                    print(Cursor.POS(j, i) + "*", end=""); 
                elif (j == x or j == x + 19) and (i > y + 1 and i < y + 9): #Verifcamos estar en un borde vertical
                    print(Cursor.POS(j, i) + "*", end=""); 
                elif (j == x + 1 and i == y + 1) or (j == x + 1 and i == y + 9) or (j == x + 18 and i == y + 1) or (j == x + 18 and i == y + 9): #Verificamos estar en una esquina
                    print(Cursor.POS(j, i) + "*", end=""); 


    imprimirDatos(); #Imprime los datos de referencia al usuario
    
    #Posiciones en X y Y de las figuras
    triangulo_x = 12; 
    triangulo_y = 59; 
    
    cuadrado_x = 12; 
    cuadrado_y = 10; 

    circulo_x = 85; 
    circulo_y = 12; 

    dibujarArea(); #Dibujamos el area del programa
    
    #Mostramos las figuras en su posicion por defecto
    moverTriangulo(triangulo_x, triangulo_y, 0); 
    moverCuadrado(cuadrado_x, cuadrado_y, 0); 
    moverCirculo(circulo_x, circulo_y, 0); 

    input(); 

def imprimir():
    e1(); 

imprimir(); 
