# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 20:43:51 2015

@author: lvrizzo
"""
from datetime import *

d1 = datetime(2015, 2, 1)
d2 = datetime(2015, 1, 31)
d3 = datetime.strptime("02/13/2015" , "%m/%d/%Y")
d4 = datetime.strptime("17/01/2015","%d/%m/%Y")

dias = [d1, d2, d3, d4]
dias_ordenados = sorted(dias)

print ("Datas na ordem da lista dias")
for d in dias : 
    print(d)

print("Datas na lista dias_ordenados")
for d in dias_ordenados:
    print(d)

#A sbtração de dois dias resulta numa variável do tipo !!timedeslta!!
delta = d1 - d2 

#a propriedade days de um timedelta dáa diferença em dias daquelas duas datas
print(delta.days)

dia_inicial = dias_ordenados[0]

dias_numerados = []
for d in dias_ordenados: 
    delta = d - dia_inicial
    dias_numerados.append(delta.days)
    
print ("Dias como inteiros a partir da primeira data")
print (dias_numerados)


