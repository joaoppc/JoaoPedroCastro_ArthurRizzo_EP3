# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 16:46:56 2015

@author: lvrizzo
"""

fator_atividade={"minimo":1.2,"baixo":1.375,"medio":1.55,"alto":1.725,"muito alto":1.9}
def necessidade_calórica(fator_atividade):
    for exercicio in fator_atividade:
        if exercicio== 0 or exercicio== "nenhuma" or exercicio=="nenhum" :
            fator_atividade.pop["minimo"]*tbm
        elif exercicio == 1 or exercicio== "baixo" or exercicio=="pouca":
            fator_atividade.pop["baixo"]*tmb
        elif exercicio == 2 or exercicio == "medio" or exercicio == "bom":
            fator_atividade.pop["medio"]*tmb
        elif exercicio == 3 or exercicio == "alto" or exercicio == "muito bom":
            fator_atividade.pop["alto"]*tmb
        elif exercicio == 4 or exercicio == "muito alto" or exercicio =="monstro" or exercicio == "atleta":
            fator_atividade.pop["muito alto"]*tmb
            
        