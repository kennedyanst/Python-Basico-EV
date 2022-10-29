# Criando o arquivo para escrita
arquivo = open("arqText.txt", "w")

arquivo.write("Curso de Python da Fundação Bradesco | Escola Virtual \n")
arquivo.write("Aula Prática")
arquivo.close()

# Abrindo o arquivo para leitura
leitura = open("arqText.txt", "r")
print(leitura.read())
leitura.close()