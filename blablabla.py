# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 17:43:46 2022

@author: Piotr
"""

name = input('Jak masz na imię? ')
age = int(input('Ile masz lat? '))
weight = int(input('Ile ważysz? '))

print('Więc masz na imię {},'.format(name), 'masz {}'.format(age), 'lat, ' 
      'ważysz {}' .format(weight), 'kilo')

# %%
title = 'Kalkulator napiwku'
print(title.upper())
rachunek = float(input('Podaj kwotę rachunku: '))
napiwek = int(input('Ile procent chcesz dać napiwku? '))
suma = float(rachunek + rachunek * napiwek / 100)
print('W sumie zapłacisz', suma, 'zł.')