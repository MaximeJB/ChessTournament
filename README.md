# ChessTournamentManager

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

3. Installez les dépendances (Ici que des bibliothèques pré-installées)
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
- 

## Rapport flake8 de ChessTournament

```bash
.\controllers.py:58:80: E501 line too long (80 > 79 characters)
.\controllers.py:64:80: E501 line too long (88 > 79 characters)
.\controllers.py:114:80: E501 line too long (80 > 79 characters)
.\controllers.py:117:80: E501 line too long (80 > 79 characters)
.\models.py:9:1: E303 too many blank lines (3)
.\models.py:39:80: E501 line too long (83 > 79 characters)
.\models.py:155:80: E501 line too long (81 > 79 characters)
.\models.py:196:80: E501 line too long (104 > 79 characters)
.\models.py:201:80: E501 line too long (83 > 79 characters)
.\models.py:221:80: E501 line too long (83 > 79 characters)
.\models.py:263:80: E501 line too long (86 > 79 characters)
.\models.py:267:80: E501 line too long (86 > 79 characters)
.\models.py:276:80: E501 line too long (84 > 79 characters)
.\models.py:315:80: E501 line too long (86 > 79 characters)
.\models.py:316:80: E501 line too long (93 > 79 characters)
.\models.py:332:80: E501 line too long (81 > 79 characters)
.\models.py:344:1: W293 blank line contains whitespace
.\models.py:348:80: E501 line too long (82 > 79 characters)
.\models.py:356:80: E501 line too long (83 > 79 characters)
.\views.py:11:80: E501 line too long (81 > 79 characters)
.\views.py:19:26: W291 trailing whitespace
.\views.py:42:1: W293 blank line contains whitespace
.\views.py:46:25: W291 trailing whitespace
.\views.py:57:44: W291 trailing whitespace
.\views.py:58:1: W293 blank line contains whitespace
.\views.py:59:27: W291 trailing whitespace
.\views.py:60:26: W291 trailing whitespace
.\views.py:66:80: E501 line too long (80 > 79 characters)
.\views.py:72:80: E501 line too long (87 > 79 characters)
.\views.py:73:80: E501 line too long (86 > 79 characters)
.\views.py:84:1: W293 blank line contains whitespace
.\views.py:87:32: W291 trailing whitespace
.\views.py:88:80: E501 line too long (86 > 79 characters)
.\views.py:90:1: W293 blank line contains whitespace
.\views.py:99:16: W291 trailing whitespace
.\views.py:100:33: W291 trailing whitespace
.\views.py:101:1: W293 blank line contains whitespace
.\views.py:104:1: W293 blank line contains whitespace
.\views.py:150:80: E501 line too long (87 > 79 characters)
.\views.py:177:80: E501 line too long (86 > 79 characters)
.\views.py:189:80: E501 line too long (90 > 79 characters)
.\views.py:232:22: W291 trailing whitespace
.\views.py:254:16: W291 trailing whitespace
.\views.py:255:1: W293 blank line contains whitespace
.\views.py:256:57: W291 trailing whitespace
.\views.py:257:56: W291 trailing whitespace
.\views.py:259:23: W291 trailing whitespace
.\views.py:261:1: W293 blank line contains whitespace
.\views.py:267:80: E501 line too long (88 > 79 characters)
.\views.py:272:80: E501 line too long (88 > 79 characters)
.\views.py:288:80: E501 line too long (85 > 79 characters)
.\views.py:304:80: E501 line too long (82 > 79 characters)
.\views.py:324:80: E501 line too long (83 > 79 characters)
.\views.py:327:80: E501 line too long (83 > 79 characters)
.\views.py:330:80: E501 line too long (83 > 79 characters)
.\views.py:339:80: E501 line too long (80 > 79 characters)


