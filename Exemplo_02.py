multi4 = open("multi4.txt", "w")

pares = open("pares.txt", "r")

for linha in pares.readlines():
    if int(linha) % 4 == 0:
        multi4.write(f"{linha} \n")

pares.close()
multi4.close()