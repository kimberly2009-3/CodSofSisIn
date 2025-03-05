#kimberly cherlyn garcia castro
#2-j
#4/03/25

#!/usr/bin/env python
# coding: utf-8

# In[9]:


porcentaje=float(input("intoduce el porcentaje del alumno"))
if porcentaje>90:
    grado='A'
    print(f"el grado del alumno es:{grado}")
elif porcentaje >=80 and porcentaje <=90:
    grado ='B'
    print(f"El grado del alumno es:")
elif porcentaje >=60 and porcentaje<= 80:
    grado = 'c'
    print(f"El grado del alumno es:{grado}")
else:
    grado ='D'
print(f"El grado del alumno es :{grado}")


# In[13]:


año=float(input("ingresa el año que deseas consultar si es biciesto"))
if(año%4== 0 and (año % 100 != 0 or año % 400 ==0)):
    print(f"El año{año} es biciesro.")
else:
    print(f"el año {año} no es biciesto. ")


# In[17]:


numero = int(input("ingresa un numero del  1 al 7:"))
dias ="domingo","lunes","martes","miercoles","jueves","viernes","sabado"
if 1<=numero <= 7:
    print(f"el dia {numero} es {dias[numero]}")
else:
    print("numero fuera de negro.ingesa un numero entre 1 y 7.")


# In[ ]:




