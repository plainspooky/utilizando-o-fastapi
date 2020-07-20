Utilizando o FastAPI
---

Exemplo de API criada a partir do [FastAPI](https://fastapi.tiangolo.com/).

# Instalação

Siga os passos:

Clone este repositório e dentro dele crie um ambiente virtual...

  ``` shell
  virtualenv --python python3.8 py3
  ```

* Em _Linux_, _macOS_ e outros _UNIXes_, ative-o usando...

  ``` shell
  source ./py3/bin/activate
  ```

* Para computadores rodando _Windows_, ative o ambiente com...

  ``` shell
  .\py3\Scripts\activate.bat
  ```

# Dependências
  
Utilize o `pip` para baixar as dependências...

``` shell
pip install -r requirements.txt
```

# Execução

Para executar o servidor use:

``` shell
uvicorn main:app
```

O servidor estará escutando a porta 8000, para testá-lo use...

``` shell
curl 127.0.0.1:8000/health/
```

Para consultar a documentação da API, acesse http:/ /127.0.0.1:8000/docs e para interomper a execução pressione «Ctrl»+«C».
