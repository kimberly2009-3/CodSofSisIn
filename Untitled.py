#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class clase1:
    pass
class clase2(clase1):
    pass
class clase3(clase2):


# In[5]:


class abuelo:
    pass
class padre(abuelo):
    pass
class madre:
    pass
class hijo(madre,padre):
    pass
print(hijo.__mro__)

