#### USANDO VIRTUALENV ####
# RODAR O PROJETO 
run:
	python manage.py runserver --host 0.0.0.0 --port 5000

upgrade:
	python manage.py db upgrade

# INSTALAR DEPENDENCIAS
deps:
	pip install -r requirements/local.txt

# INICIAR PROJETO USANDO DOCKER
serve:
	sudo docker run -p 2000:5000 residencias

# RODAR TESTES
docker-tests:
	sudo docker-compose run --rm backend py.test --tb=short -s --disable-warnings -k tests/