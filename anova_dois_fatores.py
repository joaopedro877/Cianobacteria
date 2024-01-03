import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols
import numpy as np
from statsmodels.stats.diagnostic import het_white


df=pd.read_csv('/home/joao/encontro_recifal_2024/dados/cianobacteria2.csv')
df['Ano'] = df['Ano'].astype('category')
df['Local'] = df['Local'].astype('category')

'''anova de dois fatores'''
modelo = ols('Cianobacteria ~ C(Ano) + C(Local)', data=df).fit()
resultado_anova = sm.stats.anova_lm(modelo, typ=2)

print(resultado_anova)


# Realizando o teste de White para heterocedasticidade
white_test = het_white(modelo.resid, modelo.model.exog)
labels = ['LM Statistic', 'LM-Test p-value', 'F-Statistic', 'F-Test p-value']
print(dict(zip(labels, white_test)))


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
