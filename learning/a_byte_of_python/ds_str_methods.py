# This is a string object
name = 'Syrakushaikh'

if name.startswith('Syr'):
    print('Yes, the string starts with "Syr".')

if 'a' in name:
    print('Yes, it contains the string "a".')

if name.find('sha') != -1:
    print('Yes, it contains the string "sha".')

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))
