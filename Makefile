static:
	python builder/manage.py collectstatic

migrations:
	python builder/manage.py makemigrations

migrate:
	python builder/manage.py migrate

webserver:
	python -m http.server 9000
