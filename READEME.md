
# Script da Baixaria

Esse script carrega todos os arquivos excel de uma pasta em inseri um a um no banco de dados. Todos os arquivos devem ter a mesma estrutura.


## Itens necessários:
### Python 3.12 
O script foi feito em Python 3.12 caso não tenha instado segue o link: https://www.python.org/downloads/release/python-3120/
### ODBC Driver
Para o python conseguir conectar com o banco de dados é necessário instalar o driver ODBC do banco de dados em uso, no caso o do postgresql: https://odbc.postgresql.org/ 
### Postgres
Temos duas opções, você pode instalar diretamente na sua máquina o postgresql seguindo esse link: https://www.postgresql.org/download/

Ou voce pode instalar o docker e rodar uma imagem de container do postgresql (mais complicado mas recomendado)

Etapas: 
- Instalar o Docker Desktop (https://www.docker.com/products/docker-desktop/) 
- Criar uma conta no Docker Hub
- Utilizar a imagem a seguir para criar um container do posrgres (https://hub.docker.com/_/postgres)
### Dbeaver
Utilize o Dbeaver (https://dbeaver.io/) para criar o banco e a tabela e depois executar consultas.
### PyCharm
IDE de python, utilize a versão grátis (https://www.jetbrains.com/pycharm/?msclkid=c6bcd3f3bab1104c598fb40926356d93&utm_source=bing&utm_medium=cpc&utm_campaign=AMER_en_BR_PyCharm_Search&utm_term=python%20ide&utm_content=python%20ide)

## Configuração:
No projeto existe um arquivo chamado config.ini tem os dados de conexão com o banco e informações da planilha, sustitua as informações entre '<>'

```
[DATA]
directory_name = < NOME DA PASTA DOS ARQUIVOS EXCEL DENTRO DA PASTA DO PROJETO, SE NÃO ALTEROU DEIXE 'DATA'>
file_extensions = .xls,.xlsx
min_row = <NÚMERO DA LINHA EM QUE COMEÇA OS DADOS NO EXCEL>
min_col = <NÚMERO DA COLUNA EM QUE COMEÇA OS DADOS NO EXCEL>
max_col = <NÚMERO DA COLUNA EM QUE TERMINA OS DADOS NO EXCEL>

[DATABASE]
server = <IP DO SERVIDOR DE BANCO DE DADOS>
port = <PORTA DO DB, S ENAO TROCOU USAR A PADRÃO ->5432 >
database = <NOME DO SEU BANCO DE DADOS>
user = <USUÁRIO DO BANCO DE DADOS>
pwd = <SENHA DO BANCO DE DADOS>
table_name = < NOME DA TABELA SE POSSÍVEL NOME COMPLETO, DB.SCHEMA.TABELA>
```

## Executar

- Abra o projeto na PyCharm execute o seguinte comando no terminal para instalar as dependências : 
`pip install -r requirements.txt`
- Coloque os arquivos na pasta "DATA"
- Crie a estrutura da tabela no banco, script 'create_table_script.sql' de exemplo
- Exeute o arquivo main.py



