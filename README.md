# Code Challenge Grupo ZAP
## API feita em Flask para integrar as plataformas Zap e Viva Real
<img src="https://img.shields.io/badge/Flask-v1.0.2-blue"/> <img src="https://img.shields.io/badge/PyTest-v5.4.3-yellow"/> <img src="https://img.shields.io/badge/marshmallow-v3.12.1-orange"/>



# Como rodar localmente
O projeto esta rodando com Docker, caso não tenha ainda o Docker instalado em sua máquina, basta seguir o step by step proposto pela propria documentação oficial do Docker, link abaixo:

[https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)

Com o Docker instalado precisamos criar a imagem:

##### docker build -t zap-code-challenger .

Com sua imagem pronta, basta inicializar o container:

##### docker run -p 2000:5000 zap-code-challenger

Poderá ter acesso aos endpoints para consulta da API:

[http://localhost:2000/v1/code_challenger/zap_imoveis](http://localhost:2000/v1/code_challenger/zap_imoveis)

[http://localhost:2000/v1/code_challenger/viva_real](http://localhost:2000/v1/code_challenger/viva_real)

# Como rodar os testes
O projeto usa o docker compose para rodar os testes, basta rodar o comando:
##### docker-compose run --rm backend py.test --tb=short -s --disable-warnings -k tests/

# Como fazer deploy
Para colocar o projeto em produção usei o Heroku para hospedar a api.

Primeiramente é preciso ter uma conta no Heroku:

[https://www.heroku.com/](https://www.heroku.com/)

No terminal use o comando para se logar no Heroku:
##### heroku login

Também é necessário a criação de um arquivo manifesto "heroku.yml" usado para algumas configurações de deploy. Pode ser visto esse arquivo na raiz do projeto com as configurações básicas para subir em produção.

Como próximo passo será necessário a criação do app para o Heroku:
##### heroku create code-zap-challenger

E também criar uma branch remota
##### git remote add 'branch-name' 'app-link'

Como o projeto está rodando em container, é preciso deixar explicito ao Heroku isso, para configurações internas da plataforma:
##### heroku stack:set container

E por último, mas não menos importante, o deploy de fato da aplicação
##### git push heroku master

Esse passo já está completo e pode ser acessado pelos endpoints

[https://grupozap-challenger.herokuapp.com/v1/code_challenger/zap_imoveis](https://grupozap-challenger.herokuapp.com/v1/code_challenger/zap_imoveis
)

[https://grupozap-challenger.herokuapp.com/v1/code_challenger/viva_real](https://grupozap-challenger.herokuapp.com/v1/code_challenger/viva_real)

### Considerações finais
O primeiro request tende a ser um pouco mais demorado por carregar um source de milhares de registros. Após o primeiro request esses dados são guardados em memória e pode ser usado de maneira muito mais rápida.

O Heroku fornece upload de aplicações gratuitas e para isso ele desliga a máquina tempos após não ser utilizada, mas pode ficar tranquilo que assim que a aplicação requebe um request ele trata de liga-lá, e isso também custa alguns poucos segundos.
