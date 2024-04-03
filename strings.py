class Strings(object):

    @staticmethod
    def token():
        return "7089323478:AAFsR1iSNiV9F5sHtfcrFig7ZTZNlZIfnGw"

    @staticmethod
    def start_text(name: str):
        return f"""<b>Assalomu alaykum, {name}

Bu bot sizga 👇

✨ MAXSUS BEPUL SPEAKING & READING darslariga qatnasha olishingiz uchun alohida kanal linkini beradi 👇</b>"""

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

🫵 Agar Sizda IELTS Speaking va Reading'da muammolar bo'lsa bu kurs aynan siz uchun.

😍 Ushbu Mini Speaking & Reading kursimiz 100% BEPUL ! 

🫵 Siz uchun 2 tajribali IELTS Intructorlari, Asilbek Yusupov (IELTS 9.0 | Speaking 9.0) va Fayzulloh Gulomov (IELTS 8.0 | Reading 9.0) 14 kun davomida Speaking va Reading darslarini o'tib beradi.
➖➖➖➖➖➖➖➖➖➖➖➖➖
Qatnashish uchun 👇

🔗Bot sizga taqdim etgan referral linkni atigi 5 nafar INGLIZ TILI o'rganayotgan do'stingizga yuboring va do'stlaringiz botda ro'yxatdan o'tsa, bot sizga avtomatik tarzda kurs uchun link beradi.

📝 Kurs haqida to’liq ma’lumot va soatlari Maxsus kanalda yozilgan.

Quyidagi 📎Taklif qilish havolasini olish tugmasini bosib, do'stlaringizni taklif qilishni boshlang👇</b>"""

    @staticmethod
    def referral_button_text():
        return "📎Taklif qilish havolasini olish"

    @staticmethod
    def referral():
        return "Havola"

    @staticmethod
    def referral_caption(id):
        return f"""<b>⚡️IELTS SPEAKING & READING band 9.0 egalari tomonidan o'tkaziladigan 14 kunlik 
BEPUL Speaking & Reading Course

🫵 Albatta, ushbu kursga qatnashing 🫵

Kursga qatnashish : 👇
👉<a href="https://t.me/Free_Speaking_AY_bot?start={id}">Bepul Speaking kurs</a>
👉<a href="https://t.me/Free_Speaking_AY_bot?start={id}">Bepul Speaking kurs</a>
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
    def about_teachers():
        return """<b>Asilbek Yusupov
IELTS 9.0 (Speaking 9.0)

Fayzulloh Gulomov
IELTS 8.0 (Reading 9.0)</b>"""

    @staticmethod
    def about_fayzulloh():
        return """<b></b>"""

    @staticmethod
    def refs_count(count):
        return f"""<b>🗣Takliflaringiz soni : {count} ta

Marraga yana {5 - count if count < 5 else 0} ta taklif qoldi 🏆</b>"""

    @staticmethod
    def ask_name():
        return "<b>ℹ️ Iltimos ism-familiyangizni yuboring...</b>"

    @staticmethod
    def ask_number():
        return "<b>📞 Iltimos telefon raqamingizni yuboring...</b>"

    @staticmethod
    def about_course():
        return """<b>😊Kurs haqida to'liq ma'lumot Yopiq Kanalda berilgan. 
Kursga yozilish uchun shartlarni bajaring 🫠</b>"""

    @staticmethod
    def join_private_channel():
        return """<b>🥳 Tabriklaymiz, bizni maxsus kanalga qo'shilishingiz mumkin!</b>"""