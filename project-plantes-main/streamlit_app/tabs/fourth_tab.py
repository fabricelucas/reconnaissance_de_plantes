import streamlit as st
import pandas as pd
import numpy as np

title = "Étape 3 - Modélisation"
sidebar_name = "Modélisation"


def run():

    st.header(title)

    st.markdown("___")

    st.write("""Avant de se lancer dans les tests de différents modèles, nous devons préparer nos données pour qu'elles soient adaptées à l'entraînement :  
                    - Les colonnes espèce et état contiennent des variables catégorielles. Afin qu'elles soient interprétées correctement par le modèle, elles doivent être transformées en valeurs numériques (encodage).  
                    - Les données seront ensuite divisées en deux ensembles distincts : un ensemble d'entraînement pour apprendre les caractéristiques des données, et un ensemble de test pour évaluer les performances du modèle.  
                    - Enfin, les dimensions des images seront normalisées afin d'améliorer la stabilité et l'efficacité de l'entraînement des modèles.  
             Dans un premier temps, on ne s'intéresse qu'à la variable cible 'espèce' sans tenir compte de la variable cible 'état'.
             """)
    
    
    

