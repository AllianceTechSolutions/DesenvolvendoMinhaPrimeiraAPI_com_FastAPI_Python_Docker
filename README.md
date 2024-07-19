# Desenvolvendo Minha Primeira API com FastAPI, Python e Docker

Bem-vindo ao repositório do projeto **Desenvolvendo Minha Primeira API com FastAPI, Python e Docker**. Este projeto é um exemplo de como criar uma API utilizando o FastAPI, Python e Docker. 

## Descrição

Este projeto tem como objetivo demonstrar a criação e desenvolvimento de uma API RESTful utilizando FastAPI. Ele inclui exemplos de uso de parâmetros de consulta, customização de respostas, manipulação de exceções e paginação. 

### Funcionalidades

- **Query Parameters**:
  - Endpoints para obter informações sobre atletas usando parâmetros de consulta, como `nome` e `cpf`.

- **Customização de Respostas**:
  - Respostas customizadas para o endpoint `GET all`, incluindo informações como `nome`, `centro_treinamento` e `categoria`.

- **Manipulação de Exceções**:
  - Tratamento de exceções `sqlalchemy.exc.IntegrityError` com mensagens apropriadas, como "Já existe um atleta cadastrado com o cpf: x".

- **Paginação**:
  - Adicionada paginação utilizando a biblioteca `fastapi-pagination`, com parâmetros `limit` e `offset`.

## Requisitos

- Python 3.8 ou superior
- Docker
- FastAPI
- SQLAlchemy
- fastapi-pagination

## Instalação

1. **Clone o Repositório**

   ```bash
   git clone https://github.com/AllianceTechSolutions/DesenvolvendoMinhaPrimeiraAPI_com_FastAPI_Python_Docker.git
   cd DesenvolvendoMinhaPrimeiraAPI_com_FastAPI_Python_Docker

2. **Instale as Dependências**

   ```Instale as dependências Python listadas no requirements.txt:
   pip install -r requirements.txt

3. **Configure o Ambiente**

   ```Crie um arquivo .env para variáveis de ambiente necessárias. Exemplo:
    DATABASE_URL=sqlite:///./test.db

4. **Inicie o Docker**

   ```Construa e inicie o container Docker:
    docker-compose up --build

  <hr>

## Uso

Após iniciar o Docker, a API estará disponível em http://localhost:8000. Você pode testar os endpoints usando ferramentas como Postman ou cURL.


### Exemplos de Endpoints

- **Obter todos os atletas**:

  ```
   GET /atletas
  
  ```
- **Adicionar um novo atleta**:
  
  ```
  POST /atletas
  
  ```

- **Obter atleta por CPF**:
  
  ```
  GET /atletas/{cpf}
   
  ```

  <hr>


### Contribuição

Se você deseja contribuir para este projeto, sinta-se à vontade para abrir um issue ou enviar um pull request. Certifique-se de seguir as diretrizes de contribuição.


### Contato

Para perguntas ou mais informações, entre em contato com Thiago ABC.

<br>

### Obrigado por conferir o projeto! Esperamos que este exemplo ajude você a começar com o FastAPI, Python e Docker.

<br>

### Personalize o README

- **Descrição do Projeto:** Ajuste a descrição e os detalhes conforme a sua implementação específica.
- **Requisitos e Instalação:** Certifique-se de que os requisitos e os passos de instalação estão corretos para o seu projeto.
- **Exemplos de Endpoints:** Adapte os exemplos de endpoints para corresponder às rotas e funcionalidades da sua API.

Se precisar de mais ajustes ou tiver outras informações para adicionar, fique à vontade para informar!




