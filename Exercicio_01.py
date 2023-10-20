pares = open("pares.txt", "r")
invertido = open("invertido.txt", "w")

teste = pares.readlines()

teste.reverse()

for linha in teste:
    invertido.write(f"{linha}")

invertido.close()
pares.close()


    