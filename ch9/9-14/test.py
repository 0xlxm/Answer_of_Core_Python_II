import sys
a = sys.argv[1:]
b = ''.join(a)
print b.replace('^', '**')
print b
