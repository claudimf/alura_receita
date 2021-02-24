# Alura Receita

👋 Olá, Seja Bem-vindo(a) ao 'Alura Receita'.

# Projeto 'Alura Receita' da [formação de Django](https://cursos.alura.com.br/formacao-django)

![homepage](https://raw.githubusercontent.com/claudimf/alura_receita/main/homepage.png)

# Aulas

## Curso ['Introdução ao Django 3: Modelo, Rotas e Views'](https://cursos.alura.com.br/course/fundamentos-django-2)

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

### Template, rotas e views
* Criando a pasta template
* Preparando o ambiente
* Arquivos estáticos
* Carregando estáticos
* Faça como eu fiz na aula
* Configurando estáticos
* {% load static %}
* Para saber mais: Templates
* O que aprendemos?

### Links, extends e partials
* Links, urls e views
* Estendendo html
* Partials
* Faça como eu fiz na aula
* Extends, include e partials
* O que aprendemos?

### Modelo e banco de dados
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

### Admin, parâmetros e receitas
* Django Admin
* Exibindo dados dos banco
* Parâmetro na url
* Faça como eu fiz na aula
* Ajudando alguém
* Para saber mais
* O que aprendemos?
* Conclusão
* Parabéns

## Curso ['Integração de modelos no Django 3: Filtros, buscas e admin'](https://cursos.alura.com.br/course/integracao-modelos-django-2)

## Ajustando o Django admin
* Introdução
* Saudações e Ambiente
* Listando receitas por nome
* Busca, Filtros e paginação
* Faça como eu fiz na aula
* Melhorando o admin
* O que aprendemos?

## Quem postou a receita?
* Criando um modelo de pessoas
* Integrando modelos
* Exibindo nome das pessoas
* Faça como eu fiz na aula
* __str__
* O que aprendemos?

## Filtros e categorias
* Filtro receitas publicadas
* Ordenação e edição no admin
* Foto para cada receita
* Faça como eu fiz na aula
* Configurações do Admin
* O que aprendemos?

## Buscando receitas
* Exibindo a foto
* Criando a página de busca
* Resultado da busca
* Faça como eu fiz na aula
* Foto no banco de dados
* O que aprendemos?

## Autorização e melhorando o código
* Autorização e usuários
* Partial e refatoração
* Faça como eu fiz na aula
* Template tags
* O que aprendemos?
* Conclusão
* Parabéns

## Curso ['Autenticação no Django 3: formulários, requisições e mensagens'](https://cursos.alura.com.br/course/autenticacao-django-2)

## App de usuários Ver primeiro vídeo
* Introdução
* Saudações e ambiente
* Criando o app de usuários
* Material do curso
* Cadastro e login
* Faça como eu fiz na aula
* Renderizando as páginas
* O que aprendemos?

## Formulário no Django
* Requisições no Django
* CSRF, token e dados
* Criando usuários
* Faça como eu fiz na aula
* Token CSRF
* O que aprendemos?

## Autenticação de usuários
* Login e dashboard
* Realizando o Login
* Material do curso
* Menu, logout e dashboard
* Faça como eu fiz na aula
* Menu dinâmico
* O que aprendemos?

## Formulário de receita
* Material do curso
* Criando formulário de receita
* Dados da requisição
* Receita de cada usuário
* Faça como eu fiz na aula
* Cada receita com seu dono
* O que aprendemos?

## Refatoração e mensagens
* Mensagens de sucesso e erro
* Refatoração e ajustes finais
* Faça como eu fiz na aula
* Mensagem não exibida
* O que aprendemos?
* Conclusão
* Parabéns

# Notas das aulas:

* Introdução: Projeto e subindo servidor  
    Rode no seu terminal:
    ```sh
    sudo docker-compose run web django-admin.py startproject alurareceita .
    ```
* Introdução: Servidor e app de receita  
    Entre no projeto:  
    ```sh
    docker-compose run --rm web bash
    ```
    E rode:
    ```sh
    python manage.py startapp receitas
    ```

* Django Admin
    Criar um 'super user':
    ```sh
    python manage.py createsuperuser
    ```

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

[2° Criar um projeto em Django](https://github.com/claudimf/try_django)