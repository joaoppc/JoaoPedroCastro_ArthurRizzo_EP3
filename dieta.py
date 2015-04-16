# -*- coding: utf-8 -*-
arquivo = open('usuario.csv','r')
leitura = arquivo.readlines()[:2]
for linha in leitura:
    linhas=linha.strip().split(',')
    x=0
    while x<1:
        cadastro=linhas[0]
        x+=1
        print(cadastro)
        
        for j in linhas:
            palavras=j.strip().split(',')
            print(palavras)
    