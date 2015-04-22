# -*- coding: utf-8 -*-

arquivo = open('usuario.csv','r')
leitura1 = arquivo.readlines()[1:2]#pega somente os 2 primeiros termos
for linha1 in leitura1:
    linhas1=linha1.strip().split(',')
    x=0
    while x<1:
        nome=linhas1[0]
        idade=linhas1[1]
        peso=linhas1[2]
        sexo = linhas1[3]
        altura=linhas1[4]
        fator = linhas1[5]
        x+=1
        print(nome,idade,peso,sexo,altura,fator)

