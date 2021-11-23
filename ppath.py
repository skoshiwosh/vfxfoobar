'''
Nice print of system PATH environment variable

@author: Suzanne Berger
'''

import sys
import os

# main
if __name__ == '__main__':
    print 'System PATH Environment Variable'
    if os.environ['PATH']:
        pathlist = os.environ['PATH'].split(';')
        for each in pathlist:
            print '%s' % each
            

