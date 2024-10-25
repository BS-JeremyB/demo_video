# Videotheque Flask Application

Cette application Flask est une vidéothèque permettant d'ajouter des films, de gérer les réalisateurs, d'afficher les films avec leurs réalisateurs associés, et de gérer les utilisateurs. Elle utilise **Flask**, **SQLAlchemy**, **Flask-Migrate**, **Flask-WTF** et **Flask-Login** pour la gestion des données, des formulaires, des utilisateurs, et des sessions de connexion.

## Fonctionnalités

- Ajouter des films
- Ajouter des réalisateurs
- Afficher la liste des films avec les réalisateurs
- Gestion des utilisateurs avec système de connexion et de déconnexion
- Utilisation de PostgreSQL comme base de données
- Gestion des migrations avec Flask-Migrate
- Utilisation de formulaires avec Flask-WTF
- Sécurisation des pages et personnalisation du contenu pour les utilisateurs connectés

## Prérequis

- Python 3.x
- PostgreSQL

## Installation

### 1. Cloner le projet ou créer manuellement la structure

Clone le dépôt Git ou crée manuellement la structure des fichiers comme décrit dans le projet.

```bash
git clone <repository-url>
cd videotheque
```

### 2. Créer un environnement virtuel

Crée un environnement virtuel pour isoler les dépendances du projet.

```bash
python -m venv venv
```

Active l'environnement virtuel :

- Sur **Windows** :
  
  ```bash
  .\\venv\\Scripts\\activate
  ```

- Sur **Mac/Linux** :
  
  ```bash
  source venv/bin/activate
  ```

### 3. Installer les dépendances

Installe les dépendances Python nécessaires à l'application.

```bash
pip install -r requirements.txt
```

### 4. Configurer la base de données

Modifie le fichier `config.py` pour indiquer tes informations de base de données PostgreSQL.

```python
class Config:
    SECRET_KEY = 'dev_secret_key'
    SQLALCHEMY_DATABASE_URI = 'postgresql://<username>:<password>@localhost/<dbname>'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

Assure-toi que PostgreSQL est installé et qu'une base de données est créée.

### 5. Initialiser la base de données

Initialise les migrations de la base de données avec Flask-Migrate, puis applique les migrations pour créer les tables dans la base de données.

```bash
flask db init
flask db migrate
flask db upgrade
```

### 6. Lancer l'application

Lance l'application en mode développement avec la commande suivante :

```bash
flask run
```

L'application sera disponible à l'adresse suivante : `http://127.0.0.1:5000`.


## Dépendances

- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-WTF
- Flask-Login
- psycopg2-binary

## Auteurs

- Jérémy Bazin
