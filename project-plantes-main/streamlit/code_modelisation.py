# Importation des bibliothèques nécessaires
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.layers import Conv2D
from joblib import load
import tensorflow as tf
import cv2
import matplotlib.pyplot as plt

### Définition des fonctions ### 

# Fonction pour charger et utiliser un modèle
def load_and_predict(model_path, image, model_type):
    if model_type == "keras":
        # Charger un modèle Keras
        model = load_model(model_path)
        
        # Conversion de l'image en tableau numpy
        image_array = np.array(image)

        # Ajouter une dimension batch
        image_array = np.expand_dims(image_array, axis=0) 

        # Faire la prédiction
        predictions = model.predict(image_array)[0]  # Retourne la première ligne des prédictions
        predicted_class = np.argmax(predictions)  # Classe prédite

    elif model_type == "random_forest":
        # Charger un modèle scikit-learn
        model = load(model_path)

        # Convertir l'image en niveaux de gris si nécessaire
        if len(image.shape) == 3:  # Image RGB ou similaire
            image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        
        # Aplatir l'image pour l'entrée du Random Forest
        image_array = image.flatten()

        # Faire la prédiction
        predictions = model.predict_proba([image_array])[0]
        predicted_class = np.argmax(predictions)

    return predicted_class, predictions

# Fonction pour Grad-CAM

##Importation de l'image
def get_img_array(img_path, size):
    """
    Importation d'une image dans les normes du gradcam
    Paramètres : 
        img_path (string) : chemin de l'image 
        size (tuple) : taille de l'image
    Return : 
        array (array): image 
    """
    img = tf.keras.preprocessing.image.load_img(img_path, target_size=size)
    array = tf.keras.preprocessing.image.img_to_array(img)
    array = np.expand_dims(array, axis=0)
    return array

##Heatmap pour le gradcam
def make_gradcam_heatmap(img_array, model, last_conv_layer_name, pred_index=None):
    """
    Génération de la heatmap du gradcam à partir d'un modèle 
    Paramètres : 
        img_array (array) : image
        model (keras.models) : modèle (sous forme de Model())
        last_conv_layer_name (string) : nom de la dernière couche de convolution du modèle
        pred_index : indice de prédiction
    Return : 
        heatmap (array): heatmap du gradcam 
    """
    grad_model = tf.keras.models.Model(
        [model.inputs], [model.get_layer(last_conv_layer_name).output, model.output]
    )
    
    with tf.GradientTape() as tape:
        last_conv_layer_output, preds = grad_model(img_array)
        if pred_index is None:
            pred_index = tf.argmax(preds[0])
        class_channel = preds[:, pred_index]
    
    grads = tape.gradient(class_channel, last_conv_layer_output)
    pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))
    
    last_conv_layer_output = last_conv_layer_output[0]
    heatmap = last_conv_layer_output @ pooled_grads[..., tf.newaxis]
    heatmap = tf.squeeze(heatmap)
    
    heatmap = tf.maximum(heatmap, 0) / tf.math.reduce_max(heatmap)
    return heatmap.numpy()

## Trouver le nom de la dernière couche de convolution du modèle
def find_last_conv_layer(model):
    """
    Trouver le nom de la dernière couche de convolution du modèle
    Paramètres : 
        model (keras.models) : modèle
    Return : 
        last_conv_layer.name : nom de la dernière couche de convolution du modèle
    """
    last_conv_layer = None

    for layer in reversed(model.layers):

        if type(layer) == Conv2D:
            last_conv_layer = layer
            return last_conv_layer.name

    if last_conv_layer == None:
        raise ValueError("Pas de Conv2D dans le modèle")
    return 0

## Application du gradcam pour une image
def apply_gradcam_single(img_path, model, output_name, class_labels, true_species=None):
    """
    Application du gradcam pour une image pour un seul modèle
    Paramètres : 
        img_path (chemin) : chemin de l'image à traiter
        model (keras.models) : modèle pour le gradcam
        output_name (string) : chemin de sortie de l'image appliquée au gradcam
        true_species (string) : Défaut : None - Vraie espèce de la plante
        class_labels (dictionnaire) : Dictionnaire contenant les noms des classes, avec les indices comme clés.

    Return : 
        class_img (string): nom de la classe prédite avec le maximum de probabilité
        precision (float) : pourcentage de précision
    """
    img_array = get_img_array(img_path, size=(224, 224))
    last_conv_layer_name = find_last_conv_layer(model)
    heatmap = make_gradcam_heatmap(img_array, model, last_conv_layer_name)

    img = cv2.imread(img_path)
    heatmap = cv2.resize(heatmap, (img.shape[1], img.shape[0]))
    heatmap = np.uint8(255 * heatmap)
    heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)

    superimposed_img = heatmap * 0.5 + img
    cv2.imwrite(output_name, superimposed_img)

    preds = model.predict(img_array)
    predicted_class = np.argmax(preds[0])
    class_img = class_labels.get(predicted_class, "Classe inconnue")
    precision = preds[0][predicted_class]

    return class_img,precision

## Affichage du gradcam pour une image et un seul modèle
def display_gradcam_single(output_name,class_img,precision,true_species):
    """
    Affichage du gradcam appliqué à une image pour un seul modèle
    Paramètres : 
        output_name (string) : nom du fichier de sortie de l'image
        class_img (string) : nom de la classe prédite de l'image
        precision (float) : pourcentage de probabilité de la classe prédite
        true_species (string): vraie espèce de la plante
    """
    img_sur = plt.imread(output_name)
    plt.imshow(img_sur)
    plt.colorbar()
    if true_species == None :
        plt.title(f"Prédiction : {class_img} - {precision*100:.2f}%")
    else :
        plt.title(f"Prédiction : {class_img} - {precision*100:.2f}% - Vraie espèce : {true_species}")
    plt.axis('off')
