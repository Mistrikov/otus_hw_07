runserver:
	python manage.py runserver 0.0.0.0:8000

newapp:
	python manage.py startapp $(appname)

makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

createsuperuser:
	python manage.py createsuperuser

fill_db:
	python manage.py fill_db