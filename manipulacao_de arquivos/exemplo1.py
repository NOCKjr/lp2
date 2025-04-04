arquivo = open('exemplo1.txt', 'w')
for i in range(5):
    arquivo.write(f'Hello world {i}\n')
arquivo.close()
leitura = open('exemplo1.txt')
linha = leitura.readline()
while linha!='':
    print(linha, end='')
    linha = leitura.readline()
leitura.close()