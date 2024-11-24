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
py manage.py runserver 9178