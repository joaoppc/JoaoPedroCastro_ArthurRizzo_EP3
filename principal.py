# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 18:23:43 2015

@author: João Pedro
"""

from tbm import*
from necessidade_calorica import*
arquivo = open('usuario.csv','r')
leitura1 = arquivo.readlines()[1:2]#pega somente os 2 primeiros termos
for linha1 in leitura1:
    linhas1=linha1.strip().split(',')
    x=0
    while x<1:
        nome=linhas1[0]
        idade=int(linhas1[1])
        peso=float(linhas1[2])
        sexo = linhas1[3]
        altura=float(linhas1[4])
        fator = linhas1[5]
        x+=1
        
        tmb=TMB(sexo,peso,altura,idade)
        necessidade = Necessidade_Calorica(fator,tmb)
arquivo4 = open('usuario.csv','r')
leitura4 = arquivo4.readlines()[3:10]
arquivo2 = open('alimentos.csv','r')
leitura3=arquivo2.readlines()
for linha4 in leitura4:
    linhas4=linha4.strip().split(',')
    datas = linhas4[0]
    alimentos = linhas4[1]
    quantidade = (linhas4[2])
    lista = [datas,alimentos,quantidade]
    print()
    for c in leitura3:
        linhas3=c.strip().split(',')
        key=linhas3[0]
        val=[(linhas3[1]),(linhas3[2]),linhas3[3],linhas3[4],linhas3[5]]
        if key==alimentos:
            cal = float(quantidade)/float(val[0])*float(val[1])
                   
    print(cal)
            