import os
from pathlib import Path

class FileHandler:

    def __init__(self, directory_name, file_extensions):
        #Pasta em que esse arquivo está
        current_path = Path(__file__).parent
        #Caminho absuluto da pasta onde as planilhas estão
        self.data_folder_path = current_path / directory_name
        #String com as extenções e arquivos suportadas
        self.file_extensions = file_extensions

    def get_excel_file_list(self) -> list:
        files = []
        #Um loop em todos os arquivos da pasta
        for file_name in os.listdir(self.data_folder_path):
            #Verificar se o arquivo é uma planilha
            if Path(file_name).suffix in self.file_extensions:
                #Adiciona na lista o caminho absuluto dos arquivos válidos
                files.append(self.data_folder_path / file_name)
            else:
                print(f'Pulando arquivo: {file_name}  /n')

        return files
