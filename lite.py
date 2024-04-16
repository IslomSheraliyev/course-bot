from telebot import TeleBot
from strings import Strings
from ReferralSystemDBManager import ReferralSystemDBManager as db


class Bot:
    def __init__(self, token):

        self.bot = TeleBot(token)
        self.db = db()
        self.name = ""
        self.phone_number = ""

    def start(self, message):

        self.bot.send_message(
            chat_id=message.chat.id,
            text=Strings.welcome_lite(message.from_user.first_name),
            parse_mode="HTML"
        )

        self.bot.register_next_step_handler(
            message=message,
            callback=self.get_name
        )

    def get_name(self, message):

        self.name = str(message.text)

        self.bot.send_message(
            chat_id=message.chat.id,
            text=Strings.ask_number(),
            parse_mode="HTML"
        )

        self.bot.register_next_step_handler(
            message=message,
            callback=self.get_phone_number
        )

    def get_phone_number(self, message):

        self.phone_number = str(message.text)

        self.bot.register_next_step_handler(
            message=message,
            callback=self.send_post
        )

    def save_user(self, message):

        db.create_user(
            user_id=message.chat.id,
            name=self.name,
            number=self.phone_number
        )

    def send_post(self, message):

        pass

    def run(self):
        try:
            @self.bot.message_handler(commands=['start'])
            def start(message):

                self.start(message)

            self.bot.polling(none_stop=True)

        except Exception as e:
            print(e)

        finally:
            self.run()


if __name__ == "__main__":
    bot = Bot(Strings.token())
    bot.run()
