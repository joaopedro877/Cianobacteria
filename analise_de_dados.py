#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 12:43:07 2023

@author: joao
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv("/home/joao/encontro_recifal_2024/dados/dados_completo.csv")
new_columns = []
for col in df.columns:
    if col == 'Local':
        new_columns.append(col)
    else:
        new_columns.append(f'({col.split(".")[0]}, {df[col][0]})')

# Atribuindo os novos títulos de coluna ao DataFrame
df.columns = new_columns

# Removendo as linhas que foram usadas como títulos das colunas
df = df.iloc[1:].reset_index(drop=True)

df = df.drop(0, axis=0)

df.set_index('Local', inplace=True)



'''cobertura em porcentagem, com titulo em lista'''

cobertura=(df/df.sum())*100


