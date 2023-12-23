#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 14:16:19 2023

@author: joao
"""

'''visualizando dados dos locais onde ocorreu um pulso de cianobacterias'''
import pandas as pd
import matplotlib.pyplot as plt

'''abrindo o arquivo contendo os dados de cobertura em porcentagem, por grupo taxonomico'''
df=pd.read_pickle("/home/joao/encontro_recifal_2024/dados/dados_completo_grupos_taxonomicos.pkl")


'''plotando cobertura de cianobacteria ao longo do tempo nos locais onde ocorreu um aumento consideravel'''
anos=['2011','2016','2017','2019','2021','2022']
plt.plot(anos,df['Frades'].loc['Cianobacteria'],label='Frades',linestyle='-')
plt.plot(anos[1:],df['Portugues'].loc['Cianobacteria'],label='Português',linestyle='--')
plt.plot(anos,df['Poste 1'].loc['Cianobacteria'],label='Poste 1',linestyle='-.')
plt.plot(anos,df['Poste 4'].loc['Cianobacteria'],label ='Poste 4',linestyle=':')
plt.plot(anos,df['Cardinal'].loc['Cianobacteria'],label ='Poste 4',linestyle=':')
plt.plot(anos,df['Cardinal N'].loc['Cianobacteria'],label ='Poste 4',linestyle=':')
plt.plot(anos,df['Alvas'].loc['Cianobacteria'],label ='Poste 4',linestyle=':')
plt.plot(anos,df['Dentao'].loc['Cianobacteria'],label ='Poste 4',linestyle=':')

plt.legend()
plt.ylabel('%')
plt.xlabel('Ano')
plt.title('Cobertura recifal de cianobactérias')