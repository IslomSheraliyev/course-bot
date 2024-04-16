import sqlite3
from LiteSystemDBUtils import LiteSystemDBUtils as db


class LiteSystemDBManager(object):

    @staticmethod
    def create_table():
        try:
            connection = sqlite3.connect('lite.db')
            cursor = connection.cursor()
            cursor.execute(db.create_products_table())
            connection.commit()
        except sqlite3.Error as e:
            print("Error creating table:", e)
        finally:
            if connection:
                connection.close()

    @staticmethod
    def create_user(user_id: str, name: str, number: str):
        try:
            connection = sqlite3.connect('lite.db')
            cursor = connection.cursor()
            cursor.execute(db.create_user(), (user_id, name, number))
            connection.commit()
        except sqlite3.Error as e:
            print("Error creating user:", e)
        finally:
            if connection:
                connection.close()

    @staticmethod
    def is_user_logged(user_id: str) -> bool:
        try:
            connection = sqlite3.connect('lite.db')
            cursor = connection.cursor()
            cursor.execute(db.is_user_logged(), (user_id,))
            row = cursor.fetchone()
            return bool(row)  # If row exists, user is logged
        except sqlite3.Error as e:
            print("Error checking if user is logged:", e)
            return False
        finally:
            if connection:
                connection.close()

    @staticmethod
    def clear():
        try:
            connection = sqlite3.connect('lite.db')
            cursor = connection.cursor()
            cursor.execute(db.clear_table())
            connection.commit()
        except sqlite3.Error as e:
            print("Error clearing table:", e)
        finally:
            if connection:
                connection.close()


if __name__ == '__main__':
    option = input("enter desired option\nd -> delete data\nc -> create table\n")
    d = LiteSystemDBManager()
    if option == "d":
        d.clear()
    elif option == "c":
        d.create_table()
    else:
        option = input("enter desired option\nd -> delete data\nc -> create table")
