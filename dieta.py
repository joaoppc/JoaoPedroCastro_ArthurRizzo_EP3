# -*- coding: utf-8 -*-
arquivo = open('usuario.csv','r')
leitura = arquivo.readlines()
for linha in leitura:
    palavra=linha.strip().split(',')
    print(palavra)
