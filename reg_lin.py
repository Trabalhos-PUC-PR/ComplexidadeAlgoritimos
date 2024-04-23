#!/usr/bin/python3
'''
from scipy.stats import t
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

x = [13,27,41,57,72]
y = [10000 * (1 + x.index(i)) for i in x]

res = stats.linregress(x, y)

print(f'x={x}\ny={y}')
print(f"R-squared: {res}")

plt.plot(x, y, 'o', label='original data')
plt.legend()
plt.show()
'''
def estimate_coef(x, y):
  # number of observations/points
  n = np.size(x)
 
  # mean of x and y vector
  m_x = np.mean(x)
  m_y = np.mean(y)
 
  # calculating cross-deviation and deviation about x
  SS_xy = np.sum(y*x) - n*m_y*m_x
  SS_xx = np.sum(x*x) - n*m_x*m_x
 
  # calculating regression coefficients
  b_1 = SS_xy / SS_xx
  b_0 = m_y - b_1*m_x
 
  return (b_0, b_1)

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dados = ["resultados_2h/random.csv","resultados_2h/crescente.csv","resultados_2h/decrescente.csv"]
title = ["Listas Aleatorias", "Listas Crescentes","Listas Descrescente"]
tipo = 0
plot = 1

df = pd.read_csv(dados[tipo],  header=[0] )  
plots = df.drop(['tamanho'], axis=1)
sort = plots.columns[9]

if plot == 0: 
      
    fig, ax = plt.subplots()

    for i in plots.columns:

        ax.plot(df['tamanho'], df[i], label=i)

    ax.legend()
    plt.yscale("log")
    plt.title(title[tipo])
    plt.xlabel("tamanho")
    plt.ylabel("Tempo (ms)")

    plt.show()
if plot == 1:

    x = df['tamanho']
    y = df[sort]

    b = [0,0]
    b[0], b[1] = estimate_coef(x,y)

    fig, ax = plt.subplots()

    plt.scatter(x, y, color = "m",
            marker = "o", s = 30, label = sort)
    
    # predicted response vector
    y_pred = b[0] + b[1]*x
    
    # plotting the regression line
    plt.plot(x, y_pred, color = "g", label="Regreção")
    
    # putting labels
    ax.legend()
    plt.yscale("log")
    plt.title(title[tipo])
    plt.xlabel("tamanho")
    plt.ylabel("Tempo (ms)")

    plt.show()
