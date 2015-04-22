# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 15:33:45 2015

@author: João Pedro
"""

arquivo2 = open('alimentos.csv','r')
leitura3=arquivo2.readlines()

lista_alimentos=dict()
for c in leitura3:
    linhas3=c.strip().split(',')
    key=linhas3[0]
    val=[linhas3[1],linhas3[2],linhas3[3],linhas3[4],linhas3[5]]
   
    lista_alimentos={key:val}
    print(lista_alimentos)