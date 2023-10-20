impares = open("impares.txt", "w")

pares = open("pares.txt", "w")

for i in range(1000):
    if i % 2 == 0:
        pares.write(f",{i}")
    else:
        impares.write(f"{i} \n")

pares.close()
impares.close()