#kimberly cherlyn garcia castro
#2-j
#practica10
#4/03/25


#!/usr/bin/env python
# coding: utf-8

# In[5]:


def factorial (n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n -1)
num =int(input("introduce un numero para calcular su factorial:"))
if num< 0:
    print("El factorial no esta definido para numeros negativos.:")
else:
    result =factorial(num)
    print(f"El factorial de {num} es {result}.")


# In[7]:


def suma_digitos(numero):
    suma = 0
    while numero > 0:
        suma += numero % 10
        numero //= 10
    return suma
num =int(input("introduce un numero para calcular la suma de sus digitos:"))
resultado =suma_digitos(num)
print(f"La suma de los digitos de {num} es {resultado}.")


# In[4]:


def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
num1=int(input("introduce el primer numero: "))
num2=int(input("introduce el segundo numero: "))
if num1 > num2:
    num1, num2 = num2, num1s 
print(f"Los numeros primos  entre {num1} y {num2} son:")
for num in range(num1, num2 +1):
    if es_primo(num):
        print(num)

    


# In[8]:


n = int(input("introduce un numero:"))
for i in range (1, n + 1):
    linea =''.join(str(x) for x in range (1, i + 1))
    print(f"#{linea}")

