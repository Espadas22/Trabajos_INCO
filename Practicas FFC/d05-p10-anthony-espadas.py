#practica 10
#espadas rodriguez anthony jonathan
#mariscal cervantes diego maximiliano

def e1():
    import sys; 
    from colorama import init, Fore, Style, Cursor;
    init(autoreset=True); 

    def imprimirDatos():
        print(Fore.MAGENTA + "practica 10");
        print(Fore.MAGENTA + "espadas rodriguez anthony jonathan");
        print(Fore.MAGENTA + "mariscal cervantes diego maximiliano\n");
        print(Fore.CYAN + "Selecciona: ", end="");
        print(Fore.CYAN + "\b (1)Cuadrado ", end=""); 
        print(Fore.CYAN + "\b (2)Triangulo ", end=""); 
        print(Fore.CYAN + "\b (3)Circulo ", end=""); 
        print(Fore.CYAN + "\b (0)Salir ", end="");
        print(Fore.WHITE + "\b ||", end=" ");
        print(Fore.CYAN + "Usa las direcciones W A S D para mover la figura\n"); 
    
    def dibujarArea(): #Dibuja el cuadrado que delimita las figuras
        for i in range(7, 30):
            for j in range(1, 120):
                if i == 7 or i == 29 or j == 1 or j == 119: #Valida estar en la primer o ultima linea
                    print(Fore.WHITE + Style.BRIGHT + Cursor.POS(j,i) + "*"); 
                    
    #Funcion que se encarga de dibujar el asterisco del color corresponiente
    def dibujarAsterisco(linea, columna, color): 
        linea = ((linea + 7) % 22) + 7; 
        columna = (columna % 119); 

        if color == 1:
            print(Fore.GREEN + Style.BRIGHT + Cursor.POS(columna, linea) + "*"); 
        elif color == 2:
            print(Fore.YELLOW + Style.DIM + Cursor.POS(columna, linea) + ".");  
        elif color == 3: 
            print(Fore.RED + Style.DIM + Cursor.POS(columna, linea) + "."); 
        elif color == 4:
            print(Fore.WHITE + Style.DIM + Cursor.POS(columna, linea) + "."); 

    def moverTriangulo(columna, linea, color): #Se encarga de dibujar al triangulo en consola
        distancia = 0; #Genera la separacion entre los bordes

        for i in range(linea, linea + 11):#Genera una altura de 10 lineas
            for j in range(columna - distancia, columna + distancia): #Abre distancia de los lados segun se acerca a la base
                if i == linea or i == linea + 10: #Valida estar en la primer o ultima linea 
                    if color == 1:
                        dibujarAsterisco(i, j, 1); 
                    elif color == 2:
                        dibujarAsterisco(i, j, 2); 
                    elif color == 3:
                        dibujarAsterisco(i, j, 3); 
                    else:
                        dibujarAsterisco(i, j, 4); 
                elif j == columna - distancia or j == columna + distancia -1: #Valida estar en los extremos
                    if color == 1:
                        dibujarAsterisco(i, j, 1); 
                    elif color == 2:
                        dibujarAsterisco(i, j, 2); 
                    elif color == 3:
                        dibujarAsterisco(i, j, 3); 
                    else:
                        dibujarAsterisco(i, j, 4); 
            
            distancia += 1; 

    def moverCuadrado(columna, linea, color): #Se encarga de dibujar al cuadrado en consola
        for i in range(linea, linea + 11): #Genera lado de 10 lineas
            for j in range(columna, columna + 21): #Genera lado de 20 columnas
                if i == linea or i == linea + 10: #Revisa que nos encontremos en los bordes
                    if color == 1:
                        dibujarAsterisco(i, j, 1); 
                    elif color == 2:
                        dibujarAsterisco(i, j, 2); 
                    elif color == 3:
                        dibujarAsterisco(i, j, 3); 
                elif j == columna or j == columna + 20: #E imprime el asterisco
                    if color == 1:
                        dibujarAsterisco(i, j, 1); 
                    elif color == 2:
                        dibujarAsterisco(i, j, 2); 
                    elif color == 3:
                        dibujarAsterisco(i, j, 3); 

    def moverCirculo(columna, linea, color):
        for i in range(linea, linea + 11):
            for j in range(columna, columna + 21):
                if (i == linea or i == linea + 10) and (j > columna + 2 and j < columna + 17): #Verificamos estar en borde horizontal
                    if color == 1:
                        dibujarAsterisco(i, j, 1); 
                    elif color == 2:
                        dibujarAsterisco(i, j, 2); 
                    elif color == 3:
                        dibujarAsterisco(i, j, 3); 
                elif (j == columna or j == columna + 19) and (i > linea + 1 and i < linea + 9): #Verifcamos estar en un borde vertical
                    if color == 1:
                        dibujarAsterisco(i, j, 1); 
                    elif color == 2:
                        dibujarAsterisco(i, j, 2); 
                    elif color == 3:
                        dibujarAsterisco(i, j, 3); 
                elif (j == columna + 1 and i == linea + 1) or (j == columna + 1 and i == linea + 9) or (j == columna + 18 and i == linea + 1) or (j == columna + 18 and i == linea + 9): #Verificamos estar en una esquina
                    if color == 1:
                        dibujarAsterisco(i, j, 1); 
                    elif color == 2:
                        dibujarAsterisco(i, j, 2); 
                    elif color == 3:
                        dibujarAsterisco(i, j, 3); 
    
    #Funciones que dibujan la pantalla segun la figura seleccionada
    def pintarPantallaCuadrado(cuadrado_x, cuadrado_y, color_cuadrado, triangulo_x, triangulo_y, color_triangulo, circulo_x, circulo_y, color_circulo):
        print('\x1b[2J', end = ""); 
        imprimirDatos(); 
        moverTriangulo(triangulo_x, triangulo_y, color_triangulo); 
        moverCirculo(circulo_x, circulo_y, color_circulo); 
        moverCuadrado(cuadrado_x, cuadrado_y, color_cuadrado); 
        dibujarArea(); 

    def pintarPantallaTriangulo(cuadrado_x, cuadrado_y, color_cuadrado, triangulo_x, triangulo_y, color_triangulo, circulo_x, circulo_y, color_circulo):
        print('\x1b[2J', end = ""); 
        imprimirDatos(); 
        moverCuadrado(cuadrado_x, cuadrado_y, color_cuadrado);  
        moverCirculo(circulo_x, circulo_y, color_circulo); 
        moverTriangulo(triangulo_x, triangulo_y, color_triangulo);
        dibujarArea();   

    def pintarPantallaCirculo(cuadrado_x, cuadrado_y, color_cuadrado, triangulo_x, triangulo_y, color_triangulo, circulo_x, circulo_y, color_circulo):
        print('\x1b[2J', end = ""); 
        imprimirDatos(); 
        moverCuadrado(cuadrado_x, cuadrado_y, color_cuadrado);  
        moverTriangulo(triangulo_x, triangulo_y, color_triangulo);
        moverCirculo(circulo_x, circulo_y, color_circulo); 
        dibujarArea(); 

    #Posiciones en X y Y de las figuras
    triangulo_x = 59; 
    triangulo_y = 21; 
    
    cuadrado_x = 10; 
    cuadrado_y = 21; 

    circulo_x = 85; 
    circulo_y = 21; 

    pintarPantallaCuadrado(cuadrado_x, cuadrado_y, 2, triangulo_x, triangulo_y, 4, circulo_x, circulo_y, 3); 

    seleccion = "4"; #Variable que toma los valores introducidos por el usuario

    figura = ""; #Variable que guarda la figura seleccionada

    while seleccion != "0":
        seleccion = sys.stdin.read(1);  

        if seleccion == "1": #Determina si se eligio el cuadrado
            pintarPantallaCuadrado(cuadrado_x, cuadrado_y, 1, triangulo_x, triangulo_y, 2, circulo_x, circulo_y, 3); 
            figura = "cuadrado"; 
        elif seleccion == "2": #Determina si se eligio el triangulo
            pintarPantallaTriangulo(cuadrado_x, cuadrado_y, 3, triangulo_x, triangulo_y, 1, circulo_x, circulo_y, 2); 
            figura = "triangulo";   
        elif seleccion == "3": #determina si se eligio el circulo
            pintarPantallaCirculo(cuadrado_x, cuadrado_y, 3, triangulo_x, triangulo_y, 2, circulo_x, circulo_y, 1); 
            figura = "circulo"; 
        elif seleccion == "W" or seleccion == "w": #Se movera la sigura seleccionada hacia arriba
            if figura == "cuadrado":
                cuadrado_y -= 1; 
                pintarPantallaCuadrado(cuadrado_x, cuadrado_y, 1, triangulo_x, triangulo_y, 2, circulo_x, circulo_y, 3); 
            elif figura == "triangulo":
                triangulo_y -= 1; 
                pintarPantallaTriangulo(cuadrado_x, cuadrado_y, 3, triangulo_x, triangulo_y, 1, circulo_x, circulo_y, 2); 
            elif figura == "circulo": 
                circulo_y -= 1; 
                pintarPantallaCirculo(cuadrado_x, cuadrado_y, 3, triangulo_x, triangulo_y, 2, circulo_x, circulo_y, 1); 
        elif seleccion == "S" or seleccion == "s": #Se movera la figura seleccionada hacia abajo
            if figura == "cuadrado":
                cuadrado_y += 1; 
                pintarPantallaCuadrado(cuadrado_x, cuadrado_y, 1, triangulo_x, triangulo_y, 2, circulo_x, circulo_y, 3); 
            elif figura == "triangulo":
                triangulo_y += 1; 
                pintarPantallaTriangulo(cuadrado_x, cuadrado_y, 3, triangulo_x, triangulo_y, 1, circulo_x, circulo_y, 2); 
            elif figura == "circulo": 
                circulo_y += 1; 
                pintarPantallaCirculo(cuadrado_x, cuadrado_y, 3, triangulo_x, triangulo_y, 2, circulo_x, circulo_y, 1); 
        elif seleccion == "A" or seleccion == "a": #Se movera la figura seleccionada a la izquierda
            if figura == "cuadrado":
                cuadrado_x -= 2; 
                pintarPantallaCuadrado(cuadrado_x, cuadrado_y, 1, triangulo_x, triangulo_y, 2, circulo_x, circulo_y, 3); 
            elif figura == "triangulo":
                triangulo_x -= 2; 
                pintarPantallaTriangulo(cuadrado_x, cuadrado_y, 3, triangulo_x, triangulo_y, 1, circulo_x, circulo_y, 2); 
            elif figura == "circulo": 
                circulo_x -= 2; 
                pintarPantallaCirculo(cuadrado_x, cuadrado_y, 3, triangulo_x, triangulo_y, 2, circulo_x, circulo_y, 1); 
        elif seleccion == "D" or seleccion == "d": #Se movera la figura seleccionada a la derecha
            if figura == "cuadrado":
                cuadrado_x += 2; 
                pintarPantallaCuadrado(cuadrado_x, cuadrado_y, 1, triangulo_x, triangulo_y, 2, circulo_x, circulo_y, 3); 
            elif figura == "triangulo":
                triangulo_x += 2; 
                pintarPantallaTriangulo(cuadrado_x, cuadrado_y, 3, triangulo_x, triangulo_y, 1, circulo_x, circulo_y, 2); 
            elif figura == "circulo": 
                circulo_x += 2; 
                pintarPantallaCirculo(cuadrado_x, cuadrado_y, 3, triangulo_x, triangulo_y, 2, circulo_x, circulo_y, 1); 

def imprimir():
    e1(); 

imprimir(); 
