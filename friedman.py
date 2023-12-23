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
from scipy.stats import friedmanchisquare

df=pd.read_csv('/home/joao/encontro_recifal_2024/dados/cianobacteria.csv')
df['Ano'] = df['Ano'].astype('category')
df['Local'] = df['Local'].astype('category')


'''teste de friedman, já que os dados não seguem uma distribuição normal'''
# Aplicar o teste de Friedman
grupos_iguais = []
for ano, grupo in df.groupby('Ano'):
    grupo_amostrado = grupo.sample(6, random_state=42)  # Ajuste o random_state para garantir replicabilidade
    grupos_iguais.append(grupo_amostrado['Cianobacteria'])

# Aplicar o teste de Friedman
estatistica_friedman, p_valor = friedmanchisquare(*grupos_iguais)

# Exibir resultados
print(f"Estatística de Friedman: {estatistica_friedman}")
print(f"Valor p: {p_valor}")

#teste de don buferoni ( post hoc)
from scikit_posthocs import posthoc_dunn

# Realizar o teste de Dunn-Bonferroni
pos_hoc_dunn = posthoc_dunn(grupos_iguais)

# Exibir os resultados
print(f"Teste de Friedman: Estatística = {estatistica_friedman}, p-valor = {p_valor}")
print("Teste de Dunn-Bonferroni:")
print(pos_hoc_dunn)





'''a anova não é o melhor teste, já que os dados não seguem uma distribuição normal, 
como observado no teste de shapiro-wilk
O teste de friedman foi aplicado então, considerando apenas o ano como variavel indepen
dente. O resultado indica que há diferença entre os anos'''