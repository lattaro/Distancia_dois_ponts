import math

num_1 = input("Digite o primeiro número")
num_2 = input("Digite o segundo número")
num_3 = input("Digite o terceiro número")
num_4 = input("Digite o quarto número")

num_int_1 = int (num_1)
num_int_2 = int (num_2)
num_int_3 = int (num_3)
num_int_4 = int (num_4)

dist = math.sqrt (((num_int_1 - num_int_3)**2) + ((num_int_2 - num_int_4)**2))

if (dist >= 10):
    print("longe")
else:
    print("perto")