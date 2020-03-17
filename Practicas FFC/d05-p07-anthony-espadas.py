#practica 07
#espadas rodriguez anthony jonathan
#mariscal cervantes diego maximiliano 

print("Practica  07");
print("espadas rodriguez anthony jonathan");
print("mariscal cervantes diego maximiliano\n");

def ejercicio(numero): 
    print("******************************************************************\n");
    print("Ejercicio", numero);

#funcion auxiliar para evitar valores negativos
def validarPositivo():
    valor = float(input("Ingresalo de nuevo\n"));
    if valor < 0:
        print("Tu valor no puede ser menor a cero\n");
        valor = validarPositivo();
    return valor;

#Validamos los parametros de la calificacion
def validarCalificacion():
    valor = float(input("Ingresala de nuevo\n"));
    if (valor < 0) | (valor > 100):
        print("Las calificaciones deben estar entre 0 y 100")
        valor = validarCalificacion();
    return valor;
    

def e1():
    ejercicio(1);
    print("Donde te decimos si aprobaste o no esa materia\n(minima aprobatoria 80)\n");

    calificacion = float(input("Ingresa la calificacion\n"));
    if (calificacion < 0) | (calificacion > 100):
        print("Las calificaciones deben estar entre 0 y 100\n");
        calificacion = validarCalificacion();
    if calificacion > 80:
            print("Aprobaste\n");
    else:
            print("Reprobaste\n");
    


def e2():
    ejercicio(2);
    print("En el que descubrimos cual sera el nuevo salario de un trabajador\n");

    salario = float(input("Ingresa el salario\n"));

    if salario < 0:
        print("El salario debe ser un numero positivo");
        salario = validarPositivo();
    
    if salario < 20000:
        print("Incremento del 30%!");
        salario = salario*1.3;
        print("El nuevo salario sera de: %.2f" % (salario));
    elif salario < 23000:
        salario = salario*1.15;
        print("Incremento del 15%!");
        print("El nuevo salario sera de %.2f: " % (salario));
    elif salario < 25000:
        print("Incremento del 5%!");
        salario = salario*1.05;
        print("El nuevo salario sera de: %.2f" % (salario));
    else:
        print("Sin cambios en el salario");



def e3():
    ejercicio(3);
    pago_por_hora = 15.4025;
    print("Donde calculamos el ingreso basandonos en las horas trabajadas (considerando la hora como", pago_por_hora, "pesos)");

    
    horas_trabajadas = int(input("Cuantas horas trabajaste?\n"));

    if horas_trabajadas < 0:
        print("El numero de horas debe ser positivo");
        horas_trabajadas = validarPositivo();
    
    if horas_trabajadas <= 40:
        sueldo = horas_trabajadas*pago_por_hora;
        print("Recibiras %.2f pesos" % (sueldo));
    elif horas_trabajadas <= 48:
        #al superar las 40 se sobreentiende que estas horas se pagaran integras
        sueldo = pago_por_hora*40;
        dobles = horas_trabajadas - 40;
        #primero se hace el calculo de las horas dobles para indicar cuentas fueron
        print("Hubo", dobles, "horas pagadas al doble");
        #despues se calcula cuanto se pagara por ellas
        dobles = dobles*pago_por_hora*2
        sueldo += dobles;
        print("Recibiras %.2f pesos" % (sueldo));
    else:
        sueldo = pago_por_hora*40;
        #al llegar a las horas triples ya no es necesario calcular las dobles
        dobles = 8*pago_por_hora*2;
        print("Hubo 8 horas pagadas al doble");
        triples = horas_trabajadas - 48;
        print("Hubo", triples, "horas pagadas al triple");
        triples = triples*pago_por_hora*3
        sueldo = sueldo + dobles + triples;
        print("Recibiras %.2f pesos" % (sueldo));


