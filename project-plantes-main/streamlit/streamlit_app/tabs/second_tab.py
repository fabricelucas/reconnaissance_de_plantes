import streamlit as st
import pandas as pd
import plotly.express as px

title = "Étape 1 - Exploration des données & DataVizualisation"
sidebar_name = "Exploration"

def run():

    st.header(title)

    st.markdown("___")

    st.subheader("Présentation des jeux de données utilisés")

    data = {
        "Jeu de données": ["V2 Plant Seedlings Dataset", "New Plant Diseases Dataset"],
        "Nombre d'images": ["5 539", "87 000 (filtré à 59 845)"],
        "Classes": ["12 (espèces courantes)", "38 (sain/malade)"],
        "Format": ["RVB, PNG", "RVB, segmenté"],
    }

    data = pd.DataFrame(data)
    data.set_index("Jeu de données", inplace=True)
    st.dataframe(data)

    st.image("streamlit_app/assets/datasets.png")


    # Chargement des données
    df = pd.read_csv('data\dataframe_plant_disease_id.csv')

    # Affichage du DataFrame et de ses caractéristiques
    st.subheader("Aperçu des données")
    st.write("**Premières lignes du DataFrame (V2 Plant Seedlings Dataset) :**")
    st.dataframe(df.head(5))
    st.write("**Dernières lignes du DataFrame (New Plant Diseases Dataset):**")
    st.dataframe(df.tail(5))
    
    st.write("**Résumé statistique du DataFrame :**")
    st.dataframe(df.describe())

    st.write("**Taille du DataFrame :**", df.shape)

    # Visualisations des données
    st.subheader("Visualisations des données et analyses des graphiques")

    # Affichage d'une heatmap pour visualiser les valeurs manquantes
    heatmap_fig = px.imshow(df.isna(), color_continuous_scale='greens')
    heatmap_fig.update_layout(title='Valeurs manquantes dans le DataFrame')
    st.plotly_chart(heatmap_fig)

    # Calculer le pourcentage de valeurs manquantes dans le DataFrame
    valeurs_manquantes_etat = df['état'].isna().sum()
    valeurs_manquantes_etat_pourcent = round(((valeurs_manquantes_etat / len(df)) * 100), 2)

    st.write(f"Nombre de valeurs manquantes dans la colonne 'état' : {valeurs_manquantes_etat}")
    st.write(f"Pourcentage de valeurs manquantes dans la colonne 'état' : {valeurs_manquantes_etat_pourcent}%")

    # Visualisation de la distribution des espèces de plantes au niveau du DataFrame
    especes_fig = px.histogram(df, x='espèce', title="Distribution des espèces de plantes", color_discrete_sequence=['#347d7b'])
    especes_fig.update_xaxes(title="Espèce de la plante", tickangle=45)
    especes_fig.update_yaxes(title="Nombre d'images")
    st.plotly_chart(especes_fig)

    # Calcul de la proportion représentant l'espèce 'Tomato' au niveau du DataFrame
    valeurs_tomate = (df['espèce'] == 'Tomato').sum()
    valeurs_tomate_pourcent = round((valeurs_tomate / len(df)) * 100, 2)
    st.write(f"Pourcentage de plantes de type 'Tomato' : {valeurs_tomate_pourcent}%")

    # Visualisation de la distribution des états de plantes au niveau du DataFrame
    etat_fig = px.histogram(df, x='état', title="Distribution des états de plantes", color_discrete_sequence=['#8acbc0'])
    etat_fig.update_xaxes(title="État de la plante", tickangle=45)
    etat_fig.update_yaxes(title="Nombre d'images")
    st.plotly_chart(etat_fig)

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

    # Visualisation de la distribution des hauteurs des images au niveau du DataFrame
    hauteur_fig = px.histogram(df, x='hauteur', nbins=50, title="Distribution des hauteurs des images", color_discrete_sequence=['#347d7b'])
    hauteur_fig.update_xaxes(title="Hauteur de l'image (pixels)")
    hauteur_fig.update_yaxes(title="Nombre d'images")
    st.plotly_chart(hauteur_fig)

    # Visualisation de la distribution de la catégorie 'couleur' des images au niveau du DataFrame
    couleur_fig = px.histogram(df, x='couleur', nbins=2, title="Distribution de la catégorie 'couleur' des images", color_discrete_sequence=['#8acbc0'])
    couleur_fig.update_xaxes(title="Catégorie de la 'couleur'", tickvals=[0, 1], ticktext=['RGB', 'Segmented'])
    couleur_fig.update_yaxes(title="Nombre d'images")
    couleur_fig.update_layout(bargap=0.5)
    st.plotly_chart(couleur_fig)

    # Affichage d'une image RGB et d'une image segmentée
    col1, col2 = st.columns(2)

    # Image RGB 
    with col1:
        st.write("Exemple d'une image RGB (Cleaver - DataSet V2 Plant Seedlings) :")
        st.image("streamlit_app/assets/img_rgb.png", width=200)

    # Image segmentée
    with col2:
        st.write("Exemple d'une image segmentée (Framboisier sain - DataSet PlantVillage) :")
        st.image("streamlit_app/assets/img_seg.jpg", width=200)
