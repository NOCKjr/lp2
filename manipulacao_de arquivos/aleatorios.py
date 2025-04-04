import random
with open('pares.txt', 'w') as pares:
    with open('impares.txt', 'w') as impares:
        for i in range(1, 101):
            x = random.randint(1, 10000)
            if x%2 == 0:
                pares.write(f'{x}\n')
            else:
                impares.write(f'{x}\n')
