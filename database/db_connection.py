import mysql.connector

class Connection:
    def __init__(self):
        self.connection = mysql.connector.connect(
                            host= "localhost",
                             user= "root",
                             password= "root",
                             database= "library_db"
                             )


    def get_connection(self):
        if not self.connection.is_connected():
            self.connection.reconnect()
        return self.connection
    


    def create_books_table(self):
        connection = self.get_connection()
        sql = """CREATE TABLE IF NOT EXISTS books(
        id int AUTO_INCREMENT PRIMARY KEY,
        title varchar(50) NOT NULL,
        author varchar(50) NOT NULL,
        genre varchar(50) NOT NULL,
        is_available BOOLEAN DEFAULT true,
        borrowed_by_member_id int DEFAULT NULL
        )"""

        with connection.cursor() as cursor:
            cursor.execute(sql)      
    

    def create_members_table(self):
        connection = self.get_connection()
        sql = """CREATE TABLE IF NOT EXISTS members(
        member_id int AUTO_INCREMENT PRIMARY KEY,
        name varchar(50) NOT NULL,
        email varchar(255) UNIQUE NOT NULL,
        is_active BOOLEAN DEFAULT true,
        total_borrows int DEFAULT 0
        )"""

        with connection.cursor() as cursor:
            cursor.execute(sql)


