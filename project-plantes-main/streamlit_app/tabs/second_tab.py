import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image

title = "Étape 1 - Exploration des données & DataVizualisation"
sidebar_name = "Exploration"

def run():

    st.header(title)

    st.markdown("___")

    # Chargement des données
    df = pd.read_csv('data\dataframe_plant_disease_id.csv')

    # Affichage du DataFrame et de ses caractéristiques
    st.subheader("Aperçu des données")

    st.write("**Premières lignes du DataFrame :**")
    st.dataframe(df.head(10))
    st.write("""**Description des différentes colonnes :**   
        - **chemin :** chemin de l'image dans les fichiers  
        - **hauteur :** hauteur de l'image en pixel  
        - **largeur :** largeur de l'image en pixel  
        - **espèce :** espèce de la plante  
        - **couleur :** booléen correspondant à 0 = image RGB et 1 = image segmented (sans fond)  
        - **état :** état de la plante (valable uniquement pour le DataSet PlantVillage, sinon None).  
             Prend soit :  
             - la valeur 'healthy' si la plante est saine  
             - les valeurs correspondants aux noms de la maladie présente :  
        'Black_rot', 'Early_blight', 'Target_Spot', 'Late_blight', 'Tomato_mosaic_virus', 'Haunglongbing_(Citrus_greening)', 'Leaf_Mold', 'Leaf_blight_(Isariopsis_Leaf_Spot)', 'Powdery_mildew', 'Cedar_apple_rust', 'Bacterial_spot', 'Common_rust_', 'Esca_(Black_Measles)', 'Tomato_Yellow_Leaf_Curl_Virus', 'Apple_scab', 'Northern_Leaf_Blight', 'Spider_mites Two-spotted_spider_mite', 'Septoria_leaf_spot', 'Cercospora_leaf_spot Gray_leaf_spot', 'Leaf_scorch'  
        """)

    st.write("**Résumé statistique du DataFrame :**")
    st.dataframe(df.describe())

    st.write("**Taille du DataFrame :**", df.shape)

    # Visualisations des données
    st.subheader("Visualisations des données")

    # Affichage d'une heatmap pour visualiser les valeurs manquantes
    heatmap_fig = px.imshow(df.isna(), color_continuous_scale='greens')
    heatmap_fig.update_layout(title='Valeurs manquantes dans le DataFrame')
    st.plotly_chart(heatmap_fig)

    # Calculer le pourcentage de valeurs manquantes dans le DataFrame
    valeurs_manquantes_etat = df['état'].isna().sum()
    valeurs_manquantes_etat_pourcent = round(((valeurs_manquantes_etat / len(df)) * 100), 2)

    st.write(f"Nombre de valeurs manquantes dans la colonne 'état' : {valeurs_manquantes_etat}")
    st.write(f"Pourcentage de valeurs manquantes dans la colonne 'état' : {valeurs_manquantes_etat_pourcent}%")

    st.write("""
        Nous remarquons que nous avons 5539 valeurs manquantes dans la catégorie 'état', soit 9.26 % du DataFrame. Il s'agit des images provenant du dataset [V2 Plant Seedlings Dataset](https://www.kaggle.com/datasets/vbookshelf/v2-plant-seedlings-dataset) dont les images ne disposent pas de cette donnée. 
        """)

    # Visualisation de la distribution des espèces de plantes au niveau du DataFrame
    especes_fig = px.histogram(df, x='espèce', title="Distribution des espèces de plantes", color_discrete_sequence=['#347d7b'])
    especes_fig.update_xaxes(title="Espèce de la plante", tickangle=45)
    especes_fig.update_yaxes(title="Nombre d'images")
    st.plotly_chart(especes_fig)

    # Visualisation de la distribution des états de plantes au niveau du DataFrame
    etat_fig = px.histogram(df, x='état', title="Distribution des états de plantes", color_discrete_sequence=['#9ae185'])
    etat_fig.update_xaxes(title="État de la plante", tickangle=45)
    etat_fig.update_yaxes(title="Nombre d'images")
    st.plotly_chart(etat_fig)

    # Visualisation de la distribution des hauteurs des images au niveau du DataFrame
    hauteur_fig = px.histogram(df, x='hauteur', nbins=50, title="Distribution des hauteurs des images", color_discrete_sequence=['#347d7b'])
    hauteur_fig.update_xaxes(title="Hauteur de l'image (pixels)")
    hauteur_fig.update_yaxes(title="Nombre d'images")
    st.plotly_chart(hauteur_fig)

    # Visualisation de la distribution de la catégorie 'couleur' des images au niveau du DataFrame
    couleur_fig = px.histogram(df, x='couleur', nbins=2, title="Distribution de la catégorie 'couleur' des images", color_discrete_sequence=['#9ae185'])
    couleur_fig.update_xaxes(title="Catégorie de la 'couleur'", tickvals=[0, 1], ticktext=['RGB', 'Segmented'])
    couleur_fig.update_yaxes(title="Nombre d'images")
    couleur_fig.update_layout(bargap=0.5)
    st.plotly_chart(couleur_fig)

    # Affichage d'une image RGB et d'une image segmentée
    st.write("Exemple d'une image RGB (Cleaver - DataSet V2 Plant Seedlings) : ")
    st.image(Image.open(r"streamlit_app\\assets\\img_rgb.png"), width=300)

    st.write("Exemple d'une image segmentée (Framboisier sain - DataSet PlantVillage) : ")
    st.image(Image.open(r"streamlit_app\assets\img_segmentee.jpg"), width=300)

    ### Analyse des graphiques ###
    st.subheader("Analyse des graphiques")
    
    # Calcul de la proportion représentant l'espèce 'Tomato' au niveau du DataFrame
    valeurs_tomate = (df['espèce'] == 'Tomato').sum()
    valeurs_tomate_pourcent = round((valeurs_tomate / len(df)) * 100, 2)
    st.write(f"Pourcentage de plantes de type 'Tomato' : {valeurs_tomate_pourcent}%")

    # Calcul de la proportion représentant l'état 'healthy' au niveau du DataFrame
    valeurs_healthy = (df['état'] == 'healthy').sum()
    valeurs_healthy_pourcent = round((valeurs_healthy / len(df)) * 100, 2)
    st.write(f"Pourcentage de plantes dont l'état est 'healthy' : {valeurs_healthy_pourcent}%")

    # Calcul de la proportion représentant l'état 'unhealthy' au niveau du DataFrame (différent de 'healthy' et NaN)
    valeurs_unhealthy = ((df['état'] != 'healthy') & (~df['état'].isna())).sum()
    valeurs_unhealthy_pourcent = round((valeurs_unhealthy / len(df)) * 100, 2)
    st.write(f"Pourcentage de plantes dont l'état est 'unhealthy' : {valeurs_unhealthy_pourcent}%")

    # Calcul de la proportion représentant l'état 'NaN' au niveau du DataFrame
    valeurs_nan = df['état'].isna().sum()
    valeurs_nan_pourcent = round((valeurs_nan / len(df)) * 100, 2)
    st.write(f"Pourcentage de plantes dont l'état est 'NaN' : {valeurs_nan_pourcent}%")

    st.write("""
    - **Distribution des espèces de plantes :**

    ___Observation(s) :___ La catégorie "Tomato" est nettement surreprésentée (30.35%) par rapport aux autres espèces. Cela peut entraîner un déséquilibre dans notre modèle de classification, car il sera davantage biaisé vers cette catégorie.
    
    ___Action(s) possible(s) :___ Application d'un sous-échantillonnage de "Tomato" pour équilibrer les données et pour réduire le biais dans le modèle de classification. L’application d’un suréchantillonnage serait plus complexe à mettre en œuvre, car il impliquerait de générer artificiellement des données pour de nombreuses classes sous-représentées, ce qui augmenterait la complexité et le risque de biais. En revanche, le sous-échantillonnage est ici une solution plus simple, puisqu’il ne concerne qu’une seule classe sur-représentée. Bien que cette méthode entraîne une perte d’information, cela reste acceptable compte tenu de la taille conséquente de notre échantillon d’images, qui garantit une diversité suffisante pour entraîner le modèle de manière efficace.

    - **Distribution des états des plantes :**
    
    ___Observation(s) :___ Environ 25,21 % des plantes sont dans l'état "healthy", tandis que 65,54 % sont atteintes de maladies et 9,26 % présentent des valeurs manquantes. Même si l'état "healthy" a une part importante, il y a une majorité d'exemples malades, ce qui est utile pour entraîner un modèle capable de détecter la présence de maladies sur les plantes. En ce qui concerne les valeurs manquantes, celles-ci restent significatives et pourraient avoir un impact sur la qualité des prédictions si elles ne sont pas traitées.

    ___Action(s) possible(s) :___ Nous avons décidé d'utiliser le premier dataset uniquement pour l'entraînement des modèles de détection des espèces de plantes. Par conséquent, les valeurs manquantes n'auront aucun impact lors de l'entraînement des modèles pour la détection des maladies, puisque cette étape se concentrera exclusivement sur le second dataset.

    - **Distribution de la hauteur des images :**
    
    ___Observation(s) :___ La majorité des images ont une hauteur inférieure à 500 pixels, mais des valeurs extrêmes allant jusqu'à 3600 pixels sont présentes.
    
    ___Action(s) possible(s) :___ Redimensionnement des images à une taille standard (par exemple 224x224) pour améliorer la cohérence des entrées.

    - **Distribution de la Catégorie "couleur" des images (RGB vs Segmented) :**
    
    ___Observation(s) :___ La majorité des images sont segmentées, tandis qu'une petite fraction est en format RGB (correspondante au DataSet V2 Plant Seedlings), ce qui pourrait affecter la classification.
    
    ___Action(s) possible(s) :___ Conversion de toutes les images dans un même format segmenté (avec fond noir uni) pour améliorer la cohérence des entrées.
    """)