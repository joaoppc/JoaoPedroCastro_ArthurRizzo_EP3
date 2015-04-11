# -*- coding: utf-8 -*-

def Necessidade_Calorica(fator,tmb):
    if fator=='minimo':
        necessidade = tmb*1.2
    elif fator=='baixo':
        necessidade = tmb*1.375
    elif fator=='medio':
        necessidade = tmb *1.55
    elif fator=='alto':
        necessidade = tmb*1.725
    elif fator=='muito alto':
        necessidade = tmb*1.9
    return necessidade