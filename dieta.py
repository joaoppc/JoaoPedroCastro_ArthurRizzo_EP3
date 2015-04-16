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
        leitura2=arquivo.readlines()[3:10]
for linha2 in leitura2:
    linhas2=linha2.strip().split(',')
    z=0    
    while z<1:
        
<<<<<<< Updated upstream
        data = linhas2[0]
        alimento=linhas2[1]
        quantidade=linhas2[3]
        z+=1
        print(linhas2)
        
        #for j in linhas:
         #   palavras=j.strip().split(',')
          #  print(palavras)
=======
        for j in linhas:
            palavras=j.strip().split(',')
            print(palavras)
            """isso é só a ideia"""
>>>>>>> Stashed changes
    #nome+dict()
    #nome={fulano}:30,70,m,1.64.... 
    #nome[1]= 70
