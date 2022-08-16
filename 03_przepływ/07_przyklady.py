# -*- coding: utf-8 -*-
raw_data = '345!23!3234!43434'
result = ''

# for i in raw_data:
#     if i == '!':
#         print(result)
#         result = ''
#         continue
#     result = result + i
# print(result)
        

# for i in raw_data:
#     if i != '!':
#         result = result + i
#     else:
#         result = result + ', '
# print(result)
    

# %%

for char in raw_data:
    if char != '!':
        result += char
    else:
        result += ', '
print(result)
    

# %%
suma = 0
for i in range(10):
    suma = suma + i
print(suma)

# %%
saldo = 450
print('Saldo początkowe: {}' .format(saldo))
for kwota in range(10, 60, 10):
    print('Wypłacona kwota: {}' .format(kwota))
    saldo -= kwota #odejmuje prawą stronę od lewej i przypisuje wynik do lewej
    print('Saldo {}' .format(saldo))
print('Saldo końcowe {}' .format(saldo))

# %%
print('Witaj w systemie logowania')
print('*' * 30)

nick = input('Podaj nick: ')
pin = input('Podaj pin, {}: ' .format(nick))

if len(pin) == 4:
    for char in pin:
        if char not in '0123456789':
            print('PIN niepoprawny')
            break
    else:
        print('Kod poprawny')
else:
    print('PIN niepoprawny')
