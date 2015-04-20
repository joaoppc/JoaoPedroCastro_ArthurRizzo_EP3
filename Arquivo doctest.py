# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 23:48:36 2015

@author: lvrizzo
"""


import doctest 


def esvazia_lista(lista):
    lista.clear()


def soma(a,b):
    return a+b

if __name__=="__main__":
    doctest.testmod(verbose="True")