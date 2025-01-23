# oct24_bds_reconnaissance_de_plantes

## Présentation et Installation

Ce dépôt contient le code de notre projet "Reconnaissance de plantes", développé dans le cadre de notre [formation Data Scientist](https://datascientest.com/formation-data-scientist) chez [DataScientest](https://datascientest.com/).

**Le projet vise à développer une application de reconnaissance de plantes permettant d'identifier une plante sur une image et de fournir des informations sur son espèce. Il s'adresse aux particuliers, pour une aide à l'identification des plantes dans leur jardin, ainsi qu'aux professionnels de l'agriculture pour une gestion optimisée des cultures. Le modèle utilise des réseaux de neurones convolutifs pour la classification des espèces, en se basant sur deux jeux de données principaux. La capacité à diagnostiquer l'état de santé des plantes et détecter des maladies est prévue pour une seconde phase du projet.**

Ce projet a été développé par l'équipe suivante :

- Clara BONINI ([GitHub](https://github.com/clara-bnn))
- Angélique LARCHER ([GitHub](https://github.com/angielx) / [LinkedIn](https://www.linkedin.com/in/ang%C3%A9lique-larcher-9664a412b/))
- Fabrice LUCAS ([GitHub](https://github.com/fabricelucas) / [LinkedIn](https://www.linkedin.com/in/fabrice-lucas-052b3163/))

Vous pouvez consulter et exécuter les [notebooks](./notebooks). 

Vous devrez installer les dépendances (dans un environnement dédié) :

```
pip install -r requirements.txt
```

## Streamlit App

Pour lancer l'application (faites attention aux chemins des fichiers dans l'application) :

```shell
conda create --name projet_plantes_streamlit python=3.9
conda activate projet_plantes_streamlit
pip install -r requirements.txt
streamlit run streamlit/app.py
```

L'application devrait ensuite être disponible à l'adresse suivante : [localhost:8501](http://localhost:8501).