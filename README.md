# Project_HackJKLU_2.0
 The Project we made during HackJKLU 2.0


### Setup Commands
mysql >

    CREATE DATABASE farmConnect;
	GRANT ALL ON farmConnect.* TO 'yarr'@'localhost';
	FLUSH PRIVILEGES;

python >

	py manage.py makemigrations
	py manage.py migrate
	py manage.py createsuperuser

django-admin >

	Create Groups `farmers` & `consumers`
	Create Test Users `farmer001` & `consumer001`