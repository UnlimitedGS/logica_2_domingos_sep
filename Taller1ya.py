#Parte A: for, range, contadores y acumuladores

#Contar del 1 al 10

for i in range(1, 11):
    print(i, end=" ")
print()
print()

#Cuenta regresiva con for

for i in range (10, 0, -1):
     print(i, end=" ")
print()
print()

#Suma 1...100

suma = 0
for i in range(1, 101):
    suma = suma + i
print(f'La suma de los numeros del 1 al 100 es: {suma}')
print()

#Pares 1...20 (con continue)

for i in range(1, 21):
    if i % 2 != 0:
        continue
    print(i, end=" ")
print()
print()

#Tabla del 7

n = 7
for i in range(1, 11):
    print(f'{n} x {i} = {n*i}')
print()

#Promedio de N numeros 

N = int(input('Pon solo numeros enteros porfavor: '))
acum = 0
for i in range(N):
    x = float(input(f'ponga un numero pues:'))
    acum = acum + x
prom = acum / N
print(f' El promedio es: {prom}')
print()

#Parte B while, sentinelas, banderas, validación

#cuenta regresiva con while

n = int(input('ingrese un numero para hacer cuenta regresiva: '))
while n > 0:
    print(n, end=" ")
    n = n - 1
print()
print()

#Suma hasta 0 (sentinela)

cantidad = 0
total = 0

monto = float(input('ingrese un monto (0 para terminar): '))
while monto != 0:
    cantidad = cantidad + 1
    total = total + monto
    monto = float(input('ingrese un monto (0 para terminar): '))

print(f'la cantidad de montos ingresados es: {cantidad}')
print(f'el total de los montos ingresados es: {total}')
print()

#Validacion simople de nota

nota = float(input('ingrese una nota entre 0 y 5: '))
while nota < 0 or nota > 5:
    print('nota invalida, intente de nuevo')
    nota = float(input('ingrese una nota entre 0 y 5: '))
print(f'nota valida: {nota}')
print()

#Bandera de busqueda

encontrado = False

nombre = input('ingrese un nombre (ENTER para terminar): ')
while nombre != "":
    if nombre[0].upper() == 'A':
        encontrado = True
    nombre = input('ingrese un nombre (ENTER para terminar): ')
    
if encontrado:
    print('se encontro al menos un nombre que empieza con A')
else:
    print('no se encontro ningun nombre que empiece con A')
print()

# Menu basico (while true + break)

total = 0

while True:
    print('\nMenu')
    print('1. Ingresar un monto')
    print('2. Mostrar total')
    print('3. Salir')
    
    opcion = input('ingrese la opcion: ')
    
    if opcion == '1':
        monto = float(input('ingrese un monto: '))
        total = total + monto
    elif opcion == '2':
        print(f'el total acumulado es: {total}')
    elif opcion == '3':
        print('saliendo del programa...')
        break
    else:
        print('opcion invalida, intente de nuevo')
    print()

# MInimo y Maximo (sentinela vacio)

num = []

while True:
    dato = input('ingrese un numero (ENTER para terminar): ')
    if dato == '':
        break   
    try:
        numero = float(dato)
        num.append(numero)
    except ValueError:
        print('dato invalido, intente de nuevo')

if len(num) > 0:
    print(f'el numero minimo es: {min(num)}')
    print(f'el numero maximo es: {max(num)}')
else:
    print('no se ingresaron numeros')
print()