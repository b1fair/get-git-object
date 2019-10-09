#!/usr/bin/python
# Dump a github object to stdout
# Brian Fair <blfair@gmail.com>, https://github.com/b1fair

import sys, zlib 

print(zlib.decompress(open(sys.argv[1], 'rb').read()))
