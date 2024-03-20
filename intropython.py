#comentario de una linea
#todo lo que va despues es ignorado por el interpréte de python


#variable: espacio de memoria, con nombre, donde guardo valores
#los nombres de variables deben ser cortos, descriptivos, NO TENER ESPACIOS
#en blanco, ni caracteres especiales, no deben empezar por un número

#descriptivo significa que representa la categoria del dato que quiero guardar
#en python las variables pueden contener cualquier dato de tipo primitvo
#numeros (enteros, reales), cadena de carácteres(string),booleanos(true,false)
#carácteres (letras)
variable=1
variable="juventud divino tesoro, te vas para no volver"
variable=True
variable="a"
variable=3.1414926535
#para asignar un valor a la variable se usa el operador = 

#operadores: mecanismo para obtener un dato apartir de otros datos.
#los datos que intervienen se llaman aperandos.

#Aritmeticos: +,*,-,/,%
#de comparación: retornan true o false. <,> >=, <= !=
#los de lógica Boleana: Or, and. retornan T o F de acuerdo a una tabla de verdad
#los operandos siempre son boleanos (true o false)

a=True
b=False

print(a and b)
#los operados boleanos y de comparción son muy utilizados al
#definir condiciones

#sentencias de control de código: en general un programa se ejecuta 
#linea por línea de manera sencuencial se puede romper esa sencuencialidad
# empleando un conjunto de sentencias(expresiones) que permite: 
#1. selecccionar la ejecución de un bloque de código
#2. repetir la ejecución de un blque de codigo 
#3. seleccionar entre ejecutar un bloqyue de código u otro bloque de código
# de esa manera podemos "romper" la secuencialidad
#princios del paradigma de programación estructurado

#sentencia if. si se cumple una condición (se evalua como true)se ejecuta como un bloque de codigo

print("linea 1")
print("linea 2")

if 5>8 or 3<7: 
    print("esto se muestra si la condición es verdadera")
else:
    print("esto se muestra si la condición es false")
    
entrada=int(input("cuantos años tiene?"))

if entrada<18:
    print("es un menor de edad")
else:
    print("es un mayor de edad")
    
#taller crear un programa en python que genere un numero aleatorio 
#entre 2 y 12. sin el numero es 7 imprimir ganó 