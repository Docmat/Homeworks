a = {1 : 'one',
     2 : 'two',
     3 : 'three',
     4 : 'four'}
print(a)
b = a.items()
print(b)
b = {}
for key, value in a.items():
    b[value] = key
print(b)
