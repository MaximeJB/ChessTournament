# ChessTournament
repository pour mon avancement sur le projet numéro 4 de OC. le tournois d'echec avec de la programation POO

Chess Tournament Manager

Un programme Python permettant de gérer des tournois d'échecs, des joueurs et leurs résultats.


## Prérequis

- Python 3.x

## Installation

1. Clonez le repository sur votre machine locale
```
git clone https://github.com/MaximeJB/ChessTournament.git
cd ChessTournament
```

2. Créez et activez un environnement virtuel (optionnel mais recommandé)
```
python -m venv venv
# Sur Windows
venv\Scripts\activate
# Sur macOS/Linux
source venv/bin/activate
```

3. Installez les dépendances
```
pip install -r requirements.txt
```

## Utilisation

Pour lancer le programme :
```
python main.py
```

Suivez les instructions du menu principal pour naviguer dans l'application.

## Structure des données

Le programme utilise des fichiers JSON pour stocker les données :
- `data/players.json` : Base de données des joueurs
- `data/tournaments/` : Dossier contenant les fichiers de tournois

## Génération du rapport flake8


```
pip install flake8 flake8-html
flake8 --format=html --htmldir=flake8_rapport --max-line-length=119
```

## Structure du code

Le projet suit le modèle MVC (Modèle-Vue-Contrôleur) :
- `models/` : Définition des classes du modèle (Joueur, Tournoi, Tour, Match)
- `views/` : Interfaces utilisateur pour l'affichage et la collecte des données
- `controllers/` : Logique métier reliant les modèles et les vues
- `main.py` : Point d'entrée du programme

