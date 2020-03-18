#practica 09
#espadas rodriguez anthony jonathan
#mariscal cervantes diego maximiliano 

print("practica  09");
print("espadas rodriguez anthony jonathan");
print("mariscal cervantes diego maximiliano\n");

def e01(): #Calculo de descuentos en un teatro segun edad
    tope = 2;
    boleto = 80;
    categoria_1 = categoria_2 = categoria_3 = categoria_4 = categoria_5 = 0;

    for i in range(tope):
        try:
            edad = int(input("Ingresa la edad del cliente:\n"));

        except:
            print("La edad debe ser un entero positivo");

        if edad < 0:
            print("La edad debe ser un entero positivo");
        elif edad < 5:
            print("Lo sentimos, no ingresan menores de 5 años");
        elif edad < 15:
            precio = boleto*.65;
            print("Categoria 1, tienes 35%% de descuento, paga solo %.2f" % (precio));
            categoria_1 += boleto - precio;
        elif edad < 20:
            precio = boleto*.75
            print("Categoria 2, tienes 25%% de descuento, paga solo %.2f" % (precio));
            categoria_2 += boleto - precio;
        elif edad < 46:
            precio = boleto*.90;
            print("Categoria 3, tienes 10%% de descuento, paga solo %.2f" % (precio));
            categoria_3 += boleto - precio;
        elif edad < 65:
            precio = boleto*.75
            print("Categoria 4, tienes 25%% de descuento, paga solo %.2f" % (precio));
            categoria_4 += boleto - precio;
        elif edad < 125:
            precio = boleto*.65;
            print("Categoria 5, tienes 35%% de descuento, paga solo %.2f" % (precio));
            categoria_5 += boleto - precio;
        else:
            print("Nadie ha vivido tanto, verifique sus datos")

        eleccion = str(input("Quieres ingresar otro usuario? (si/no)\n"));

        if eleccion == "si":
            tope +=1;

def imprime():
    e01();

imprime();
