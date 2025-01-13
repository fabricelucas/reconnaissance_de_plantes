import streamlit as st

title = "Projet : Reconnaissance de plantes"
sidebar_name = "Introduction"

def run():

    st.image("streamlit_app/assets/banner.png")

    st.title(title)

    st.markdown(
        """
        <hr class="hr">
        """,
        unsafe_allow_html=True
    )

    st.markdown("**Présentation du projet**")
    st.write("""
    Notre projet vise à répondre à des besoins concrets :
    - *Particuliers* : Identifier facilement les plantes.
    - *Professionnels* : Outils pour l’agriculture et les espaces publics.
    """)

    st.markdown("**Actuellement**")
    st.write("""
    - Entraînement avec un jeu de données interne.
    - Utilisation des réseaux de neurones convolutifs (Deep Learning).
    - Capture photo en temps réel et détection de maladies à venir.
    """)

    st.markdown("**Pourquoi ce projet ?**")
    st.image("streamlit_app/assets/apps_logo.png")
    st.write("""
    Les applications actuelles montrent des limites :
    - Détection des maladies insuffisante.
    - Certaines fonctionnalités payantes.
    """)

    st.markdown("**Notre objectif**")
    st.write("""
    Créer une solution complète, combinant identification des espèces **et** analyse de santé.
    """)