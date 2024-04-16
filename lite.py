from telebot import TeleBot
from strings import Strings
from LiteSystemDBManager import LiteSystemDBManager as db
from CustomKeyboardMarkup import CustomKeyboardMarkup


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
            parse_mode="HTML",
            reply_markup=CustomKeyboardMarkup.get_number_keyboard()
        )

    def send_post(self, message):
        pass

    def run(self):
        try:
            @self.bot.message_handler(commands=['start'])
            def start(message):

                if db.is_user_logged(message.chat.id):
                    self.bot.register_next_step_handler(
                        message,
                        self.send_post
                    )
                else:
                    self.start(message)

            @self.bot.message_handler(content_types=['contact'])
            def handle_contact(message):
                self.phone_number = str(message.contact.phone_number)

                self.db.create_user(
                    user_id=message.chat.id,
                    name=self.name,
                    number=self.phone_number
                )

                self.bot.register_next_step_handler(
                    message=message,
                    callback=self.send_post
                )

            self.bot.polling(none_stop=True)

        except Exception as e:
            print(e)

        finally:
            self.run()


if __name__ == "__main__":
    bot = Bot(Strings.token())
    bot.run()
