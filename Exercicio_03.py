arquivo = open("numeros3.txt", "r")

teste = arquivo.readlines()

def lista_num(valor):
    num = []

    for linhas in valor:
        linha_separada = linhas.split(" ")
        num.append(linha_separada[:])

    return num

def unicos(lista):
    unicos = []

    for i in lista:
        unicos.append(lista[i][i])

num = lista_num(teste)

unicos(num)