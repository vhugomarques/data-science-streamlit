import streamlit as st
from multiapp import MultiApp
from apps import home, data_stats, monte_carlo # import your app modules here

app = MultiApp()

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Data Stats", data_stats.app)
app.add_app("Monte Carlo", monte_carlo.app)
# The main app
app.run()
