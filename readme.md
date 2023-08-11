python version: 3.10.12

INSTALL

- Clone the repo
- Create a virtual env
- Install dependencies      => pip install -r requirements.txt
- Configure MySQL           => Create a mysql database and add the required fields in the settings.py file
- Remove Prev Migrations    => As the requirements required the migrations to be visible, you will have to delete the previous requirements to view run the app. Remove all files from migrations/ except for the __init__.py files.

- Make migrations           => python manage.py makemigrations
- Migrate                   => python manage.py migrate
- Create Super User         => python manage.py createsuperuser
- Run the server            => python manage.py runserver


Here is an example of settings for mysql in settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mobileapi',
        'USER': 'root',
        'PASSWORD': 'mypassword',
        'PORT': '3306'
    }
}



API

- Get units:
 /units/phone-number/   GET

 Response:

 [
    {
        'pk': int,      # Primary key of unit
        'name': str     # Name of unit
    }
 ]


- Make visit:
 /visit/phone-number/   POST
 body: {
    'pk: int,           # Primary key of unit
    'coordinates': {
        'latitude': float,
        'longitide': float
    }
 }

 Response:

 [
    {
        'pk': int,      # Primary key of visit
        'date_time': datetime
    }
 ]