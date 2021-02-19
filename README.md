# Alura Receita

👋 Olá, Seja Bem-vindo(a) ao 'Alura Receita'.

# Projeto 'Alura Receita' do curso ['Introdução ao Django 3: Modelo, Rotas e Views'](https://cursos.alura.com.br/course/fundamentos-django-2):

# Aulas

###  Introdução  
* Saudações e Ambiente  
* Django e venv  
* Projeto e subindo servidor  
* Servidor e app de receita  
* Faça como eu fiz na aula  
* Benefícios da venv  
* Projeto e app  
* Para saber mais: Django  
* O que aprendemos?  

## Template, rotas e views
* Criando a pasta template
* Preparando o ambiente
* Arquivos estáticos
* Carregando estáticos
* Faça como eu fiz na aula
* Configurando estáticos
* {% load static %}
* Para saber mais: Templates
* O que aprendemos?

## Links, extends e partials
* Links, urls e views
* Estendendo html
* Partials
* Faça como eu fiz na aula
* Extends, include e partials
* O que aprendemos?

## Modelo e banco de dados
* Nomes de receitas dinâmicas
* Banco de dados
* Psycopg2
* Modelo de receita
* Faça como eu fiz na aula
* {{ }} e {% %}
* Models no Django
* makemigration e migrate
* Para saber mais: Models
* O que aprendemos?

## Admin, parâmetros e receitas
* Django Admin
* Exibindo dados dos banco
* Parâmetro na url
* Faça como eu fiz na aula
* Ajudando alguém
* Para saber mais
* O que aprendemos?
* Conclusão
* Parabéns

## Sobre o projeto:

### Permissões de arquivos:

Ao se criar migrações, adicionar libs ou qualquer outro comando que crie arquivos dentro do contâiner Docker o proprietário para edição se torna o contâiner, sendo assim você precisará rodar o comando abaixo para alterar essas permissões e você poder editar:

```sh
sudo chown -R $USER:$USER .
```

# Exigências

**:warning: Atenção:** É necessário que os desenvolvedores usem o Docker no seu ambiente de desenvolvimento.

- **🛠 Modo Desenvolvimento Docker**
    - :computer: [Linux Ubuntu LTS](https://ubuntu.com/download/desktop)
    - 🐳 [Docker](https://docs.docker.com/engine/installation/) Deve estar instalado.
    - 🐳 [Docker Compose](https://docs.docker.com/compose/) Deve estar instalado.
    - **💡 Dica:** [Documentação do Docker](https://docs.docker.com/)

# Instalando

## 🐳 Modo Desenvolvimento com Docker

Após instalar o docker e docker-compose, estando na pasta raiz do projeto, execute:

```sh
docker-compose up
```

Para se certificar que os seus containers subiram corretamente, todos os containers deve estar com o status `UP`, execute:

```sh
docker-compose ps -a
```

Para acessar o container da aplicação, execute:

```sh
docker-compose run --rm web bash
```

Para acessar a instância do banco de dados, execute:

```sh
docker exec-it [nome do db] bash
```

Para derrubar e subir a instância do docker novamente, execute:

```sh
docker-compose down && docker-compose up
```

🚀 :clap: Para visualizar o sistema basta acessar no navegador no endereço: [localhost:8000](localhost:8000)

# Referências utilizadas

[1° Como criar uma aplicação Django com Docker](https://github.com/claudimf/django-docker)