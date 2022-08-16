for i in range(10):
    if i == 6:
        continue
    print(i)

# %%
for ii in range(20):
    if ii % 2 == 0:
        continue
    print(ii)

# %%
for iii in range(20):
    if iii % 2 == 1:
        continue
    print(iii)
# %%
sample = 'Python Course'
for char in sample:
    if char == ' ':
        continue
    print(char)

# %%
hashtags = 'summer#holiday#free'
result = ''
for char in hashtags:
    if char =='#':
        print(result)
        result = ''
        continue
    result = result + char
print(result)