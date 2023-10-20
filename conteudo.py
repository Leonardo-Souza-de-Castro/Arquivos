# Com o comando open informamos ao python qual arquivo deve ser aberto ou criado e como vamos utilizar esse arquivo (nos casos do r o arquivo já deve existir).
# OBS: O nome do arquivo deve contar todo o caminho para o arquivo caso não esteja na pasta raiz do projeto.
arquivo = open("teste2.txt", "w")

# Com o comndo write escrevemos no arquivo que escolhemos
# OBS 2: Devemos indicar com \n sempre que devemos pular de linha, se não o arquivo vai escrever tudo em uma linha só.
arquivo.write("funciona")

# Aqui indicamos que o arquivo será fechado e salvara o que foi escrito.
arquivo.close()