age = 20
name = 'Shaikh'


print('{0} was {1} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))

# Omit the index in '{}'
print('{} was {} years old when he wrote this book'.format(name, age))
print('Why is {} playing with that python?'.format(name))

# More detailed specifications
# decimal (.) precision of 3 for float '0.333'
print('{0:.3f}.format(1.0/3) '+'{0:.3f}'.format(1.0/3))
print('{0:.3f}.format(1/3) '+'{0:.3f}'.format(1/3))
# fill with underscores (_) with the text centered
# (^) to 11 width '___hello___'
print('11 {0:_^11}'.format('hello'))
print('15 {0:_^15}'.format('hello'))
print('16 {0:_^16}'.format('hello'))
# keyword-based 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))

# print without the default '\n'
print('a', end='')
print('b', end='')
print()
print('a', end=' ')
print('b', end=' ')
print('c')

# Escape sequence '\'
print('\ ')
print('\'')
print('This is the first line\nThis is the second line')
print("This is the first sentence. \
This is the second sentence.")
print(r"Newlines are indicated by \n")
