import sys
from passwordcheck import CreatePassword
length = int(sys.argv[1])
path = sys.argv[2]
number = int(sys.argv[3])
password = CreatePassword()
for i in range(number):
    password.generator(length,path)