# -*- coding: utf-8 -*-

KOD_PIN = '0000'

pin = input('Podaj kod: ')
while pin != KOD_PIN:
    pin = input('Jeszcze raz: ')
print('Kod OK')

# %%

KOD_PIN = '0000'
counter = 0

pin = ''

while pin != KOD_PIN and counter < 3:
    pin = input('Podaj PIN: ')
    if pin == KOD_PIN:
        print("Zalogowany")
        break
    counter += 1
else:
    print('za dużo prób')