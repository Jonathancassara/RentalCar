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

python manage.py runserver
```

## Authors

- [@jonathancassara](https://www.github.com/jonathancassara)

## TODO

- TimeZone UTC
- check phone number / email si deja dans la DB 
- check if customers are already in DB 
- ajoute commentaire ( option none )  
- check format email 
-  Ajoute pied page Footer
- ajouter Header 

bug : 
Driver: 
Add  : 
- probleme modal , no pop up 
List : 
- colonne  Surname !  
- fix remove dont work ! 

rentals : 
Add
-date rent :  no past !  TODAY  ,  pas + 7 jours ; attention si weekend !  
Modify :
-not working ! 
Finish :
-  modal comments or none quand user finish !   
-finish not working 
-visual  no car ??? 
-comment no  visible 
List :
-design !
-update ????  
-delete with modal confirmation !!!! 

Car:
remove :
liste avec modification  et delete 
modal de confirmation






