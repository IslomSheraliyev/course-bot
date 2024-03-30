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
    def increment_referral_count(user_id: str):
        try:
            connection = sqlite3.connect('refs.db')
            cursor = connection.cursor()
            cursor.execute(db.increment_referral_count(), (user_id, user_id))
            connection.commit()
        except sqlite3.Error as e:
            print("Error incrementing referral count:", e)
        finally:
            if connection:
                connection.close()

    @staticmethod
    def create_user(user_id: str):
        try:
            print(user_id)
            connection = sqlite3.connect('refs.db')
            cursor = connection.cursor()
            cursor.execute(db.create_user(), (user_id,))
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


if __name__ == '__main__':
    ReferralSystemDBManager().clear()
