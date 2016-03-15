# Time-stamp: <2016-03-15 Tue 19:11:36 Shaikh>
# -*- coding: utf-8 -*-
import sys
import time


f = None
try:
    f = open("poem.txt")
    # Our usual file-reading idiom
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='', flush=True)
        # sys.stdout.flush()
        print('Press ctrl+c now')
        # To make sure it runs for a while
        time.sleep(2)
except IOError:
    print("Could not find file 'poem.txt'")
except KeyboardInterrupt:
    print("!! You canceled the reading from the file.")
finally:
    if f:
        f.close()
    print("(Cleaning up: Closed the file)")
