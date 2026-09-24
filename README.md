# Projet 05 - Prediction de consommation energetique des batiments

> Formation Data Engineer - OpenClassrooms | Outils : Python, Scikit-learn, BentoML, JupyterLab

## Objectif

Anticiper les besoins en consommation energetique de batiments de la ville de Seattle a partir de donnees de benchmarking energetique (2016). Le projet inclut l'entrainement d'un modele de Machine Learning et son deploiement via une API REST avec BentoML.

## Competences travaillees

- Analyse exploratoire et nettoyage de donnees
- Entrainement de modeles de regression (scikit-learn)
- Evaluation et selection de modele
- Deploiement d'un modele ML via API REST avec BentoML

## Contenu du repo

- Projet 06.ipynb : notebook d'analyse et d'entrainement du modele
- service.py : service BentoML pour le deploiement de l'API
- bentofile.yaml : configuration du build BentoML
- Selmen_Oumayma_2_presentation_012026.pptx : support de presentation

## Donnees

Dataset Seattle Building Energy Benchmarking 2016 - non inclus dans ce repo.
Source : https://data.seattle.gov/

## Lancer le service

Installer les dependances :
pip install -r requirements.txt

Lancer le service BentoML :
bentoml serve service:svc

## Résultats
    Modèle de machine learning de prédiction exposé en API
---
Formation Data Engineer - OpenClassrooms
