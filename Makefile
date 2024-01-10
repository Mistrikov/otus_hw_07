runserver:
	python manage.py runserver 0.0.0.0:8000 #192.168.1.253:8000 

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

test:
	python manage.py test

coverage:
	coverage run --source='.' manage.py test
	coverage report --omit=settings/asgi.py,settings/wsgi.py,manage.py,mainapp/management/* --fail-under=80
	coverage html --omit=settings/asgi.py,settings/wsgi.py,manage.py,mainapp/management/*
	