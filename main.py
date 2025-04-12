import configparser

from file_handler import FileHandler
import excel_handler
from database_handler import DatabaseHandler

def main():
    #Obtem os valores do arquivo config.ini que são as configurações do projeto
    config = configparser.ConfigParser()
    config.read('config.ini')
    config.sections()

    #Etapa 1: Obter a lista de arquivos
    file_handler = FileHandler(config['DATA']['directory_name'], config['DATA']['file_extensions'])
    files = file_handler.get_excel_file_list()

    #Etapa 2: Vamos ler um arquivo por vez e já inserir no banco de dados para não ficar com todas as planilhas juntas em memória
    print("Carregando arquivos:")
    # Abre a conexão com o banco
    db = DatabaseHandler(config['DATABASE']['server'],
                         config['DATABASE']['port'],
                         config['DATABASE']['database'],
                         config['DATABASE']['user'],
                         config['DATABASE']['pwd'])
    for file in files:
        print(f"{file}")
        # A variável current_data armazena os dados da planilha atual em lista
        current_data = excel_handler.read(file,
            int(config['DATA']['min_row']),
            int(config['DATA']['min_col']),
            int(config['DATA']['max_col']))

        #Loop em linha por linha do arquivo
        for row in current_data:
            # Agora vamos salvar no banco os dados da planilha atual
            db.save(row)

    db.close_connection()
    print("FIM!")

if __name__ == "__main__":
    main()
