# -*- coding: utf-8 -*-

for i in '0123456789':
    i = int(i)
    print(i)
    if i == 6:
        break
print('koniec')

# %%
sample = 'Python Course'

for ii in sample:
    if ii == ' ':
        break
    print(ii)
    
# %%
for char in 'ziele86@gmail.com':
    if char == '@' :
        print('adres zweryfikowany')
        break
else:
    print('adres nieprawidłowy')
    
print('KONIEC')