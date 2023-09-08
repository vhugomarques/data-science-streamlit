import streamlit as st
from multiapp import MultiApp
from apps import home, confidence_interval, data_stats, monte_carlo # import your app modules here

app = MultiApp()

# Add all your application here
app.add_app("Principal", home.app)
app.add_app("Intervalo de confiança", confidence_interval.app)
app.add_app("Dados estatisticos", data_stats.app)
app.add_app("Simulação Monte Carlo", monte_carlo.app)
# The main app
app.run()
