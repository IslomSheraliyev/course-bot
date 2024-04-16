class LiteSystemDBUtils(object):
    @staticmethod
    def create_products_table():
        return """
            CREATE TABLE IF NOT EXISTS referrals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT UNIQUE,
                name TEXT,
                number TEXT
            )
            """.strip()

    @staticmethod
    def create_user():
        return f"""
                INSERT INTO  referrals (user_id, name, number) 
                VALUES (?, ?, ?)
                """.strip()

    @staticmethod
    def is_user_logged():
        return f"""
                SELECT 1 FROM referrals WHERE user_id = ? LIMIT 1
                """.strip()

    @staticmethod
    def get_refs_count():
        return "SELECT refs_count FROM referrals WHERE user_id = ?"

    @staticmethod
    def clear_table():
        return "DELETE FROM referrals"

    @staticmethod
    def remove_user():
        return "DELETE FROM referrals WHERE user_id = ?"
