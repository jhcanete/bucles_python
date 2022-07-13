# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Realice una calculadora:
Dentro de un bucle se debe ingresar por línea de comando dos números
Luego se ingresará como tercera entrada al programa el símbolo de la operación
que se desea ejecutar:
- Suma (+)
- Resta (-)
- Multiplicación (*)
- División (/)
- Exponente/Potencia (**)
Se debe efectuar el cálculo correcto según la operación ingresada por consola
Imprimir en pantalla la operación realizada y el resultado

El programa se debe repetir dentro del bucle hasta que como operador
se ingrese la palabra "FIN", en ese momento debe terminar el programa

Se debe debe imprimir un cartel de error si el operador ingresado no es
alguno de lo soportados o no es la palabra "FIN".
'''






while True:
    print("ingrese numero entero: ")
    numero1 = int(input())
    print("ingrese otro numero entero: ")
    numero2 = int(input())
    print("ingrese el tipo de operacion a realizar(+,-,*,/,**, o fin para terminar): ")
    operacion = input()
    resultado = 0 
    if operacion == "+" or operacion == "-" or operacion == "*" or operacion == "/" or operacion == "**" or operacion == "fin":
        if operacion == "+":
            resultado = numero1 + numero2
            print("el resultado es: ", resultado)
        elif operacion == "-":
            resultado = numero1 - numero2
            print("el resultado es: ", resultado)
        elif operacion == "*":
            resultado = numero1 * numero2
            print("el resultado es: ", resultado)
        elif operacion == "/":
            resultado = numero1 / numero2
            print("el resultado es: ", resultado)
        elif operacion == "**":
            resultado = numero1 ** numero2
            print("el resultado es: ",resultado)
        elif operacion == "fin":
            print("fin del programa")
            break
        else:
            print("error ingrese valor correcto")
print("Mi Calculadora (^_^)")
# Empezar aquí la resolución del ejercicio
