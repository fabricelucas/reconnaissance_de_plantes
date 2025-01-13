import streamlit as st
import pandas as pd
import plotly.express as px
from code_preprocessing import import_image, resize_image, create_green_mask

title = "Étape 2 - Pre-processing et feature engineering"
sidebar_name = "Pre-processing"

def run():

    st.header(title)

    st.markdown("___")

    st.subheader("Etapes clés :")
    st.write("""
    - Nettoyage des données
             
    - Equilibrage des classes
    """)
    # Chargement des données
    df_equilibre = pd.read_csv('data\dataframe_up_mask.csv')

    # Visualisation de la distribution des espèces de plantes au niveau du DataFrame
    especes_fig = px.histogram(df_equilibre, x='espèce', title="Distribution des espèces de plantes", color_discrete_sequence=['#347d7b'])
    especes_fig.update_xaxes(title="Espèce de la plante", tickangle=45)
    especes_fig.update_yaxes(title="Nombre d'images")
    st.plotly_chart(especes_fig)

    # Calcul de la proportion représentant l'espèce 'Tomato' au niveau du DataFrame
    valeurs_tomate = (df_equilibre['espèce'] == 'Tomato').sum()
    valeurs_tomate_pourcent = round((valeurs_tomate / len(df_equilibre)) * 100, 2)
    st.write(f"Pourcentage de plantes de type 'Tomato' : {valeurs_tomate_pourcent}%")

    st.write("""
    - Application de la fonction process_images
    """)

    # Chemins prédéfinis vers une image de chaque dataset
    semis_image_path = r"data/semis/Cleavers/1.png"
    plantdisease_image_path = r"data/plantdisease/Apple___healthy/0a553fc0-fc2c-4598-baba-3bc10191447c___RS_HL 5969_final_masked.jpg"


    # Charger et afficher une image de 'semis'
    st.write("*Traitement d'une image du dataset 'semis'*")
    semis_image = import_image(semis_image_path)
    st.image(semis_image, caption="Image originale - Cleavers")
    original_height, original_width = semis_image.shape[:2]
    st.write(f"Dimensions de l'image originale : {original_width} x {original_height}")

    # Redimensionnement de l'image à une taille standard (224x224)
    img_resized_semis = resize_image(semis_image, size=(224, 224))
    st.image(img_resized_semis, caption="Image redimensionnée - Cleavers")
    resized_height, resized_width = img_resized_semis.shape[:2]
    st.write(f"Dimensions de l'image redimensionnée : {resized_width} x {resized_height}")

    # Appliquer le masque vert pour l'image du dataset 'semis'
    green_mask, masked_image_semis = create_green_mask(img_resized_semis)
    st.image(masked_image_semis, caption="Image redimensionnée avec fond uni (après application du masque Vert) - Cleavers")
    st.write(f"Dimensions de l'image redimensionnée après application du masque : {masked_image_semis.shape[1]} x {masked_image_semis.shape[0]}")


    # Charger et afficher une image de 'plantdisease'
    st.write("*Traitement d'une image du dataset 'plantdisease'*")
    plantdisease_image = import_image(plantdisease_image_path)
    st.image(plantdisease_image, caption="Image originale - Apple (healthy)")
    original_height, original_width = plantdisease_image.shape[:2]
    st.write(f"Dimensions de l'image originale : {original_width} x {original_height}")

    # Redimensionnement de l'image à une taille standard (224x224)
    img_resized_pd = resize_image(plantdisease_image, size=(224, 224))
    st.image(img_resized_pd, caption="Image redimensionnée - Apple (healthy)")
    resized_height, resized_width = img_resized_pd.shape[:2]
    st.write(f"Dimensions de l'image redimensionnée : {resized_width} x {resized_height}")




