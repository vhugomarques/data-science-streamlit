import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
def app():
    st.title("Simulation Monte Carlo")

    st.write("This is a sample of Monte Carlo in the mutliapp.")
    st.write("See `apps/monte_carlo.py` to know how to use it.")

    st.sidebar.header("Drag the bar")
    #st.sidebar.markdown("Arraste a barra")

    n = st.sidebar.slider("Iterations:",1,10**5,10**1)

    #Gera Distribuicao Uniforme com n pontos
    #n = 10**6
    r = 1
    x = np.random.rand(n,2)

    #Computa todos os pontos dentro do raio r
    aux=np.sqrt(x[:,0]**2+x[:,1]**2) < r
    inside = x[np.sqrt(x[:,0]**2+x[:,1]**2) < r]

    #Calcula pi
    estimate = 4*len(inside)/len(x)
    title='Estimative of $\pi$: '+str(estimate)+' with '+str(n)+' iterations'

    #Plot
    fig = plt.figure(figsize=(8,8))
    plt.scatter(x[:,0], x[:,1], s = .5, c='red')
    plt.scatter(inside[:,0], inside[:,1], s = .5, c='blue')
    plt.title(title)
    plt.legend()
    plt.show()
    st.pyplot(fig)
