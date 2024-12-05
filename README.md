
# Mini Blog Django

## Description

Mini Blog est une application web développée avec Django permettant de gérer des articles de blog et leurs commentaires.
L'application offre les fonctionnalités suivantes :
- Création, modification, affichage et suppression d'articles de blog.
- Ajout, modification et suppression de commentaires associés aux articles.
- Une interface intuitive avec des modèles HTML extensibles.

Ce projet est conçu pour illustrer les bonnes pratiques avec l'architecture Modèle-Vue-Modèle (MVT) de Django.

---

## Installation et configuration

### Prérequis
Avant de commencer, assurez-vous d'avoir les éléments suivants installés :
- **Python 3.8 ou supérieur**
- **Pip** pour gérer les dépendances
- **Django 4.0 ou supérieur** (inclus dans `requirements.txt`)

### Étape 1 : Cloner le dépôt
Clonez ce dépôt sur votre machine locale :
```bash
git clone <URL_DU_DÉPÔT>
cd MiniBlog
```

### Étape 2 : Créer un environnement virtuel
Créez un environnement virtuel Python pour isoler les dépendances :
```bash
python -m venv venv
source venv/bin/activate  # Pour Linux/Mac
venv\Scripts\activate   # Pour Windows
```

### Étape 3 : Installer les dépendances
Installez Django et les autres dépendances à partir du fichier `requirements.txt` :
```bash
pip install -r requirements.txt
```

### Étape 4 : Configurer la base de données
Appliquez les migrations pour initialiser la base de données SQLite :
```bash
python manage.py makemigrations
python manage.py migrate
```

### Étape 5 : Lancer le serveur local
Démarrez le serveur de développement Django :
```bash
python manage.py runserver
```
Ouvrez votre navigateur et rendez-vous sur [http://127.0.0.1:8000/](http://127.0.0.1:8000/) pour accéder à l'application.

---

## Structure du projet

```
MiniBlog/
├── blog/
│   ├── migrations/       # Migrations de la base de données
│   ├── templates/        # Modèles HTML
│   │   ├── blog/         # Templates spécifiques à l'application blog
│   │       ├── base.html
│   │       ├── post_list.html
│   │       ├── post_detail.html
│   │       ├── create_post.html
│   │       ├── edit_post.html
│   │       ├── delete_post.html
│   │       ├── add_comment.html
│   │       ├── edit_comment.html
│   │       ├── delete_comment.html
│   ├── admin.py          # Configuration de l'administration Django
│   ├── apps.py           # Configuration de l'application blog
│   ├── forms.py          # Définition des formulaires
│   ├── models.py         # Modèles de la base de données
│   ├── tests.py          # Tests automatisés
│   ├── urls.py           # Routage de l'application blog
│   ├── views.py          # Vues Django (logique métier)
├── MiniBlog/
│   ├── settings.py       # Configuration globale du projet
│   ├── urls.py           # Routage principal
│   ├── wsgi.py           # Interface avec le serveur WSGI
├── db.sqlite3            # Base de données SQLite (créée après migrations)
├── manage.py             # Commande principale pour gérer le projet
└── requirements.txt      # Liste des dépendances Python
```

---

## Auteur
Ce projet a été conçu pour apprendre Django et explorer les fonctionnalités MVT d'une application web. Si vous avez des questions ou souhaitez contribuer, n'hésitez pas à ouvrir une issue.

