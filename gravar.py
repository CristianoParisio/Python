arquivo = open('gravar.txt', 'w')

arquivo.write('Curso Python ensinando como criar arquivos textos \n')
arquivo.write('Aula Pratica - Gerando um arquivo txt com conteudo \n')
arquivo.write('Arquivo gerado atraves do programa gravar.py \n')
arquivo.write('Executado no console')

arquivo.close()



# Leitura do arquivo Texto

leitura=open('gravar.txt', 'r')
print(leitura.read())
leitura.close()
