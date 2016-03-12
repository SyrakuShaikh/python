# Time-stamp: <2016-03-12 Sat 09:53:02 Shaikh>
import os

# traverse root directory, and list directories
# as dirs and files as files
for root, dirs, files in os.walk('.'):
    path = root.split('/')
    print((len(path) -1 ) * '---|',
          os.path.basename(root))
    for file in files:
        print(len(path) * '---|', file)
