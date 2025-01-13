import streamlit as st
import pandas as pd 

title = "Étape 4 - Interprétabilité avec Grad-CAM"
sidebar_name = "Interprétabilité avec Grad-CAM"

def run():

    st.header(title)

    st.markdown("___")

    st.write("""
    - Technique de visualisation des zones importantes pour la classification.
    - Heatmaps montrent les régions influentes pour les décisions des modèles.
    - Permet de comparer comment chaque modèle analyse une image.
    """)

    st.markdown("### Visualisations Grad-CAM - Différences entre les modèles")
    st.image("streamlit_app/assets/model_comparison_0.png")
    st.image("streamlit_app/assets/model_comparison_1.png")
    st.image("streamlit_app/assets/model_comparison_2.png")
    st.image("streamlit_app/assets/model_comparison_3.png")
