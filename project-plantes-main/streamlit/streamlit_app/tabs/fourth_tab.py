import streamlit as st
import os

title = "Étape 3 - Modélisation"
sidebar_name = "Présentation des modèles"

def run():

    st.header(title)

    st.markdown("___")

    models = ["Random Forest", "ResNet50", "EfficientNetB3", "MobileNet", "From Scratch inspiré par LeNet"]
    selected_model = st.radio("Choisissez un modèle :", models)

    # Présentation des modèles
    if selected_model == "Random Forest":
        st.subheader("Random Forest")
        st.image("streamlit/streamlit_app/assets/architeture_random_forest.png", width=500)
        st.write("""
        - Modèle simple et intuitif, utilisé comme référence en Machine Learning.
        - Combine plusieurs arbres de décision pour voter sur une classe majoritaire.
        - Précision obtenue : **69%**.
        - Limitation : Incapacité à capturer les relations spatiales complexes entre pixels.
        - Peu adapté à la reconnaissance d’images malgré une possible optimisation des hyperparamètres.
        """)

    else:
        if selected_model == "ResNet50":
            st.subheader("ResNet50")
            st.image("streamlit/streamlit_app/assets/architeture_ResNet.png")
            st.write("""
            - CNN avec connexions résiduelles pour faciliter l’entraînement des réseaux profonds.
            - Pré-entraîné sur ImageNet (14M images, 1000 classes).
            - Précision obtenue : **97%**.
            - Forces : Bonne généralisation, courbes d’apprentissage efficaces.
            - Limitation : Faible performance sur certaines classes comme Black-Grass.
            """)
            curves_path = "streamlit/streamlit_app/assets/courbes_ResNet.png"
            f1_path = "streamlit/streamlit_app/assets/rapport_ResNet.png"

        elif selected_model == "EfficientNetB3":
            st.subheader("EfficientNetB3")
            st.image("streamlit/streamlit_app/assets/architeture_EfficientNet.png")
            st.write("""
            - Modèle optimisé pour équilibrer profondeur, largeur, et résolution (Compound scaling).
            - Pré-entraîné sur ImageNet.
            - Précision obtenue : **99%**.
            - Forces : Excellente performance avec moins de ressources computationnelles.
            - Limitation : Difficultés similaires à ResNet sur des classes spécifiques comme Black-Grass.
            """)
            curves_path = "streamlit/streamlit_app/assets/courbes_EfficientNet.png"
            f1_path = "streamlit/streamlit_app/assets/rapport_EfficientNet.png"

        elif selected_model == "MobileNet":
            st.subheader("MobileNet")
            st.image("streamlit/streamlit_app/assets/architeture_MobileNet.png")
            st.write("""
            - Modèle optimisé pour les environnements à ressources limitées.
            - Idéal pour des tâches nécessitant des modèles légers et efficaces.
            - Précision obtenue : **95%**.
            - Forces : Bon compromis entre précision et coût computationnel.
            """)
            curves_path = "streamlit/streamlit_app/assets/courbes_MobileNet.png"
            f1_path = "streamlit/streamlit_app/assets/rapport_MobileNet.png"

        elif selected_model == "From Scratch inspiré par LeNet":
            st.subheader("From Scratch inspiré par LeNet")
            st.image("streamlit/streamlit_app/assets/architeture_LeNet.png")
            st.write("""
            - Modèle CNN inspiré de l’architecture LeNet, conçu sans transfert learning.
            - Composé de couches convolutives et de pooling entièrement connectées.
            - Précision obtenue : **80%**.
            - Forces : Permet de comprendre l’importance des architectures complexes et des données.
            - Limitation : Inférieur aux modèles pré-entraînés, dépend fortement du pré-processing.
            """)
            curves_path = "streamlit/streamlit_app/assets/courbes_LeNet.png"
            f1_path = "streamlit/streamlit_app/assets/rapport_LeNet.png"
            

        # Affichage courbes ou rapport F1
        if st.button("Afficher les courbes"):
            if os.path.exists(curves_path):
                st.image(curves_path, caption="Courbes de performance")
            else:
                st.error("L'image des courbes pour ce modèle est introuvable.")

        if st.button("Afficher le rapport F1"):
            if os.path.exists(f1_path):
                st.image(f1_path, caption="Rapport F1")
            else:
                st.error("L'image du rapport F1 pour ce modèle est introuvable.")
