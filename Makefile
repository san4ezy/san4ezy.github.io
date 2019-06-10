static:
	python manage.py collectstatic

migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

webserver:
	python -m http.server 9000
