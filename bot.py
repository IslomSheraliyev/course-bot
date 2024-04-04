from telebot import TeleBot
from telebot.apihelper import ApiTelegramException
from telebot.types import InputMediaPhoto

from Utils import get_channel_name

from CustomInlineMarkup import CustomInlineMarkup
from CustomKeyboardMarkup import CustomKeyboardMarkup

from strings import Strings
from constants import channels, key

from ReferralSystemDBManager import ReferralSystemDBManager as db


class Bot:
    def __init__(self, token):
        try:
            self.bot = TeleBot(token)
            self.subscribe_msg = -1
            self.description_msg = -1
            self.db = db()
            self.from_user = ""
            self.name = ""
            self.number = ""
            self.private_chat_id = -1002119653669
        except Exception as e:
            print(f"An error occurred in __init__: {e}")

    def get_name(self, message):
        try:
            self.name = message.text
            self.bot.send_message(
                message.chat.id,
                Strings.ask_number(),
                parse_mode="HTML",
                reply_markup=CustomKeyboardMarkup.get_number_keyboard()
            )
        except Exception as e:
            print(f"An error occurred in get_name: {e}")

    def start(self, message):
        try:
            if self.db.is_user_logged(message.chat.id):
                self.bot.send_photo(
                    message.chat.id,
                    photo=open("banner.jpg", "rb"),
                    caption=Strings.start_text(message.from_user.first_name),
                    parse_mode="HTML"
                )
                if not self.is_subscribed(message.chat.id):
                    self.subscribe_text(message)
                else:
                    self.get_referral_link(message)

            else:
                self.bot.send_message(message.chat.id, Strings.ask_name(), parse_mode="HTML")
                self.bot.register_next_step_handler(message, self.get_name)
        except Exception as e:
            print(f"An error occurred in start: {e}")

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
        except Exception as e:
            print(f"An error occurred in is_subscribed: {e}")
            return False

    def subscribe_text(self, message):
        try:
            if not self.is_subscribed(message.chat.id):
                self.subscribe_msg = self.bot.send_message(
                    message.chat.id,
                    Strings.subscribe_text(),
                    parse_mode="HTML",
                    reply_markup=CustomInlineMarkup.add_inline_button(
                        CustomInlineMarkup.inline_linked_keyboard(*channels),
                        {Strings.check_button_text(): Strings.check_button_text()}
                    )
                ).id
            else:
                self.get_referral_link(message)
        except Exception as e:
            print(f"An error occurred in subscribe_text: {e}")

    def get_referral_link(self, message):
        try:
            if not self.db.is_user_logged(message.chat.id):
                self.db.create_user(str(message.chat.id), str(self.name), str(self.number))

            self.description_msg = self.bot.send_message(
                message.chat.id,
                Strings.referral_text(),
                parse_mode="HTML",
                reply_markup=CustomInlineMarkup.inline_keyboard(
                    {Strings.referral_button_text(): Strings.referral_button_text()}
                )
            ).id
        except Exception as e:
            print(f"An error occurred in get_referral_link: {e}")

    def get_referral(self, call):
        try:
            self.bot.answer_callback_query(call.id, Strings.referral())
            self.bot.delete_message(call.message.chat.id, self.description_msg)
            self.bot.send_photo(
                call.message.chat.id,
                photo=open('banner.jpg', 'rb'),
                caption=Strings.referral_caption(call.message.chat.id),
                parse_mode="HTML",
                reply_markup=CustomKeyboardMarkup.keyboard(
                    ["📎Taklif qilish havolasini olish"],
                    ["👩‍🏫🧑‍🏫Ustozlar haqida", "📕Kurs haqida"],
                    ["🧮Takliflarim soni"]
                )
            )
        except Exception as e:
            print(f"An error occurred in get_referral: {e}")

    def not_subscribed_alert(self, call):
        try:
            self.bot.answer_callback_query(call.id, Strings.not_subscribed_text(), True)
        except Exception as e:
            print(f"An error occurred in not_subscribed_alert: {e}")

    def send_refs_count(self, chat_id):
        try:
            self.bot.send_message(chat_id, Strings.refs_count(self.db.get_refs_count(str(chat_id))), parse_mode="HTML")
        except Exception as e:
            print(f"An error occurred in send_refs_count: {e}")

    def send_about_teachers(self, message):
        try:
            self.bot.send_media_group(
                message.chat.id,
                [
                    InputMediaPhoto(open("asilbek.jpg", 'rb'), Strings.about_teachers(), parse_mode="HTML"),
                    InputMediaPhoto(open("fayzulloh.jpg", 'rb')),
                ]
            )
        except Exception as e:
            print(f"An error occurred in send_about_teachers: {e}")

    def join_private_chat(self, chat_id):
        try:
            self.bot.send_message(
                chat_id,
                Strings.join_private_channel(),
                parse_mode="HTML",
                reply_markup=CustomInlineMarkup.inline_linked_keyboard(
                    {"Qo'shilish": str(
                        self.bot.create_chat_invite_link(self.private_chat_id, member_limit=1).invite_link)}
                )
            )
            self.bot.send_message(
                chat_id,
                "✅",
                parse_mode="HTML",
                reply_markup=CustomKeyboardMarkup.keyboard(
                    ["📎Taklif qilish havolasini olish"],
                    ["👩‍🏫🧑‍🏫Ustozlar haqida", "📕Kurs haqida"],
                    ["🧮Takliflarim soni"]
                )
            )

        except Exception as e:
            print(f"An error occurred in join_private_chat: {e}")

    def run(self):
        try:
            @self.bot.message_handler(commands=['start'])
            def send_welcome(message):
                try:
                    if len(message.text.split(' ')) == 2:
                        self.from_user = message.text.split(' ')[1]
                    self.start(message)
                except Exception as e:
                    print(f"An error occurred in send_welcome: {e}")

            @self.bot.message_handler()
            def message_handler(message):
                try:
                    if message.text == "📎Taklif qilish havolasini olish":
                        self.get_referral_link(message)

                    elif message.text == "👩‍🏫🧑‍🏫Ustozlar haqida":
                        self.send_about_teachers(message)

                    elif message.text == "📕Kurs haqida":
                        self.bot.send_message(message.chat.id, Strings.about_course(), parse_mode="HTML")

                    elif message.text == "🧮Takliflarim soni":
                        c = db.get_refs_count(message.chat.id)
                        self.bot.send_message(
                            message.chat.id,
                            Strings.refs_count(c),
                            parse_mode="HTML"
                        )
                        if c >= 5:
                            self.join_private_chat(message.chat.id)
                except Exception as e:
                    print(f"An error occurred in message_handler: {e}")

            @self.bot.callback_query_handler(func=lambda call: True)
            def callback_query_handler(call):
                try:
                    if call.data == Strings.check_button_text():
                        if self.is_subscribed(call.from_user.id):
                            self.bot.delete_message(call.message.chat.id, self.subscribe_msg)
                            if len(self.from_user) > 0 and not self.db.is_user_logged(call.message.chat.id):
                                name = self.db.get_user_name_by_id(call.message.chat.id)
                                number = self.db.get_user_number_by_id(call.message.chat.id)
                                self.db.increment_referral_count(self.from_user, name, number)
                                c = db.get_refs_count(self.from_user)
                                if c >= 5:
                                    self.join_private_chat(self.from_user)

                            if not self.db.is_user_logged(call.message.chat.id):
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
                            self.start(call.message)
                        else:
                            self.not_subscribed_alert(call)

                    if call.data == Strings.referral_button_text():
                        self.get_referral(call)
                except Exception as e:
                    print(f"An error occurred in callback_query_handler: {e}")

            @self.bot.message_handler(content_types=['contact'])
            def handle_contact(message):
                try:
                    self.number = str(message.contact.phone_number)
                    if self.from_user == key:
                        self.join_private_chat(message.chat.id)
                    elif self.is_subscribed(message.chat.id):
                        self.get_referral_link(message)
                        if not self.db.is_user_logged(message.chat.id):
                            self.db.create_user(message.chat.id, str(self.name), str(self.number))
                    else:
                        self.subscribe_text(message)
                except Exception as e:
                    print(f"An error occurred in handle_contact: {e}")

            self.bot.polling(none_stop=True)
        except Exception as e:
            print(f"An error occurred in run: {e}")


if __name__ == "__main__":
    bot = Bot(Strings.token())
    bot.run()
