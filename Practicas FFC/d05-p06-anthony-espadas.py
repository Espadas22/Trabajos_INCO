#practica 06
#espadas rodriguez anthony jonathan
#mariscal cervantes diego maximiliano 

print("Practica  06");
print("Espadas Rodriguez Anthony Jonathan");
print("Mariscal Cervantes Diego Maximiliano\n");

def asteriscos(): 
    print("******************************************************************\n");

asteriscos();

def ejercicio(numero):
    print("Ejercicio", numero, ("\n"));

ejercicio(1);

def tarea_1():
    t1 = 30;
    return t1;

def tarea_2():
    t2 = 75;
    return t2;

def tarea_3():
    t3 = 85;
    return t3;

def examen():
    e = 100;
    return e;

def e01_1():
    tareas_m = ((tarea_1() + tarea_2() + tarea_3())/3)*.8;
    e_m = (examen())*.2;
    calificacion_m = tareas_m + e_m;
    return calificacion_m;

def e01_2():
    tareas_f = ((tarea_1() + tarea_2() + tarea_3())/3)*.85;
    e_f = (examen())*.15;
    calificacion_f = tareas_f + e_f;
    return calificacion_f;

def e01_3():
    tareas_q = ((tarea_1() + tarea_2() + tarea_3())/3)*.25;
    e_q = (examen())*.75;
    calificacion_q = tareas_q + e_q;
    return calificacion_q;

print("El promedio general es: ", (e01_1() + e01_2() + e01_3())/3);
print("La calificacion de matematicas es: ", e01_1());
print("La calificacion de fisica es: ", e01_2());
print("La calififcacion de quimica es: ", e01_3(), "\n");

asteriscos();

ejercicio(2);

def e02_1():
    capital = 58000;
    return capital;

def e02_2():
    ganancia = (e02_1())*.033;
    return ganancia;

print("Si un individuo decide invertir un capital de", e02_1(), "pesos en un banco\n que paga un 3.3% mensual, en un mes habra generado una ganancia de", e02_2(), "pesos\n");

asteriscos();

ejercicio(3);

def e03_1():
    ventas = (4*tarea_1() + 3*tarea_2() + 3*tarea_3());
    comision = ventas*.15
    return comision;

def e03_2():
    sueldo_base = examen();
    sueldo_final = sueldo_base + e03_1(); 
    return sueldo_final;

print("Un vendedor que realizo 10 ventas en un año gano una comision de", e03_1(), "\nlo que lo deja con un sueldo final de", e03_2(), "\n");

asteriscos();

ejercicio(4);

def e04():
    compra = examen();
    pago = compra * .835;
    return pago;

print("El pago total, despues de aplicar el descuento de 16.5%, es de", e04(), "pesos\n");

asteriscos();

ejercicio(5);

def e05():
    parciales = examen()* .55;
    final = examen()* .3;
    trabajo_final = tarea_1() * .15;
    calificacion_final = parciales + final + trabajo_final;
    return calificacion_final;

print("La calificacion final en la materia de algoritmia es:", e05(), "\n");

asteriscos();

ejercicio(6);

def e06_1():
    mujeres = tarea_1();
    hombres = tarea_2();
    total = hombres + mujeres;
    return mujeres, hombres, total;

def e06_2():
    mujeres, hombres, total = e06_1();
    porcentaje_mujeres = mujeres/total*100;
    return porcentaje_mujeres;

def e06_3():
    mujeres, hombres, total = e06_1();
    porcentaje_hombres = hombres/total*100;
    return porcentaje_hombres;

print("El porcentaje de alumnos es", e06_2(),"% mujeres y", e06_3(), "% hombres\n");

asteriscos();

ejercicio(7);

def e07():
    dia_nacimiento = 22;
    mes_nacimiento = 10;
    año_nacimiento = 1996;
    dia_actual = 26;
    mes_actual = 2;
    año_actual = 2020;
    edad = año_actual - año_nacimiento;
    if mes_nacimiento > mes_actual:
        edad -= 1;
        return edad;
    if mes_nacimiento == mes_actual:
        if dia_nacimiento > dia_actual:
            edad -= 1;
            return edad;
    return edad;

print("La edad es de", e07(), "años\n");

asteriscos();

ejercicio(8);

def e08_1():
    presupuesto = 85000;
    return presupuesto;

def e08_2():
    presupuesto_gine = e08_1() * .2;
    return presupuesto_gine;

def e08_3():
    presupuesto_trauma = e08_1() * .2;
    return presupuesto_trauma;

def e08_4():
    presupuesto_pedia = e08_1() * .6;
    return presupuesto_pedia;

print("Para un presupuesto de", e08_1(), "pesos.\nEl servicio de ginecologia tiene", e08_2(), "pesos,\nel de traumatologia", e08_3(), "pesos\ny el de pediatria", e08_4(), "pesos.\n");

asteriscos();

ejercicio(9);

def e09():
    producto = tarea_2();
    precio = producto *1.4;
    return precio;

print("El precio del producto debe ser de", e09(), "pesos para tener una ganancia del 40%\n");

asteriscos();

ejercicio(10);

def e10():
    tiempos = tarea_1() + tarea_2() + tarea_3();
    promedio = tiempos/7;
    return promedio;

print("El tiempo promedio es de", e10(),"\n");

asteriscos();

ejercicio(11);

def e11_1():
    inversion = tarea_1() + tarea_2() + tarea_3();
    return inversion;

def e11_2():
    porcentaje_1 = tarea_1()/e11_1()*100;
    return porcentaje_1;

def e11_3():
    porcentaje_2 = tarea_2()/e11_1()*100;
    return porcentaje_2;

def e11_4():
    porcentaje_3 = tarea_3()/e11_1()*100;
    return porcentaje_3;

print("El socio 1 invirtio", e11_2(), "%\nEl socio 2 invirtio", e11_3(), "%\nEl socio 3 invirtio", e11_4(),"%\n");