def e4():
    ejercicio(4);
    print("Vamos a descubrir de a cuanto toca el subsidio");

    hijos = int(input("Cuantos hijos hay en la familia?\n"));

    if hijos < 0:
        print("La cantidad de hijos no puede ser negativa");
        hijos = validarPositivo();

    
    #para ejecutar en caso de que el numero de hijos en edad escolar sea mayor que el numero de hijos
    def validarEdadEscolar():
        valor = int(input("Ingresala de nuevo\n"));

        if valor > hijos:
            print("La cantidad de hijos en edad escolar no puede ser mayor que la de hijos");
            valor = validarEdadEscolar();
        return valor;


    #si no hay hijos no hay porque hacer esta pregunta, pero se deja la variable en cero para no generar problemas en el calculo
    edad_escolar = 0;
    if hijos > 0:
        edad_escolar = int(input("Cuantos tienen entre 6 y 18 años?\n"));
        if edad_escolar > hijos:
            print("La cantidad de hijos en edad escolar no puede ser mayor que la de hijos");
            edad_escolar = validarEdadEscolar();

    #corroboramos que la respuesta sea solo 'si' o 'no'
    def validarViudez():
        respuesta = str(input("La madre es viuda?\n"));
        if (respuesta != "si") & (respuesta != "no"):
            print("La respuesra debe ser 'si' o 'no'");
            respuesta = validarViudez();
        return respuesta;


    viuda = str(input("La madre es viuda?\n"));
    if (viuda !="si") & (viuda !="no"):
        print("La respuesra debe ser 'si' o 'no'");
        viuda = validarViudez();

    #el subsidio comienza en cero para los casos donde no hay hijos
    subsidio = 0
    if (hijos <= 2) & (hijos > 0):
        subsidio = 70;
    elif (hijos <=5) & (hijos > 0):
        subsidio = 90;
    elif hijos >= 6:
        subsidio = 120;
    #sumamos los agregados
    if viuda == "si":
        subsidio += 10;
    subsidio = subsidio + (edad_escolar*10)
    print("El total del subsidio sera de: ", subsidio, "pesos");




