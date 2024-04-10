import sqlite3
from ReferralSystemDBUtils import ReferralSystemDBUtils as db


class ReferralSystemDBManager(object):

    @staticmethod
    def create_table():
        try:
            connection = sqlite3.connect('refs.db')
            cursor = connection.cursor()
            cursor.execute(db.create_products_table())
            connection.commit()
        except sqlite3.Error as e:
            print("Error creating table:", e)
        finally:
            if connection:
                connection.close()

    @staticmethod
    def increment_referral_count(user_id, name, number):
        try:
            connection = sqlite3.connect('refs.db')
            cursor = connection.cursor()
            # Pass user_id twice, once for the initial insertion and once for the WHERE clause
            cursor.execute(db.increment_referral_count(), (user_id, name, number, user_id))
            connection.commit()
        except sqlite3.Error as e:
            print("Error incrementing referral count:", e)
        finally:
            if connection:
                connection.close()

    @staticmethod
    def create_user(user_id: str, name: str, number: str):
        try:
            connection = sqlite3.connect('refs.db')
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
            connection = sqlite3.connect('refs.db')
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
    def get_refs_count(user_id: str) -> int:
        try:
            connection = sqlite3.connect('refs.db')
            cursor = connection.cursor()
            cursor.execute(db.get_refs_count(), (user_id,))
            row = cursor.fetchone()
            if row:
                return row[0]  # Return the refs_count value
            else:
                return 0  # User not found, return 0 refs_count
        except sqlite3.Error as e:
            print("Error fetching refs count:", e)
            return -1  # Return -1 to indicate an error
        finally:
            if connection:
                connection.close()

    @staticmethod
    def clear():
        try:
            connection = sqlite3.connect('refs.db')
            cursor = connection.cursor()
            cursor.execute(db.clear_table())
            connection.commit()
        except sqlite3.Error as e:
            print("Error clearing table:", e)
        finally:
            if connection:
                connection.close()

    @staticmethod
    def get_user_name_by_id(user_id):
        try:
            connection = sqlite3.connect('refs.db')
            cursor = connection.cursor()
            cursor.execute(db.get_user_name_by_id(user_id), (user_id,))
            result = cursor.fetchone()
            return result[0] if result else None
        except sqlite3.Error as e:
            print("Error fetching user by id:", e)
            return None
        finally:
            if connection:
                connection.close()

    @staticmethod
    def get_user_number_by_id(user_id):
        try:
            connection = sqlite3.connect('refs.db')
            cursor = connection.cursor()
            cursor.execute(db.get_user_number_by_id(), (user_id,))
            result = cursor.fetchone()
            return result[0] if result else None
        except sqlite3.Error as e:
            print("Error fetching user by id:", e)
            return None
        finally:
            if connection:
                connection.close()

    @staticmethod
    def remove_user_by_id(user_id):
        try:
            connection = sqlite3.connect('refs.db')
            cursor = connection.cursor()
            cursor.execute(db.remove_user(user_id))

        except sqlite3.Error as e:
            print("Error fetching user by id:", e)
            return None
        finally:
            if connection:
                connection.close()


if __name__ == '__main__':
    option = input("enter desired option\nd -> delete data\nc -> create table\n\n")
    d = ReferralSystemDBManager()
    if option == "d":
        d.clear()
    elif option == "c":
        d.create_table()
    elif option == "r":
        user_id = input()
        d.remove_user_by_id(user_id)
    else:
        option = input("enter desired option\nd -> delete data\nc -> create table")
