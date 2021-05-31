#### USANDO VIRTUALENV ####
# RODAR O PROJETO 
run:
	python manage.py runserver --host 0.0.0.0 --port 5000

migrate:
	python manage.py db migrate

upgrade:
	python manage.py db upgrade

# INSTALAR DEPENDENCIAS
deps:
	pip install -r requirements/local.txt

# INICIAR PROJETO USANDO DOCKER
serve:
	sudo docker run -p 2000:5000 zap

# RODAR TESTES
docker-tests:
	sudo docker-compose run --rm backend py.test --tb=short -s --disable-warnings -k tests/