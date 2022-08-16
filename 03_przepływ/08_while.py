# -*- coding: utf-8 -*-

i = 0
while i < 15:
    print(i)
    i = i + 1

# %%
n = 0
while True:
    print(n)
    if n >= 10:
        break            
    n = n + 1

# %%
while True:
    name = input('Podaj imię: ')
    if len(name) >= 3 and name.isalpha():
        break
print('Czesc {}' .format(name))
# %%
m = 0

while m < 20:
    m = m + 1
    if m % 2 == 0:
        continue
    print(m)

# %%
lista = [12, 21, 35, 45, 64]
flaga = False
wartosc = 45

idx = 0
while idx < len(lista):
    if lista[idx] == wartosc:
        flaga = True
        break
    idx += 1
if flaga:
    print('Znaleziono {}' .format(wartosc))

# %%
lista = [12, 21, 35, 45, 64]
flaga = False
wartosc = 450

idx = 0
while idx < len(lista):
    if lista[idx] == wartosc:
        flaga = True
        break
    idx += 1
if not flaga:
    lista.append(wartosc)
    
