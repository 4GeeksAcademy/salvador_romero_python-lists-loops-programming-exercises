# Remember to import random function here
import random
my_list = [4, 5, 734, 43, 45]

# The magic goes below
for i in range(10):
    numero_aleatorio = random.randint(1,11)
    my_list.append(numero_aleatorio)

print(my_list)