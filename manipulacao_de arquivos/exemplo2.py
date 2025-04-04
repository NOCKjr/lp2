with open('exemplo1.txt') as leitura:
    conteudo = leitura.readline()
    while conteudo!='':
        print(conteudo, end='')
        conteudo = leitura.readline()