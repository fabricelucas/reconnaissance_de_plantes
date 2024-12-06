import os 
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

from code_preprocessing import import_image, resize_image, create_green_mask

title = "Étape 2 - Pre-processing et feature engineering"
sidebar_name = "Pré-processing"

def run():

    st.header(title)

    st.markdown("___")

    st.write("""Dans cette partie, nous allons appliquer différentes méthodes afin de répondre aux conclusions tirées précédemment :   
                    - Appliquer un sous-échantillonnage à la classe 'Tomato' pour équilibrer les classes.
                    - Redimensionner les images à une taille standard pour faciliter l'entraînement des modèles.  
                    - Convertir toutes les images au même format pour garantir la cohérence des entrées (application d'un masque vert pour supprimer le fond des images RGB).  
             """)
    
    # Chemin vers le dossier contenant les images
    dataset_folder = r"data"

 # Liste des images disponibles dans les dossiers 'plantdisease' et 'semis' uniquement
    image_files = []
    for root, dirs, files in os.walk(dataset_folder):
        if any(folder in root for folder in ['plantdisease', 'semis']):
            for file in files:
                if file.endswith(('.png', '.jpg', '.jpeg')):
                    image_files.append(os.path.join(root, file))

    # Interface pour sélectionner une image 
    selected_image = st.selectbox("Choisissez une image à traiter :", image_files)
    st.write("""Note :  
             - Si vous sélectionnez une image provenant du dossier data\plantdisease, vous ne verrez pas l'application du masque vert puisque l'image d'origie est déjà segmentée.  
             - Si vous sélectionnez une image provenant du dossier data\semis, vous pourrez voir la mise en oeuvre du masque vert.  """)

    if selected_image:
        # Chemin complet de l'image sélectionnée
        image_path = selected_image

        # Charger l'image originale
        st.subheader("Image Originale")
        
        image = import_image(image_path)
        st.image(image, caption=f"Image Originale - {os.path.basename(selected_image)}")

        # Afficher les dimensions de l'image originale
        original_height, original_width = image.shape[:2]
        st.write(f"Dimensions de l'image originale : {original_width} x {original_height}")

        # Redimensionner l'image à une taille standard (224x224)
        st.subheader("Image Redimensionnée")
        img_resized = resize_image(image, size=(224, 224))
        st.image(img_resized, caption="Image Redimensionnée (224x224)",)

        # Appliquer le masque vert pour supprimer le fond des images RGB uniquement si l'image est dans 'semis'
        if 'semis' in image_path:
            st.header("Image avec Masque Vert Appliqué")
            green_mask, masked_image = create_green_mask(img_resized)
            st.image(masked_image, caption="Image avec Fond Supprimé (Masque Vert)")

        # Afficher les dimensions de l'image redimensionnée
        resized_height, resized_width = img_resized.shape[:2]
        st.write(f"Dimensions de l'image redimensionnée : {resized_width} x {resized_height}")
