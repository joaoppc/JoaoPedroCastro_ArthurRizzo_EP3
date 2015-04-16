# -*- coding: utf-8 -*-
arquivo = open('usuario.csv','r')
leitura = arquivo.readlines()[:2]#pega somente os 2 primeiros termos
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
    #nome+dict()
    #nome=[fulano]:30,70,m,1.64....
    #nome[1]= 70
            