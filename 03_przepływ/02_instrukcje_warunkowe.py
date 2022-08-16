# -*- coding: utf-8 -*-
# %%
version = 3.7

print(version)
# %%
version > 3
version <= 3

# %% sprawdzenie dwóch wartosci - 2 znaki =

number = 1200
number > 1000

number == 1200
number == 1201

number != 1200

number != 1201

# %%

# if [warunek]:
#    [instrukcje]

# %%
if 8 < 10:
    print('Zgadza sie')
    
# %%
a = 18
if a < 10:  
    print('tak')
else:
    print('nie')    

# %%

age = 12
if age < 18:
    print('nie masz uprawnień')
else:
    print('masz dostęp')

# %%

age = 21
if age == 18:
    print('Masz 18 lat')
elif age < 18:
    print('nie masz uprawnień')
    # elif age > 18 - zadziała jak else poniżej ale jest bardziej czytelny
else:
    print('masz uprawnienia')
# %%

age = int(input('Podaj swój wiek: '))
if age == 18:
    print('Masz 18 lat')
elif age < 18:
    print('nie masz uprawnień')
    # elif age > 18 - zadziała jak else poniżej ale jest bardziej czytelny
else:
    print('masz uprawnienia')

# %%