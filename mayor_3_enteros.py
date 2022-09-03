# Instrucciones Condicionales

##Caso No. 2: Hallar el mayor entero de tres numeros enteros


print("------------------------------")
print("----HALLAR EL MAYOR ENTERO----")
print("------------------------------")

# input
a = int(input("Digite el primer número: "))
b = int(input("Digite el segundo número: "))
c = int(input("Digite el tercer número: "))

# processing

if a>b:
    if a>c:
        mayor = a
    else: 
        mayor = c
    
else:
    if b>c:
        mayor = b
    else:
        mayor = c

#output

print("-----------------------------")
print("---------RESULTADOS----------")
print("-----------------------------")

print("El mayor entero entre " + str(a) + ", "+ str(b) + " y " + str(c) + " es: " + str(mayor))
