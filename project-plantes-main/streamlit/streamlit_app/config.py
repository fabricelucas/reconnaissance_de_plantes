"""

Fichier config pour l'application Streamlit reconnaissance des plantes

"""

from .member import Member

TITLE = "Projet : Reconnaissance de plantes"

TEAM_MEMBERS = [
    Member(
        name="Clara BONINI",

        github_url="https://github.com/clara-bnn",
    ),

    Member(
        name="Angélique LARCHER",
        linkedin_url="https://www.linkedin.com/in/ang%C3%A9lique-larcher-9664a412b/",
        github_url="https://github.com/angielx",
    ),
    
    Member(
        name="Fabrice LUCAS",
        linkedin_url="https://www.linkedin.com/in/fabrice-lucas-052b3163/",
        github_url="https://github.com/fabricelucas",
    )
    
]

PROMOTION = "Promotion Bootcamp Data Scientist - Octobre 2024"

DATASET1 = "[V2 Plant Seedlings Dataset](https://www.kaggle.com/datasets/vbookshelf/v2-plant-seedlings-dataset)"

DATASET2 = "[PlantVillage Dataset](https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset)"
