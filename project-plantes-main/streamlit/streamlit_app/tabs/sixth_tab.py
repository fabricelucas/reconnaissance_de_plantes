import os
import streamlit as st
import pandas as pd
from PIL import Image
from tensorflow.keras.models import load_model
from code_preprocessing import import_image, resize_image, create_green_mask
from code_modelisation import load_and_predict, apply_gradcam_single

title = "Reconnaissance de plantes - Pre-processing, Modélisation et Interprétabilité"
sidebar_name = "Démonstration"

# Dictionnaire des modèles disponibles
models = {
    "Random Forest": "data/modèles/random_forest_model.joblib",
    "ResNet50": "data/modèles/resnet_model.h5",
    "EfficientNetB3": "data/modèles/efficientnet_model.h5",
    "MobileNet": "data/modèles/mobilenet_model.h5",
    "From Scratch inspiré par LeNet": "data/modèles/lenet_model.h5"
}

# Dictionnaire des classes disponibles 
class_labels = {
    0: 'Apple',
    1: 'Black-grass',
    2: 'Blueberry',
    3: 'Charlock',
    4: 'Cherry_(including_sour)',
    5: 'Cleavers',
    6: 'Common Chickweed',
    7: 'Common wheat',
    8: 'Corn_(maize)',
    9: 'Fat Hen',
    10: 'Grape',
    11: 'Loose Silky-bent',
    12: 'Maize',
    13: 'Orange',
    14: 'Peach',
    15: 'Pepper,_bell',
    16: 'Potato',
    17: 'Raspberry',
    18: 'Scentless Mayweed',
    19: 'Shepherd’s Purse',
    20: 'Small-flowered Cranesbill',
    21: 'Soybean',
    22: 'Squash',
    23: 'Strawberry',
    24: 'Sugar beet',
    25: 'Tomato'
}

def run():
    st.header(title)
    st.markdown("___")

    # Sélection de l'image
    dataset_folder = r"data"
    image_files = []
    for root, dirs, files in os.walk(dataset_folder):
        if any(folder in root for folder in ['plantdisease', 'semis']):
            for file in files:
                if file.endswith(('.png', '.jpg', '.jpeg')):
                    image_files.append(os.path.join(root, file))

    selected_image_path = st.selectbox("Choisissez une image :", image_files)

    if selected_image_path:
        st.subheader("Pre-processing")
        image = import_image(selected_image_path)
        st.image(image, caption="Image originale")

        # Afficher les dimensions de l'image originale
        original_height, original_width = image.shape[:2]
        st.write(f"Dimensions de l'image originale : {original_width} x {original_height}")

        # Redimensionnement
        img_resized = resize_image(image, size=(224, 224))
        st.image(img_resized, caption="Image redimensionnée")

        # Afficher les dimensions de l'image redimensionnée
        resized_height, resized_width = img_resized.shape[:2]
        st.write(f"Dimensions de l'image redimensionnée : {resized_width} x {resized_height}")

        # Masque vert si image dans le dataset 'semis'
        if 'semis' in selected_image_path:
            _, img_resized = create_green_mask(img_resized)
            st.image(img_resized, caption="Image redimensionnée avec fond uni (masque vert appliqué)")
            st.write(f"Dimensions de l'image redimensionnée après application du masque : {img_resized.shape[1]} x {img_resized.shape[0]}")

        # Sélection d'un modèle
        st.subheader("Modélisation")
        selected_model_name = st.selectbox("Choisissez un modèle :", list(models.keys()))
        model_path = models[selected_model_name]

        # Prédiction
        if st.button("Lancer la prédiction"):
            st.write("Chargement du modèle et traitement de l'image...")
            model_type = "random_forest" if selected_model_name == "Random Forest" else "keras"
            model = load_model(model_path) if model_type == "keras" else None

            predicted_class, predictions = load_and_predict(model_path, img_resized, model_type)
            predicted_label = class_labels.get(predicted_class, "Classe inconnue")

            # Extraire la classe réelle à partir du dossier parent
            true_class = os.path.basename(os.path.dirname(selected_image_path))

            # Affichage des résultats
            st.subheader("Résultats de la prédiction")
            st.write(f"Classe prédite : {predicted_label} (Indice : {predicted_class})")
            st.write(f"Classe réelle : {true_class}")
            
            probabilities_df = pd.DataFrame({
                "Classe": [class_labels[i] for i in range(len(predictions))],
                "Probabilité (%)": [round(float(prob) * 100, 2) for prob in predictions]
            })
            st.dataframe(probabilities_df, use_container_width=True)

            # Visualisation Grad-CAM
            if model_type == "keras":
                st.subheader("Interprétabilité avec Grad-CAM")
                gradcam_folder = "data/output_images_gradcam"
                os.makedirs(gradcam_folder, exist_ok=True)
                gradcam_output_path = os.path.join(gradcam_folder, f"gradcam_{os.path.basename(selected_image_path)}")

                gradcam_label, precision = apply_gradcam_single(
                    img_path=selected_image_path,
                    model=model,
                    output_name=gradcam_output_path,
                    class_labels=class_labels,
                    true_species=predicted_label
                )

                gradcam_image = Image.open(gradcam_output_path)
                st.image(gradcam_image, caption=f"Grad-CAM")