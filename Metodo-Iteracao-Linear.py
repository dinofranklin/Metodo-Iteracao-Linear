#!/usr/bin/env python
# coding: utf-8

# In[6]:


from sympy import *
import numpy as np
import matplotlib.pyplot as plt
import math
get_ipython().run_line_magic('matplotlib', 'inline')
x, y = symbols('x y')


# In[7]:


def verifica_convergencia(ponto_fixo, x0):
    # Calcula a derivada do ponto fixo e verifica pra qual x essa derivada < 1
    derivada = diff(ponto_fixo)
    intervalo = solveset(derivada < 1, x, S.Reals)
    
    # Verifica se é possível utilizar x0 como inicial
    if x0 > intervalo.inf and x0 < intervalo.sup: 
        return True
    
    else:
        return False
    
def metodo_iteracao_linear(ponto_fixo, x0):   
    if (verifica_convergencia(ponto_fixo, x0)):
        # Calcula a aproximacao de x1
        aproximacao = ponto_fixo.subs({x: x0})
        print('x{i} = {aprox}'.format(i=0,aprox=aproximacao))

        i = 1
        
        #Calcula as aproximações xk
        while i< 25:
            aproximacao = ponto_fixo.subs({x: aproximacao})
            print('x{i} = {aprox}'.format(i=i,aprox=aproximacao))
            i = i+1
            
    else:
        print('A sequência de aproximações resultantes não é convergente.')
        
def mostrar_grafico(ponto_fixo): 
    xx = np.linspace(0, 5, 5000, endpoint=False)
    yy = lambdify(x, [x, ponto_fixo])(xx)
    plt.figure(figsize=(20,10))
    plt.axis([1, 5, 0, 10])
    plt.plot(xx, np.transpose(yy))
    plt.show()


# In[9]:


metodo_iteracao_linear(x**2, 2.5)


# In[10]:


metodo_iteracao_linear(sqrt(2+x), 2.5)


# In[11]:


mostrar_grafico(x**2 - 2)


# In[12]:


mostrar_grafico(sqrt(2+x))


# In[ ]:




