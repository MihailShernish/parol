import random

 

rp = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

 

pas = int(input('введи длинну пароля: '))

 

finalpas = ''

 

for i in range(pas):

    finalpas += random.choice(rp)

print(finalpas)