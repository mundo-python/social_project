# Estos son los archivos iniciales del proyecto

## Este proyecto corresponde al tutorial de youtube: 

#### Para utilizarlo/configurarlo:

1. Clona el repositorio o descargalo como zip.

```git clone https://github.com/mundo-python/social_project.git```


2. Crea un ambiente virtual 

```python -m venv socialenv```


3. Instala las dependencias/librerias en requirements.txt

```pip install -r requirements.txt```


4. Ejecuta las migraciones.

```python manage.py makemigrations```
```python manage.py migrate```


5. Crea un superusuario.

```python manage.py createsuperuser```

6. Corre el servidor.

```python manage.py runserver```