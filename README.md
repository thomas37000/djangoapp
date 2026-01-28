# Djangoapp

Juste une app Django avec PostgreSql pour apprendre et pratiquer

## Installation

```bash

1/ lancer le serveur local et activer
    python -m venv .venv 
    .\.venv\Scripts\activate
    python -m pip install django

2/ Django (pour initialiser / créez les dossiers et fichiers python / Django)
    django-admin startproject “nomduProjet”

3/ pour initialiser / créez les dossiers et fichiers API python / Django
(api, ça peut être n’importe quel nom mais par convention api par rapport au rest api)


cd nomDuProjet
python manage.py startapp api

4/ ajouter api, rest_framework et cors-header dans settings.py:
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "api",
    "cors-header",
]

 5/ remplacer sqlite3 par postgresql et ajouter le nom de la BDD et les autres champs USER / PASSWORD / HOST et PORT
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "nomDeLaBDD", # ex djangoapp
    }
}

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "djangoapp",
        "USER":"postgres",
        "PASSWORD":"azerty123",
        "HOST":"localhost",
        "PORT":"5432"
    }
}


5/ créez requirements.txt
	django
    psycopg2

    pip install -r requirements.txt
    pip install psycopg2-binary
    pip install djangorestframework
    python -m pip install python-dotenv

6/ créer le serializers.py dans /api pour créer les champs d’une ou plusieurs tables et refresh dans pgadmin4
    python manage.py makemigrations
    python manage.py migrate

7/crééz un SUPERUSER
    python manage.py createsuperuser
    superuser votre nom

8/ install cors header pour le frontend ( React / Vue / Angular )
    pip install django-cors-headers

9/ python manage.py runserver
```

### Testez
    http://127.0.0.1:8000/admin