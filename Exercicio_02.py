pares = open("numeros2.txt", "r")
soma = 0

for linha in pares.readlines():
    linha_separada = linha.split(" ")

    for i in linha_separada:
        soma += int(i)

print(soma)
