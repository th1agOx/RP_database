import sqlite3

def initialize_database():
    conn = sqlite3.connect("rpdatabase.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS gestores (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,  
                    email_gestor TEXT NOT NULL UNIQUE
                )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS centro_de_custo (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    valor_mensal_total REAL NOT NULL,
                    gestor_id INTEGER NOT NULL, 
                    FOREIGN KEY (gestor_id) REFERENCES gestores(id)
                )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cobranca (
                   id INTERGER PRIMARY KEY AUTOINCREMENT,
                   telefone TEXT NOT NULL UNIQUE,
                   nome_funcionario TEXT NOT NULL, 
                   valor_mensal REAL NOT NULL,
                   centro_de_custo_id INTEGER NOT NULL ,
                   FOREIGN KEY (centro_de_custo) REFERENCES centro_de_custo(id)
                )
    ''')
    
    conn.commit()
    conn.close()



if __name__ == "__main__":
    initialize_database()