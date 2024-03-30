from telebot import TeleBot
from telebot.apihelper import ApiTelegramException

from components.CustomInlineMarkup import CustomInlineMarkup
from components.Utils import get_channel_name

from components.CustomKeyboardMarkup import CustomKeyboardMarkup

from res.strings import Strings
from res.constants import channels

from data.ReferralSystemDBManager import ReferralSystemDBManager as db


class Bot:
    def __init__(self, token):
        self.bot = TeleBot(token)
        self.subscribe_msg = -1
        self.description_msg = -1
        self.db = db()
        self.from_user = ""

    def start(self, message, from_user=""):

        self.bot.send_photo(
            message.chat.id,
            photo=open("../res/images/banner.jpg", "rb"),
            caption=Strings.get_start_text(message.from_user.first_name),
            parse_mode="HTML"
        )
        if not self.is_subscribed(message.chat.id):
            self.subscribe_text(message)

        else:
            self.get_referral_link(message)

        if len(from_user) > 0 and not self.db.is_user_logged(str(message.chat.id)):
            self.db.increment_referral_count(from_user)
            self.db.create_user(str(message.chat.id))
            try:
                self.bot.send_message(
                    int(from_user),
                    Strings.send_you_referred(message.from_user.first_name),
                    parse_mode="HTML"
                )
            except:
                print("Something went wrong")
        else:
            self.db.create_user(str(message.chat.id))

    def is_subscribed(self, user_id):
        try:
            for channel in channels:
                for _, url in channel.items():
                    res = self.bot.get_chat_member(get_channel_name(url), user_id)
                    if res.status in ["left", "kicked"]:
                        return False
            return True

        except ApiTelegramException:
            return False

    def subscribe_text(self, message):
        self.subscribe_msg = self.bot.send_message(
            message.chat.id,
            Strings.get_subscribe_text(),
            parse_mode="HTML",
            reply_markup=CustomInlineMarkup.add_inline_button(
                CustomInlineMarkup.inline_linked_keyboard(*channels),
                {Strings.get_check_button_text(): Strings.get_check_button_text()}
            ) if not self.is_subscribed(message.chat.id) else None
        ).id

    def get_referral_link(self, message):

        self.description_msg = self.bot.send_message(
            message.chat.id,
            Strings.get_referral_text(),
            parse_mode="HTML",
            reply_markup=CustomInlineMarkup.inline_keyboard(
                {Strings.get_referral_button_text(): Strings.get_referral_button_text()}
            )
        ).id

    def get_referral(self, call):
        self.bot.answer_callback_query(call.id, Strings.get_referral())
        self.bot.delete_message(call.message.chat.id, self.description_msg)
        self.bot.send_photo(
            call.message.chat.id,
            photo=open('../res/images/banner.jpg', 'rb'),
            caption=Strings.get_referral_caption(call.message.chat.id),
            parse_mode="HTML"
        )

    def not_subscribed_alert(self, call):
        self.bot.answer_callback_query(call.id, Strings.get_not_subscribed_text(), True)

    def run(self):
        @self.bot.message_handler(commands=['start'])
        def send_welcome(message):
            if len(message.text.split(' ')) == 2:
                self.start(message, from_user=message.text.split(' ')[1])
                self.from_user = message.text.split(' ')[1]
            else:
                self.start(message)
            print(message)

        @self.bot.message_handler()
        def message_handler(message):
            if message.text == "📎Taklif qilish havolasini olish":
                self.get_referral_link(message)

            elif message.text == "👩‍🏫🧑‍🏫Ustozlar haqida":
                self.bot.send_message(
                    message.chat.id,
                    Strings.about_teachers(),
                    parse_mode="HTML"
                )

            elif message.text == "📕Kurs haqida":
                self.bot.send_photo(message.chat.id, open("../res/images/about_course_1.jpg", 'rb'))
                self.bot.send_photo(message.chat.id, open("../res/images/about_course_2.jpg", 'rb'))

            elif message.text == "🧮Takliflarim soni":
                self.bot.send_message(
                    message.chat.id,
                    Strings.get_refs_count(db.get_refs_count(message.chat.id)),
                    parse_mode="HTML"
                )

        @self.bot.callback_query_handler(func=lambda call: True)
        def callback_query_handler(call):
            if call.data == Strings.get_check_button_text():
                if self.is_subscribed(call.from_user.id):
                    self.bot.delete_message(call.message.chat.id, self.subscribe_msg)
                    self.db.increment_referral_count(self.from_user)
                    self.bot.send_message(
                        call.message.chat.id,
                        Strings.joined_to_all_channels(),
                        parse_mode="HTML",
                        reply_markup=CustomKeyboardMarkup.keyboard(
                            ["📎Taklif qilish havolasini olish"],
                            ["👩‍🏫🧑‍🏫Ustozlar haqida", "📕Kurs haqida"],
                            ["🧮Takliflarim soni"]
                        )
                    )

                else:
                    self.not_subscribed_alert(call)

            if call.data == Strings.get_referral_button_text():
                self.get_referral(call)

        self.bot.polling(none_stop=True)


if __name__ == "__main__":
    bot = Bot(Strings.get_token())
    bot.run()
