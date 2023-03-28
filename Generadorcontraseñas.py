import random
minu = "abcdefghijklmnñopqrstuvwxyz"
mayu = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
nume = "1234567890"
simbo = "[]{}()*;/,._-"
all = minu + mayu + nume + simbo
length = 12 
contraseña = "".join(random.sample(all,length))
print(contraseña)