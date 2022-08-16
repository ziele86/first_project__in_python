# -*- coding: utf-8 -*-

empty_tuple = tuple()
print(empty_tuple)

# %%
amazon = ('Amazon', 'USA', 'technology', 1)
google = ('Google', 'USA', 'technology', 2)

name_google = google[0]
google[0] = 'Google Com'

# %%
data = (amazon, google)
print(data)

# %%
a = ('Piotr', 'Zieliński')
print(a)

# %%
imie = 'Piotr'
nazwisko = 'Zieliński'

# %%
imie, nazwisko, id_user = ('Piotr', 'Zieliński', '001')

# %%
amazon_name, country, sector, rank = amazon

# %%
nested = 'Europa', 'Polska', ('Poznań', 'Warszawa')
print(nested)

# %%
a = 12
b = 15
c = b
b = a
a = c

print(a, b)

# %%

x, y = 10000, 20
x, y = y, x
print(x, y)
