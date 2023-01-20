# TRANSFORMANDO MONGODB EM MYSQL COM PYTHON

Neste projeto a ideia é pegar uma collection em mongo, e transformar ela em mysql para um manuseio melhor em relatórios. Utilzei neste projeto uma collection
que possuia array, e uma solução para transforma-la em relacional. 
## 🚀 Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

### 📋 Pré-requisitos



```
MongoDb
Python
Mysql
```


## 🛠️ Construído com


* [MongoD Community](https://www.mongodb.com/try/download/community) - Banco de dados primario utilizado para extração. 
* [Python](https://www.python.org/) - Linguagem utilizada para realizar o ETL.
* [MySQL](https://www.mysql.com/downloads/) - Banco de dados escolhido para ser inserido o resultado.
* [Pymongo](https://pymongo.readthedocs.io/en/stable/) - Biblioteca utilizada para realizar a conexão entre Python e Mongodb
* [locale](https://docs.python.org/pt-br/3.8/library/locale.html) - Biblioteca utilizada tratar a origem dos dados no formato desejado.
* [mysql.connector](https://dev.mysql.com/doc/connector-python/en/) - Biblioteca utilizada para realizar a conexão entre Python e Mysql
* [Pymongo](https://pymongo.readthedocs.io/en/stable/) - Biblioteca utilizada para realizar a conexão entre python e Mongodb


## 📌 Versão

Esta e a 1.0 do projeto de teste, foi realizado localmente com o intuido de transformar uma modelagem não relacional em relacional para obter melhor manuseio 
relatórios, nas proximas versões pretendo automatizar a extração na base primaria do mongodb orientada a evento change-stream, com o objetivo de quaisquer alterações
na base primaria seja transmitido ao mysql assim objetendo os dados em tempo real. 

## ✒️ Autores


* **Analista de Dados** - *Trabalho Inicial* - [desenvolvedor](https://github.com/luiz-rafael)


---
Desenvolvido por [Luiz Rafael](https://github.com/luiz-rafael) 😊
