class ReferralSystemDBUtils(object):
    @staticmethod
    def create_products_table():
        return """
            CREATE TABLE IF NOT EXISTS referrals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER UNIQUE,
                refs_count INTEGER
            )
            """.strip()

    @staticmethod
    def increment_referral_count():
        return f"""
                INSERT INTO referrals (user_id, refs_count)
                VALUES (?, 1)
                ON CONFLICT(user_id)
                DO UPDATE SET refs_count = refs_count + 1
                WHERE user_id = ?
                """.strip()

    @staticmethod
    def create_user():
        return f"""
                INSERT INTO referrals (user_id, refs_count)
                VALUES (?, 0)
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
