# Time-stamp: <2016-03-15 Tue 18:24:57 Shaikh>
# -*- coding: utf-8 -*-
try:
    text = input('Enter something --> ')
except EOFError:
    print('Why did you do an EOF on me?')
except KeyboardInterrupt:
    print('You canceled the operation.')
else:
    print('You entered {}'.format(text))
