#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 17:33:13 2023

@author: joao
"""
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols
import numpy as np


df=pd.read_csv('/home/joao/encontro_recifal_2024/dados/cianobacteria.csv')
df['Ano'] = df['Ano'].astype('category')
df['Local'] = df['Local'].astype('category')

'''anova de dois fatores'''
modelo = ols('Cianobacteria ~ C(Ano) + C(Local)', data=df).fit()
resultado_anova = sm.stats.anova_lm(modelo, typ=3)

print(resultado_anova)

anova_table = sm.stats.anova_lm(modelo, typ=2)

# Exibindo a tabela ANOVA
print(anova_table)

'''anova de um fator '''
modelo = ols('Cianobacteria ~ Ano', data=df).fit()
anova_tabela = sm.stats.anova_lm(modelo)

# Exibir a tabela ANOVA
print(anova_tabela)


'''teste de friedman, já que os dados não seguem uma distribuição normal'''
# Aplicar o teste de Friedman
from scipy.stats import friedmanchisquare
grupos = []
for local, grupo in df.groupby('Ano'):
    grupos.append(grupo['Cianobacteria'])

grupos_iguais = []
for local, grupo in df.groupby('Ano'):
    grupo_amostrado = grupo.sample(6, random_state=42)  # Ajuste o random_state para garantir replicabilidade
    grupos_iguais.append(grupo_amostrado['Cianobacteria'])

# Aplicar o teste de Friedman
estatistica_friedman, p_valor = friedmanchisquare(*grupos_iguais)

# Exibir resultados
print(f"Estatística de Friedman: {estatistica_friedman}")
print(f"Valor p: {p_valor}")




'''a anova não é o melhor teste, já que os dados não seguem uma distribuição normal, 
como observado no teste de shapiro-wilk
O teste de friedman foi aplicado então, considerando apenas o ano como variavel indepen
dente. O resultado indica que há diferença entre os anos'''