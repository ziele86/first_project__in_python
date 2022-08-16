# -*- coding: utf-8 -*-
"""
Created on Tue May 31 16:49:19 2022

@author: Piotr
"""


print(10 / 3)

print((10 - 2 ** 3) * 10)
# %%
a = 10
b = 20
c = a + b
print(c)
# %%
print('love python')
print('Python\n3.7')
# %%
print('\tPython')
print('\t\tPython')
print('\t\t\tPython')

print('c:\path\to\something\new')
print(r'c:\path\to\something\new')
# %%
import os
os.getcwd()

# %%
name = 'Pythonn'

print(name + '3.7')

print(name, '3.7')
# %%
age = 35
imie = 'Piotr'
nazwisko= 'Zieliński'

print(imie + ' ' + str(age))
print('{1} {0} ma {2} lat.'.format(imie, nazwisko, age))


print('{} {} ma {} lat.'.format(imie, nazwisko, age))

nazwa = imie + nazwisko
print(nazwa)
# %%
saldo = 45
print(saldo)
saldo = saldo + 50
print(saldo)
# %%
lokata = 1000
czynnik_akum = lokata * 0.04
lokata_rok = lokata + czynnik_akum

print('Wartość lokaty dzisiaj:', lokata)
print('Wartość lokaty po roku:', lokata_rok)
# %%
sal = 50 
sal = sal + 20

sal -= 32
print(sal)
sal +=19.5
print(sal)
# %%
pixel = 150

'''pixel = 150 / 255'''
pixel /= 255

print(pixel)

# %%
base = 2
base = base **5
print(base)
base5 = 5
base5 **= 5
print(base5)
# %%
x = 103
x = x % 10
print(x)

y = 104
y %= 10
print(y)
# %%
name = 'Python'
version = ' 3.7'

name += version
print(name)
# %%

