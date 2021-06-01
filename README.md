# Teste WIPRO - ITAU
## API feita em Flask para manipulação de Data Frames e entrega dos dados em JSON
<img src="https://img.shields.io/badge/Flask-v1.0.2-blue"/> <img src="https://img.shields.io/badge/PyTest-v5.4.3-yellow"/> <img src="https://img.shields.io/badge/marshmallow-v3.12.1-orange"/>



# Como rodar localmente
Primeiramente é necessário ter uma virtualenv usando python 3.6:

[https://pypi.org/project/virtualenv/](https://pypi.org/project/virtualenv/)

Para ativar o ambiente é só entrar no diretório raiz da env que foi criada e rodar o comando:

##### source bin/activate

Agora será preciso instalar as dependencias do projeto:

##### pip install -r requirements/local.txt

Também será necessário adicinar uma variavel de ambiente

##### export FLASK_APP=backend.__ini__.py

Agora é a hora de criar, migrar e atualizar o banco, usando os comandos abaixo seguidos um do outro:

##### flask db init
##### flask db migrate
##### flask db upgrade

Agora é a hora de rodarmos o script para manipular e persistir no banco os dados gerados. Na pasta raiz do projeto (onde encontra o arquivo **manage.py**)

##### python manage.py run_bases

Esse provesso pode demorar um pouco devido a quantidade de registro. Num cenário ideial seria interessando colocar num lambda (AWS), ou realizar de forma assincrona com um **celery**, por exemplo.

Com todos esses passos criados, a API já esta pronta para ser consumida. Use o comando **flask run** e acesse os endpoints:

[http://127.0.0.1:5000/v1/api/wipro/residencias](http://127.0.0.1:5000/v1/api/wipro/residencias)
[http://127.0.0.1:5000/v1/api/wipro/preco-medio](http://127.0.0.1:5000/v1/api/wipro/preco-medio)
[http://127.0.0.1:5000/v1/api/wipro/like](http://127.0.0.1:5000/v1/api/wipro/like)

# Como rodar os testes

Os testes são simbólicos, apenas para efeitos demonstrativos de como usa-los. Foram criados dois testes de integração que verificam se o retorna da API é 200, indicando que está tudo ok
Na pasta raiz use o comando
##### pytest


### Considerações finais
Esse projeto é simples e tem por finalidade demonstrar um pouco dos meus conhecimentos e estilo de trabalho. Tenho muito a aprender e experiencia para adquirir, mas acredito que todos nós podemos ter trocas de informações e que todos podemos aprender um pouquinho com nossos colegas de trabalhos.
