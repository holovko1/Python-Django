# python_web MVC

py --version
python -m venv .venv
.venv\Scripts\activate.bat
deactivate

code .
Install
    Django
    vscode-icons

.venv\Scripts\activate.bat
py -m pip install Django
py -m pip install -U pip
py
>>> import django
>>> print(django.get_version())
>>> quit()

django-admin startproject blog
cd blog
py manage.py runserver

----------App and Templates----------
.venv\Scripts\activate.bat
cd blog
py manage.py startapp posts
py manage.py runserver

py manage.py migrate
py manage.py makemigrations
py manage.py migrate

----------Testing Django ORM----------
py manage.py shell
>>> from posts.models import Post
>>> p=Post()
>>> p
>>> p.title="Перша новина. Привіт світ!"
>>> p.save()
>>> Post.objects.all()
>>> exit()

----------Model Post and str----------
py manage.py shell
>>> from posts.models import Post
>>> p=Post()
>>> p
>>> p.title="Друга новина. Вареники з чорницею!"
>>> p.save()
>>> Post.objects.all()
>>> exit()

----------Django Admin---------
py manage.py runserver
http://127.0.0.1:8000/admin
ctrl+c
py manage.py createsuperuser

User: dev
Password: Qwertry123