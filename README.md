# Rental Car

Exercice Project [NOT USE]



## Deployment

To deploy this project run

```bash
  STEP BY STEP

Install Python 3.12 (test 3.13 ok)
# Créez un environnement virtuel
python -m venv venv

# Activez l'environnement virtuel
# Sur Linux/Mac
source venv/bin/activate

# Sur Windows
venv\Scripts\activate

# Installez Django
pip install django

# Créez le projet RentalCar
django-admin startproject RentalCar .

# Créez l'application Frontend
python manage.py startapp Frontend

CREATE DATABASE RentalCarDB;

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

pip freeze > requirements.txt

pip install -r /path/to/requirements.txt
```

## Authors

- [@jonathancassara](https://www.github.com/jonathancassara)

## TODO






