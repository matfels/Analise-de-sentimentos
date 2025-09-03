import sqlite3

class Database:
    def __init__(self, db_nome): #db_name vai receber o nome do banco de dados
        self.conn = sqlite3.connect(db_nome) #sqlite3.connect() estabelece a conexão com o banco de dados, se ele não existir ele será criado.
        self.cursor = self.conn.cursor() #cursor() permite executar comandos SQL e percorrer os resultados de uma consulta.
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS twitter (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                post TEXT NOT NULL,
                category TEXT,
                active boolean,
                score float
            )
        """)
        self.conn.commit() #Confirma a transição, salvar as alterações feiras no banco de dados 

    def insert_post(self, post, category, score, active ):
        self.cursor.execute("INSERT INTO twitter (post, category, active, score) VALUES(?, ?, ?, ?)", (post, category, active, score))
        self.conn.commit()

    def update_post(self, post_id, new_post, new_category, active, score):
        self.cursor.execute("UPDATE twitter SET post = ?, category = ?, active = ?, score = ?  WHERE id = ?", (new_post, new_category,active, score, post_id))
        self.conn.commit()

    def delete_post(self, post_id):
        self.cursor.execute("DELETE from twitter where id = ?", (post_id,))    
        self.conn.commit()


    def read_posts(self):
        self.cursor.execute("SELECT * from twitter")    
        return self.cursor.fetchall()
    
    def __del__(self):
        self.conn.close()

    


