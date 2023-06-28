# Variables

variable = "Hello World!"
numero = 10
decimal = 10.5
booleano = True

# strings 

texto = "Hello World!"
print(texto)  #metodo print
print(texto[0]) #imprime la letra en la posicion 0
print(texto.upper()) #imprime el texto en mayusculas
print(texto.find("World")) #imprime la posicion de la palabra World
print(texto.replace("World", "Mundo")) #reemplaza la palabra World por Mundo
print(texto.split(" ")) #divide el texto en una lista
print("Hello" in texto) #imprime True si la palabra Mundo esta en el texto

# arithmetic operators

print(10 + 5) #suma
print(10 - 5) #resta
print(10 * 5) #multiplicacion
print(10 / 5) #division
print(10 % 5) #modulo
print(10 ** 5) #potencia
print(10 // 5) #division entera

# comparation operators

n1 = 10
n2 = 20

print(n1 == n2) #igualdad
print(n1 != n2) #desigualdad
print(n1 > n2) #mayor que
print(n1 < n2) #menor que
print(n1 >= n2) #mayor o igual que
print(n1 <= n2) #menor o igual que

# logical operators

n1 = 10
n2 = 20

print(n1 == n2 and n1 != n2) #and
print(n1 == n2 or n1 != n2) #or
print(not(n1 == n2 and n1 != n2)) #not

# if statement

n1 = 10
n2 = 20

if n1 == n2:
    print("Son iguales")
elif n1 != n2:
    print("Son diferentes")
else:
    print("No se que son")

# while loop

i = 1

while i <= 10:
    print(i)
    i += 1

# for loop

for i in range(1, 11):
    print(i)

#input

nombre = input("Ingrese su nombre: ")
print("Hola " + nombre)

#convert

n1 = "10"
n2 = "20"

print(int(n1) + int(n2))
print(float(n1) + float(n2))
print(str(n1) + str(n2))
print(bool(n1))
print(bool(False))
print(bool(0))
print(bool(""))
print(bool(None))

## Ejercicio: conversor de celcius a fahrenheit

# lists

lista = ["Hola", 10, 10.5, True]
print(lista)
print(lista[0])
print(lista[1:3])
print(lista[1:])
print(lista[:3])
print(lista[-1])
print(lista[-3:-1])
print(len(lista))
lista[0] = "Hello"
print(lista)
lista.append("Mundo")
print(lista)
lista.insert(1, "Hello")
print(lista)
lista.remove("Hello")
print(lista)
lista.pop()
print(lista)
del lista[0]
print(lista)
lista.clear()
print(lista)
del lista

lenguajes = ["Python", "Java", "JavaScript"]

i=0
while i < len(lenguajes):
    print(lenguajes[i])
    i += 1

for i in range(len(lenguajes)):
    print(lenguajes[i])

for i in lenguajes:
    print(i)

