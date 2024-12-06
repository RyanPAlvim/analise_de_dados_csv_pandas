import pandas as pd
import numpy as np

#Transformando os dados do arquivo em um dataframe
df = pd.read_csv("data.csv", sep=',')

#Printando esse df, também existe a função display no jupyter
print(df)

#Pegando a média do salário
print(df['Salario'].mean())

#Pegando a média das idades
print(df['Idade'].mean())

#Pegando a soma de todos salários
print(df['Salario'].sum())

#Pega as 5 primeiras linhas do data frame
print(df.head(5))

#Mostra as linhas e colunas da tabela
print(df.shape)

#Faz uma descrição de diversos elementos do df, média, soma, etc
print(df.describe())

#Uma serie do panda (pd.Series), nada mais é que uma coluna do df
#df['Idade'] é uma pd.Series

#Podemos pegar 2 colunas:
print(df[['Idade', 'Salario']])

#Pegar uma linha:
print(df.loc[2])