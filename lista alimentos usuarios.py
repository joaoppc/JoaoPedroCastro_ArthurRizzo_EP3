# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 16:28:31 2015

@author: João Pedro
"""
from datetime import *
arquivo4 = open('usuario.csv','r')
leitura4 = arquivo4.readlines()[3:10]#pega somente os 2 primeiros termos
for linha4 in leitura4:
    linhas4=linha4.strip().split(',')
    datas = linhas4[0]
    alimentos = linhas4[1]
    quantidade = linhas4[2]
    d = datetime.strptime(datas,"%d/%m/%Y")
    print(d)  
