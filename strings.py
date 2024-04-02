class Strings(object):

    @staticmethod
    def token():
        return "7168101617:AAGkoYuT8xTMBhCfjfCDDwZiRI8UKjk7m_8"

    @staticmethod
    def start_text(name: str):
        return f"""<b>Assalomu alaykum, {name}

Bu bot sizga 👇

✨ MAXSUS BEPUL SPEAKING darslariga qatnasha olishingiz uchun alohida kanal linkini beradi 👇</b>"""

    @staticmethod
    def subscribe_text():
        return f"<b>Faqat YOPIQ KANAL linkini olish uchun quyidagi kanallarimizga obuna bo'lishingiz talab etiladi ✅</b>"

    @staticmethod
    def not_subscribed_text():
        return f"ℹ️ Iltimos ko'rsatilgan kanallarning barchasiga obuna bo'ling!"

    @staticmethod
    def check_button_text():
        return f"✅ Tekshirish"

    @staticmethod
    def referral_text():
        return """<b>‼️Diqqat bilan o'qing 👇

🫵 Speaking balingizni bir oy davomida
1.5 yoki 2 ballga oshirmoqchi bo'lsangiz ushbu MAXSUS BEPUL SPEAKING kurs aynan siz uchun.

😍 Ushbu Speaking kursimiz 100% BEPUL ! 🫵 Siz uchun Speaking band 9 holders tomonidan juda ham foydali bo'lgan Speaking darslari o'tib beriladi !!
➖➖➖➖➖➖➖➖➖➖➖➖➖
Qatnashish uchun 👇

🔗Bot sizga taqdim etgan referral linkni atigi 5 nafar INGLIZ TILI o'rganayotgan do'stingizga yuboring va do'stlaringiz botda ro'yxatdan o'tsa, bot sizga avtomatik tarzda kurs uchun link beradi.

📝 Kurs haqida to’liq ma’lumot va soatlari Maxsus kanalda yozilgan

Quyidagi <code>📎Taklif qilish havolasini olish</code> tugmasini bosib, do'stlaringizni taklif qilishni boshlang👇</b>"""

    @staticmethod
    def referral_button_text():
        return "📎Taklif qilish havolasini olish"

    @staticmethod
    def referral():
        return "Havola"

    @staticmethod
    def referral_caption(id):
        return f"""<b>⚡️IELTS SPEAKING band 9.0 va band 8.0
egalari tomonidan o'tkaziladigan bir oylik 
BEPUL ONLINE SPEAKING MARATHON 

🫵 Albatta, ushbu kursga qatnashing 🫵

Kursga qatnashish : 👇
👉<a href="https://t.me/english_course_project_bot?start={id}">Bepul Speaking kurs</a>
👉<a href="https://t.me/english_course_project_bot?start={id}">Bepul Speaking kurs</a>
</b>
"""

    @staticmethod
    def you_referred(name: str):
        return f"""<b>Siz taklif qilgan do'stingiz {name} botimizga tashrif buyurdi 😊

Do'stingiz barcha kanallarimizga a'zo bo'lsa, taklif qilgan do'stlaringiz soni yana bittaga ortadi 🤗</b>"""

    @staticmethod
    def joined_to_all_channels():
        return "<b>✅ Barcha kanallarga a'zo bo'ldingiz</b>"

    @staticmethod
    def about_asilbek():
        return """<b>Asilbek Yusupov
IELTS 9.0 (Speaking 9.0)</b>"""

    @staticmethod
    def about_fayzulloh():
        return """<b>Fayzulloh Gulomov
IELTS 8.0 (Reading 9.0)</b>"""

    @staticmethod
    def refs_count(count):
        return f"""<b>🗣Takliflaringiz soni : {count} ta

Marraga yana {5 - count if count < 5 else 0} ta taklif qoldi 🏆</b>"""

    @staticmethod
    def ask_name():
        return "<b>ℹ️ Iltimos ismingizni yuboring...</b>"

    @staticmethod
    def ask_number():
        return "<b>📞 Iltimos telefon raqamingizni yuboring...</b>"

    @staticmethod
    def join_private_channel():
        return """<b>🥳 Tabriklaymiz, bizni maxsus kanalga qo'shilishingiz mumkin!</b>"""