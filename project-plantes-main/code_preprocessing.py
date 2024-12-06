# Importation des bibliothèques nécessaires
import os
import pandas as pd 
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Chargement du fichier 'dataframe_plant_disease_id.csv' dans un DataFrame df et visualisation des données
df = pd.read_csv('data\dataframe_plant_disease_id.csv')

### Définition des fonctions ### 

### Définition des fonctions ### 

# Fonction pour importer et convertir une image au format classique (0-255)
def import_image(image_path):
    # Importation de l'image
    img = plt.imread(image_path)
    
    # Conversion du type png (0-1) en classique (0-255)
    if img.dtype == np.float32 or img.dtype == np.float64:
        img = (img * 255).astype(np.uint8)
    
    return img

# Fonction pour redimensionner une image à la taille standard 224x224
def resize_image(img, size=(224, 224)):
   
    img_resized = cv2.resize(img, size)

    return img_resized

# Fonction pour appliquer un masque vert et convertir les images RGB au format segmenter (fond noir)
def create_green_mask(img, green_threshold=(90, 10, 90)):
    
    # Isoler les pixels du filtre vert
    green_mask = (img[:,:,1] > img[:,:,0]) & (img[:,:,1] > img[:,:,2])
    
    # Seuil pour vert
    green_mask = green_mask & (img[:,:,1] > green_threshold[1])
    
    # Seuil pour rouge et jaune
    green_mask = green_mask & (img[:,:,0] < green_threshold[0]) & (img[:,:,2] < green_threshold[2])
    
    # Application du masque + négatif
    masked_img = img.copy()
    if img.shape[2] == 3 : 
        masked_img[~green_mask] = [0, 0, 0]
    elif img.shape[2] == 4 :
        masked_img[~green_mask] = [0, 0, 0, 255]
    
    return green_mask, masked_img

# Fonction pour sous-échantillonner la classe "Tomato" qui est sur-représentée
def downsample_majority_classe(df):
    from sklearn.utils import resample
    
    # Séparation de la classe majoritaire (Tomato) et des autres classes
    df_majority = df[df['espèce'] == 'Tomato']
    df_minority = df[df['espèce'] != 'Tomato']
    
    # Définition de la taille cible comme celle de la classe minoritaire la plus grande
    target_size = df_minority['espèce'].value_counts().max()
    
    # Sous-échantillonner la classe majoritaire
    df_majority_downsampled = resample(df_majority, 
                                       replace=False,           # Échantillonnage sans remise
                                       n_samples=target_size,   # Réduire à la taille cible
                                       random_state=42)         # Pour la reproductibilité
    
    # Fusion de la classe majoritaire sous-échantillonnée et des autres classes
    df_equilibre = pd.concat([df_majority_downsampled, df_minority])
    
    return df_equilibre
