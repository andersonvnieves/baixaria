import pyodbc

class DatabaseHandler:

    def __init__(self, server, port, database, user, pwd):
        # Tem que instalar o driver ODBC do banco de dados que voce for usar,
        # tem o link no README.md, use o comando a baixo para saber se funcionou
        # print(pyodbc.drivers())

        #Gera a string de conexão com o banco
        self.connection_string = f"""
            DRIVER=PostgreSQL Unicode(x64);
            SERVER={server};
            PORT={port};
            DATABASE={database};
            UID={user};
            PWD={pwd};
        """
        #Abre uma conexão com o banco
        self.conn = pyodbc.connect(self.connection_string)

    def save(self, data):
        self.conn.execute(f"""INSERT INTO INVENTORY_RECORDS_DATA VALUES (
                '{data[0]}', '{data[1]}', {data[2]}, {data[3]}, {data[4]}, {data[5]}, {data[6]}, {data[7]});""")
        self.conn.commit()

    def read(self):
        cursor = self.conn.cursor()
        cursor.execute("select * from public.teste")
        for record in cursor.fetchall():
            print(record.name)

        cursor.close()

    def close_connection(self):
        self.conn.close()
