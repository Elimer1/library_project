from db_connection import Connection

class BookDB:
    def __init__(self):
        self.db = Connection()
        self.connection = self.db.get_connection()


    def create_book(self, data):
        sql = """INSERT INTO books (title, author, genre)
        VALUES (%(title)s, %(author)s, %(genre)s)"""
        with self.connection.cursor() as cursor:
            cursor.execute(sql, data)
            self.connection.commit()

    
    def get_all_books(self):
        sql = """SELECT * FROM books"""
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()
        

    def get_book_by_id(self, id):
        sql = """SELECT * FROM books WHERE id = %s"""
        with self.connection.cursor() as cursor:
            cursor.execute(sql, (id, ))
            return cursor.fetchone()

            
        

    def update_book(self, id, data):
        set_parts = [f"{key} = %s" for key in data.keys()]
        set = ", ".join(set_parts)
        sql = f"""UPDATE books
        SET {set} 
        WHERE id = %s"""
        values = list(data.values()) + [id]
        with self.connection.cursor() as cursor:
            cursor.execute(sql, values)

            self.connection.commit()
            return cursor.rowcount() > 0
        

    def set_available(self, id, val, member_id):
        sql = """UPDATE books 
            SET is_available = %s, borrowed_by_member_id = %s
            WHERE id = %s
            """
        with self.connection.cursor() as cursor:
            if val:
                cursor.execute(sql, (False, member_id, id))
            else:
                cursor.execute(sql, (True, None, id))


            self.connection.commit()
            return cursor.rowcount() > 0
          

    def count_total_books(self):
        sql = """SELECT COUNT(id) FROM books"""
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchone()[0]
        

    def count_available_books(self):
        sql = """SELECT COUNT(id) FROM books WHERE is_available = true"""
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchone()[0]
        

    def count_borrowed_books(self):
        sql = """SELECT COUNT(id) FROM books WHERE is_available = false"""
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchone()[0]
        
    
    def count_by_genre(self, genre):
        sql = """SELECT COUNT(id) FROM books WHERE genre = %s"""
        with self.connection.cursor() as cursor:
            cursor.execute(sql, (genre, ))
            return cursor.fetchone()[0]
        

    def count_active_borrows_by_member(self, member_id):
        sql = """SELECT COUNT(id) FROM books WHERE borrowed_by_member_id = %s"""
        with self.connection.cursor() as cursor:
            cursor.execute(sql, (member_id, ))
            return cursor.fetchone()[0]