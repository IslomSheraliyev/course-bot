class Strings(object):

    @staticmethod
    def get_token():
        return "7168101617:AAGkoYuT8xTMBhCfjfCDDwZiRI8UKjk7m_8"

    @staticmethod
    def get_start_text(name: str):
        return f"""<b>Assalamu alaykum, {name}\n\nBu bot sizga 👇\n\n✨ IELTS SPEAKING band 9.0 va band 8.0 egalari tomonidan o'tkaziladigan bir oylik MAXSUS BEPUL SPEAKING darslariga qatnasha olishingiz uchun alohida kanal linkini beradi 👇</b>""".strip()

    @staticmethod
    def get_subscribe_text():
        return f"""<b>✅ Davom etish uchun quyidagi kanallarga obuna bo’ling👇 va <code>Tekshirish</code> ✅ tugmasini bosing.</b>"""

    @staticmethod
    def get_not_subscribed_text():
        return f"""ℹ️ Check each of channels, you didn't subscribed to all of them!"""

    @staticmethod
    def get_check_text():
        return f"""✅ Check"""
