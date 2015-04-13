# -*- coding: utf-8 -*-
arquivo = open('usuario.csv','r')
leitura = arquivo.readlines()
for linha in leitura:
    linhas=linha.strip().split(',')
    for j in linhas:
        palavras=j.strip().split(',')