def e5():
    ejercicio(5);
    print("Donde determinamos si eres apto para el equipo de baloncesto\n");

    #Asegura tener un año dentro del rango valido
    def validarAnio():
        valor = int(input("Ingresalo de nuevo\n"));
        if valor > 2020:
            print("El año no puede ser mayor al actual\n")
            valor = validarAnio();
        return valor;

    anio = int(input("Dame tu año de nacimiento:\n"));
    if anio > 2020:
        print("El año no puede ser mayor al actual");
        anio = validarAnio();

    #Validar tener el mes dentro de un rango valido
    def validarMes():
        valor = int(input("Ingresalo de nuevo\n"));
        if (anio == 2020) & (valor > 3):
            print("El mes no puede ser mayor al actual");
            valor = validarMes();
        elif (valor < 1) | (valor > 12):
            print("Los meses deben estar entre 1 y 12\n")
            valor = validarMes();
        return valor;

    mes = int(input("Dame tu mes de nacimiento (numero)\n"));
    if (anio == 2020) & (mes > 3):
        print("El mes no puede ser mayor al actual");
        mes = validarMes();
    elif (mes < 1) | (mes > 12):
        print("Los meses deben estar entre 1 y 12");
        mes = validarMes();

    #Asegura tener un dia dentro de los rangos validos
    def validarDia():
        valor = int(input("Ingresalo de nuevo\n"));
        if (anio == 2020) & (mes == 3) & (valor > 11):
            print("El dia no puede ser mayor al actual");
            valor = validarDia();
        elif (anio % 4 == 0) & (mes == 2) & (valor > 29):
            print("Este mes no tiene", valor, "dias");
            valor = validarDia();
        elif (anio % 4 != 0) & (mes == 2) & (valor > 28):
            print("Este mes no tiene", valor, "dias");
            valor = validarDia();
        elif ((mes == 4) | (mes == 6) | (mes == 9) | (mes == 11)) & (valor > 30):
            print("Este mes no tiene", valor, "dias");
            valor = validarDia();
        elif ((mes == 1) | (mes == 3) | (mes == 5) | (mes == 7) | (mes == 8) | (mes == 10) | (mes == 12)) & (dia > 31):
            print("Valor fuera de rango");
            valor = validarDia();
        return valor;

    print("Dame tu dia de nacimiento:")
    dia = int(input());
    if (anio == 2020) & (mes == 3) & (dia > 11):
        print("El dia no puede ser mayor al actual");
        dia = validarDia();
    elif (anio % 4 == 0) & (mes == 2) & (dia > 29):
        print("Este mes no tiene", dia, "dias");
        dia = validarDia();
    elif (anio % 4 != 0) & (mes == 2) & (dia > 28):
        print("Este mes no tiene", dia, "dias");
        dia = validarDia();
    elif ((mes == 4) | (mes == 6) | (mes == 9) | (mes == 11)) & (dia > 30):
        print("Este mes no tiene", dia, "dias");
        dia = validarDia();
    elif ((mes == 1) | (mes == 3) | (mes == 5) | (mes == 7) | (mes == 8) | (mes == 10) | (mes == 12)) & (dia > 31):
        print("Valor fuera de rango");
        dia = validarDia();
        

    #definimos esta funciona para que solo se ejecute en los casos que pasaron el filtro
    def registro():
        #Asegura que el grado sea por lo menos 1
        def validarGrado():
            valor = int(input("Ingresalo nuevamente\n"));
            if valor < 1:
                print("El grado debe ser al menos 1");
                valor = validarGrado();
            return valor;

        #El grupo estara dentro de los parametros permitidos
        def validarGrupo():
            valor = str(input("Introduce un grupo valido\n"));
            if (valor != "A") & (valor != "B") & (valor != "C") & (valor != "D"):
                print("Ese grupo no existe");
                valor = validarGrupo();
            return valor;

        #Limita el turno a dos opciones
        def validarTurno():
            print("Debes elegir entre 'matutino' y 'vespertino'\n");
            eleccion = str(input());
            if (eleccion != "matutino") & (eleccion != "vespertino"):
                print("Respuesta no valida");
                eleccion = validarTurno();
            return eleccion;
        
        grado = int(input("Que grado cursas?\n"));

        if grado < 1:
            print("El grado debe ser al menos 1");
            grado = validarGrado();

        grupo = str(input("En que grupo? (A, B, C, D)\n"));
        if (grupo != "A") & (grupo != "B") & (grupo != "C") & (grupo != "D"):
            print("Ese grupo no existe");
            grupo = validarGrupo();

        print("Ingresa tu promedio hasta el", grado, "grado");
            
        promedio = float(input());
        if (promedio < 0) | (promedio > 100):
            print("La calificacion debes estar entre 0 y 100");
            promedio = validarCalificacion();
            
        if promedio < 60:
            print("Lo sentimos mucho pero no podrás formar parte por tu bajo promedio");
        if promedio >= 60:
            print("Prefieres el horario matutino o vespertino?");
            horario = str(input());
            if (horario != "matutino") & (horario != "vespertino"):
                print("Respuesta no valida");
                horario = validarTurno();
            print("Registro completado para turno", horario);
    
    #Validamos que sea mayor de 18
    if 2020 - anio > 18:
        print("Podrás formar parte del equipo de baloncesto");
        registro()
    #si cumple 18 este año verificamos que su cumpleaños ya haya pasado
    if (2020 - anio == 18) & (mes < 3):
        print("Podrás formar parte del equipo de baloncesto");
        registro()
    #si cumple años este mes verificamos que su cumpleaños ya haya pasado
    if (2020 - anio == 18) & (mes == 3) & (dia < 4):
        print("Podrás formar parte del equipo de baloncesto");
        registro()
    #para casos donde la edad minima no es cumplida
    if 2020 - anio < 18:
        print("Lo sentimos, no podras formar parte del equipo de baloncesto");
    #para casos donde cumpleaños este año pero aun no es el mes
    if (2020 - anio == 18) & (mes > 3):
        print("Lo sentimos, no podras formar parte del equipo de baloncesto");
    #para casos donde cumpleaños este mes pero aun no es el dia
    if (2020 - anio == 18) & (mes == 3) & (dia > 11):
        print("Lo sentimos, no podras formar parte del equipo de baloncesto");


    
