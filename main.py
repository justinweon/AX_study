#from chapter06.utils.sub import mod3

#mod3.print_version()
import sys

print(sys.argv)

_, a, b, c = sys.argv
print(type(b))

print(int(a) + int(b) + int(c))