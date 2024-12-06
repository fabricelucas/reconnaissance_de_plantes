import streamlit as st


title = "Projet : Reconnaissance de plantes"
sidebar_name = "Introduction"

def run():

    st.image("streamlit_app/assets/banner.png")

    st.title(title)

    st.markdown("___")

    st.header("1. Contexte du projet")

    st.write("""
        Ce projet de reconnaissance de plantes s’inscrit pleinement dans le métier de Data Scientist. Il participe à la transformation numérique en offrant des solutions pour les particuliers, comme une aide à l’identification des plantes dans leur jardin, et pour les professionnels, notamment dans le secteur agricole. En agriculture, ce type de technologie peut améliorer la gestion des cultures et prévenir les maladies, tandis que dans les services de voirie, il peut contribuer à une gestion écologique optimisée des espaces publics.

        Sur le plan technique, ce projet exploite des méthodes avancées de reconnaissance d’images, en utilisant des réseaux de neurones convolutifs pour la classification des espèces et, à terme, pour l’identification des maladies potentielles. Il intègre également des étapes essentielles de prétraitement des images pour garantir une qualité uniforme des données en entrée. Ces outils de Deep Learning permettent de développer des modèles robustes et performants, capables d’analyser des images de qualité variable.

        D’un point de vue économique, ce projet vise à prévenir les maladies des plantes, permettant ainsi un traitement plus rapide et efficace. Cela peut se traduire par une réduction des pertes de cultures et des économies substantielles pour les particuliers et les exploitants agricoles. Enfin, sur le plan scientifique, l’objectif est de construire un modèle exhaustif et performant qui s’appuie sur des techniques de vision par ordinateur pour analyser des images diversifiées, enrichissant ainsi les recherches sur la flore et sa santé.
        """)

    st.header("2. Objectifs")

    st.write("""
        L’objectif principal de ce projet est de localiser une plante sur une image et de fournir des informations précises sur son espèce. Cette capacité constitue le cœur de l’application et répond au besoin d’identification fiable pour les utilisateurs.
        En complément, le projet vise également à déterminer si une plante est saine ou malade, mais cette partie sera développée dans un second temps. Une fois cette fonctionnalité implémentée, le modèle pourra identifier le type de maladie et son stade, apportant ainsi une aide précieuse pour la gestion et le traitement des cultures.
        Plusieurs outils similaires, comme Pl@ntNet, PlantSnap et PictureThis, ont permis de mieux comprendre les défis et les opportunités de ce projet. Ces applications présentent des fonctionnalités intéressantes mais limitées, notamment l’absence de reconnaissance de maladies, ce qui positionne notre projet comme une solution complémentaire et innovante.
        """)

    st.header("3. Cadre")

    st.write("""
        Ce projet s’appuie sur deux jeux de données principaux. Le premier, le V2 Plant Seedlings Dataset, contient 5 539 images de semis représentant 12 classes courantes en agriculture danoise. Ces images, au format RVB et PNG, varient en taille et permettent d’entraîner le modèle pour la classification des espèces. Le second, le PlantVillage Dataset, a été filtré pour n'utiliser que les images segmentées, offrant ainsi un sous-ensemble pertinent pour notre étude. Ce sous-ensemble contient des feuilles de cultures saines ou malades, réparties en 38 classes.
        En combinant ces deux jeux de données et en ne retenant que les images segmentées pour une cohérence de traitement, le projet s'appuie sur un total de 59 845 images. Cette volumétrie permet d’entraîner et d’évaluer efficacement les modèles, bien que les défis subsistent en raison de la variabilité des images en termes de qualité, notamment des différences de taille, de bruit visuel ... Ces particularités nécessitent un prétraitement minutieux pour assurer des entrées uniformes et fiables dans le pipeline de modélisation.
        """)
