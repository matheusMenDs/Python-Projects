import mysql.connector

class DatabaseManager:
    def __init__(self, host, user, password, database):
        self.config = {
            "host": host,
            "user": user,
            "password": password,
            "database": database
        }
        self.connection = self.create_connection()
        self.create_table()

    def create_connection(self):
        """Estabelece a conexão com o banco de dados."""
        return mysql.connector.connect(**self.config)

    def create_table(self):
        """Cria a tabela de usuários, caso não exista."""
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL UNIQUE
            )
        """)
        self.connection.commit()

    def insert_user(self, name, email):
        """Insere um novo usuário no banco de dados."""
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        self.connection.commit()

    def fetch_users(self):
        """Busca todos os usuários cadastrados."""
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users")
        return cursor.fetchall()
