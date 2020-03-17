#practica 05 
#Espadas Rodriguez Anthony Jonathan
#Mariscal Cervantes Diego Maximiliano 

print("Practica  5");
print("Espadas Rodriguez Anthony Jonathan");
print("Mariscal Cervantes Diego Maximiliano\n");

print("*******************************************\n");

print("Parte I");
print("Construimos expresiones para 6 variables con los valores");
print("A=5, B=25, C=10\n");

def resultado (nombre, valor):

    print("El valor de ", nombre, " es: ", valor);

a = 5;
b = 25;
c = 10;

x1 = a+(b+c) % a;
x2 = (a**b)*c/a;
x3 = b+b/c/a;
x4 = a+b % c;
x5 = (a+b)//c;
x6 = c+(b/c)*b;

resultado ("x1", x1);
resultado ("x2", x2);
resultado ("x3", x3);
resultado ("x4", x4);
resultado ("x5", x5);
resultado ("x6", x6);

print("\n*******************************************\n");
print("Parte II");
print("Determinaremos el valor numerico de 6 constantes\n");

c1 = 8+5*3+9*6/2;
c2 = (2**3) % 4;
c3 = (33+3*4)/8;
c4 = 2**55*3;
c5 = 3+9*(18-3**2)//5;
c6 = 16*6-3*2;

resultado ("c1", c1);
resultado ("c2", c2);
resultado ("c3", c3);
resultado ("c4", c4);
resultado ("c5", c5);
resultado ("c6", c6);

print("\n*******************************************");
