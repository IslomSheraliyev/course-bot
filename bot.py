from telebot import TeleBot
from telebot.apihelper import ApiTelegramException

from Utils import get_channel_name

from CustomInlineMarkup import CustomInlineMarkup
from CustomKeyboardMarkup import CustomKeyboardMarkup

from strings import Strings
from constants import channels

from ReferralSystemDBManager import ReferralSystemDBManager as db


class Bot:
    def __init__(self, token):
        self.bot = TeleBot(token)
        self.subscribe_msg = -1
        self.description_msg = -1
        self.db = db()
        self.from_user = ""
        self.name = "",
        self.number = ""

    def get_name(self, message):
        self.name = message.text
        self.bot.send_message(message.chat.id, Strings.get_ask_number(), parse_mode="HTML")
        self.bot.register_next_step_handler(message, self.get_phone_number)

    def get_phone_number(self, message):
        self.number = message.text
        # self.db.create_user(message.chat.id, str(self.name), str(self.number))
        if self.is_subscribed(message.chat.id):
            self.get_referral_link(message)
        else:
            self.subscribe_text(message)

    def start(self, message):
        if self.db.is_user_logged(message.chat.id):
            self.bot.send_photo(
                message.chat.id,
                photo=open("banner.jpg", "rb"),
                caption=Strings.get_start_text(message.from_user.first_name),
                parse_mode="HTML"
            )
            if not self.is_subscribed(message.chat.id):
                self.subscribe_text(message)
            else:
                self.get_referral_link(message)

        else:
            self.bot.send_message(message.chat.id, Strings.get_ask_name(), parse_mode="HTML")
            self.bot.register_next_step_handler(message, self.get_name)

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
        if not self.is_subscribed(message.chat.id):
            self.subscribe_msg = self.bot.send_message(
                message.chat.id,
                Strings.get_subscribe_text(),
                parse_mode="HTML",
                reply_markup=CustomInlineMarkup.add_inline_button(
                    CustomInlineMarkup.inline_linked_keyboard(*channels),
                    {Strings.get_check_button_text(): Strings.get_check_button_text()}
                )
            ).id
        else:
            self.get_referral_link(message)

    def get_referral_link(self, message):

        if not self.db.is_user_logged(message.chat.id):
            self.db.create_user(str(message.chat.id), str(self.name), str(self.number))

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
            photo=open('banner.jpg', 'rb'),
            caption=Strings.get_referral_caption(call.message.chat.id),
            parse_mode="HTML"
        )

    def not_subscribed_alert(self, call):
        self.bot.answer_callback_query(call.id, Strings.get_not_subscribed_text(), True)

    def send_refs_count(self, chat_id):
        self.bot.send_message(chat_id, Strings.get_refs_count(self.db.get_refs_count(str(chat_id))), parse_mode="HTML")

    def run(self):
        @self.bot.message_handler(commands=['start'])
        def send_welcome(message):
            if len(message.text.split(' ')) == 2:
                self.from_user = message.text.split(' ')[1]
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
                self.bot.send_photo(message.chat.id, open("about_course_1.jpg", 'rb'))
                self.bot.send_photo(message.chat.id, open("about_course_2.jpg", 'rb'))

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
                    if len(self.from_user) > 0 and not self.db.is_user_logged(call.message.chat.id):
                        print("enter")
                        name = self.db.get_user_name_by_id(call.message.chat.id)
                        number = self.db.get_user_number_by_id(call.message.chat.id)
                        self.db.increment_referral_count(self.from_user, name, number)
                        self.send_refs_count(self.from_user)

                    self.db.create_user(str(call.message.chat.id), str(self.name), str(self.number))
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
