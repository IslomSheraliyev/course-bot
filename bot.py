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
        self.bot = TeleBot(token)
        self.subscribe_msg = -1
        self.description_msg = -1
        self.db = db()
        self.from_user = ""
        self.name = ""
        self.number = ""
        self.private_chat_id = -1002119653669

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

    # Implement other methods similarly with try-except blocks

    def run(self):
        try:
            @self.bot.message_handler(commands=['start'])
            def send_welcome(message):
                if len(message.text.split(' ')) == 2:
                    self.from_user = message.text.split(' ')[1]
                self.start(message)

            # Add other handlers here

            self.bot.polling(none_stop=True)
        except Exception as e:
            print(f"An error occurred in run: {e}")


if __name__ == "__main__":
    try:
        bot = Bot(Strings.token())
        bot.run()
    except Exception as e:
        print(f"An error occurred: {e}")
