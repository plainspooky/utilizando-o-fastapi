Utilizando o FastAPI
---

Exemplo de API criada a partir do [FastAPI](https://fastapi.tiangolo.com/).

# Instalação

Siga os passos:

Clone este repositório e dentro dele crie um ambiente virtual...

  ``` shell
  virtualenv --python python3.8 py3
  ```

* Em _Linux_, _macOS_ e outros _UNIXes_, ative-o usando:

  ``` shell
  source ./py3/bin/activate
  ```

* Para computadores rodando _Windows_, ative o ambiente com:

  ``` shell
  .\py3\Scripts\activate.bat
  ```

# Dependências
  
Utilize o `pip` para baixar as dependências do projeto:

``` shell
pip install -r requirements.txt
```

# Banco de dados

A aplicação usa o **SQLite3** e criará automaticamente o banco de dados mas
desejando uma versão já populada, use:

``` shell
sqlite3 db.sqlite3 < examples/students.sql
```

# Execução

Para executar o servidor use:

``` shell
FASTAPI__DATABASE='sqlite:///db.sqlite3' uvicorn main:app
```

A varíavel `FASTAPI__DATABASE` contém a URL de conexão com o banco de dados.

O servidor estará escutando a porta 8000, para testá-lo use:

``` shell
curl 127.0.0.1:8000/health/
```

Para consultar a documentação da API, acesse http://127.0.0.1:8000/docs e para interomper a execução pressione «Ctrl»+«C».
