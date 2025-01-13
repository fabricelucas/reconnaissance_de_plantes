import streamlit as st
import pandas as pd

title = "Conclusion"
sidebar_name = "Conclusion"

def run():

    st.image("streamlit_app/assets/banner.png")

    st.title(title)

    st.markdown(
        """
        <hr class="hr">
        """,
        unsafe_allow_html=True
    )

    data = {
        "Modèle": ["EfficientNetB3", "ResNet50", "MobileNet", "From Scratch (LeNet)"],
        "Résultat": [
            "Meilleur équilibre précision/performance",
            "Exigeant mais très performant",
            "Idéal pour ressources limitées",
            "Amélioration possible avec preprocessing en adéquation"
        ]
    }

    df = pd.DataFrame(data)
    df.set_index("Modèle", inplace=True)
    st.dataframe(df)

    st.markdown("**Pistes d'améliorations**")

    st.write("""
    *Interface utilisateur :*  
            -> Intégration d'une fonction pour importer des photos personnelles.  
            -> Conseils d’entretien personnalisés pour les plantes identifiées.  
    
    *Surbrillance des plantes :*  
            -> Implémentation d'un contour en surbrillance pour délimiter les plantes.  
    
    *Détection des maladies :*  
            -> Identification des maladies avec détails sur le traitement recommandé.  
    """)

    
    st.markdown("**Merci pour votre attention. Nous avons planté des idées aujourd’hui, à vous de les faire fleurir avec vos questions !**")