def e6():
    ejercicio(6);
    print("Donde evaluamos el desempeño de tu auto\n")

    #Aseguramos un valor de 6 digitos
    def validarMatricula():
        valor = int(input("Introduzca una matricula valida\n"));
        if (valor < 99999) | (valor > 999999):
            print("La matricula debe contar con 6 digitos");
            valor = validarMatricula();
    
    #Cerramos el rango de los kilometros por litro
    def validarKMPL():
        valor = int(input("Introduce un valor dentro del rango\n"));
        if (valor < 10) | (valor > 16):
            print("Los kilometros por litro deben estar entre 10 y 16");
            valor = validarKMPL();
        return valor;

    matricula = int(input("Dame la matricula de tu auto(6 digitos)\n"));
    if (matricula < 99999) | (matricula > 999999):
        print("La matricula debe contar con 6 digitos");
        matricula = validarMatricula();

    print("A cuantas millas corre?");
    millas = float(input());
    if millas < 0:
        print("Las millas no pueden ser negativas");
        millas = validarPositivo();
    if millas > 80:
        print("Esta arriba del límite de velocidad (80 millas)");

    print("Cuantos kilometros ha recorrido el auto?");
    kilometraje = float(input());
    if kilometraje < 0:
        print("El kilometraje no puede ser negativo");
        kilometraje = validarPositivo();
    if (kilometraje > 200) & (kilometraje < 350):
        print("Le hace falta mantenimiento al auto");

    kmpl = int(input("Cuantos kilometros recorre con un litro?\n"));
    if (kmpl < 10) | (kmpl > 16):
        print("Los kilometros por hora debene estar entre 10 y 16");
        kmpl = validarKMPL();
    if (kmpl >= 14) & (kmpl <= 16):
        print("Consume poca gasolina");
        rendimiento = 100/kmpl;
        print("Solo necesita ", rendimiento, "litros para recorrer 100km");
    else:
        print("Consume algo de gasolina");
    


def e7():
    ejercicio(7);
    print("Para el que tuvimos que investigar como se cuentan los puntos en el basquetbol");
    print("(con la finalidad de ayudar a un equipo a saber cuantos puntos anota cada uno de sus jugadores)\n");

    def validarJugador():
        valor = int(input("Introduce un numero valido\n"));
        if (valor > 99) | (valor < 0):
            print("Los numeros de jugador estan entre 0 y 99");
            valor = validarJugador();
        return valor;

    print("Dame el numero del jugador");
    jugador = int(input());
    if (jugador > 99) | (jugador < 0):
        print("Los numeros de jugador estan entre 0 y 99");
        jugador = validarJugador();

    print("Dime cuantos tiros anoto el jugador", jugador);
    anotados = int(input());
    if anotados < 0:
        print("Las anotaciones no pueden ser negativas");
        anotados = validarPositivo();

    print("Dime cuentos tiros fallo el jugador", jugador);
    fallados = int(input());
    if fallados < 0:
        print("Los fallos no pueden ser negativos");
        fallados = validarPositivo();

    if (anotados > 0) & (fallados > 0):
        tirados = anotados + fallados;
        print("El jugador", jugador, "hizo un total de", tirados, "tiros");

    print("Dime cuantos puntos anoto el jugador", jugador);
    puntos = int(input());
    if puntos < 0:
        print("Los puntos no pueden ser negativos");
        puntos = validarPositivo();

    #definimos la funcion que calcula los puntos
    def calcular():
        #se saca el porcentaje de los tiros anotados y se divide entre 33.33 para tenerlo en terminos de tercios
        promedio = int(((anotados * 100)/(anotados+fallados))/33.33)
        print("En promedio, el jugador", jugador, "anoto", promedio, "tiros de cada 3");
        

    
    if (puntos >= 3) & (puntos <= 6):
            print("Anoto pocos puntos");
    elif (puntos >= 7) & (puntos <= 15):
            print("Anoto puntos aceptables");
            calcular();
    elif puntos >= 16:
            print("Felicidades por sus anotaciones");
            calcular();
    else:
        print("Hay que mejorar el juego");

e1();
e2();
e3();
e4();
e5();
e6();
e7();
