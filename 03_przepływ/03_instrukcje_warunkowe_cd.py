# -*- coding: utf-8 -*-

print('Program uruchomiony...')
print("""Włam się do systemu, zgadująć dwucyfrowy PIN.
Numer PIN składa się z cyfr 0, 1, 2.""")
pin = input('Wprowadź numer PIN: ')

if pin == '21':
    print('BRAWO! Złamałes system')
elif pin == '20':
    print('Trochę za mało')
elif pin == '22':
    print('Trochę za dużo')
else:
    print('Nie trafiłes')
# %%

    print('Program uruchomiony...')
    print("""Włam się do systemu, zgadująć dwucyfrowy PIN.
    Numer PIN składa się z cyfr 0, 1, 2.""")
    pin = int(input('Wprowadź numer PIN: '))

    if pin == 21:
        print('BRAWO! Złamałes system')
    elif pin == 20:
        print('Trochę za mało')
    elif pin == 22:
        print('Trochę za dużo')
    else:
        print('Nie trafiłes')
# %%
string = ''
if string:
    print('Niepusty')
else:
    print('Pusty')
# %%
number = 1
if number:
    print('liczba niezerowa')
else:
    print('Zero')
# %%
default_flag = False

if default_flag:
    print('Doszło do defaultu')
else:
    print('Nie doszło')
# %%
default_flag = False

if not default_flag:
    print('Nie doszło')
else:
    print('Doszło do defaultu')
# %%
saldo = 10000
klient_zwer = True

if saldo > 0 and klient_zwer:
    print('możesz wyplacic')
else:
    print('nie możesz')
# %%
saldo = 10000
klient_zwer = True
amount = int(input('ile chcesz? '))
if saldo > 0 and klient_zwer and saldo >= amount:
    print('możesz wyplacic')
else:
    print('nie możesz. '
          'Brakuje ci {}'.format(abs(saldo - amount)))
# %%
name = 'Python'
if 'Po' in name:
    print('znaleziono')
else:
    print('nie znaleziono')
# %%
tech = 'Python'
'dobry wybor' if tech == 'Python' else 'Poszukaj czegos innego'
