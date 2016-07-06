#!/bin/python

import os
import time

# def robert(user):
loc = '/home/{}/log' .format('icadi')

for fpath in os.listdir(loc):
    print('Checking {}' .format(fpath))
    fpath = os.path.join(loc, fpath)

    try:
         with open(fpath) as fhandle:
             for l in fhandle:
                  print(l)
                  time.sleep(0.2)
    except IsADirectoryError:
         print('{} is a directory' .format(fpath))
         pass
