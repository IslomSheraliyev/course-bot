from telebot import TeleBot
from telebot.apihelper import ApiTelegramException
from components.custom_inline_markup import CustomInlineMarkup
from utils import get_channel_name

from res.strings import Strings
from res.constants import channels


class Bot:
    def __init__(self, token):
        self.bot = TeleBot(token)
        self.msg = -1

    def start(self, message):
        self.bot.send_message(
            message.chat.id,
            Strings.get_start_text(message.from_user.first_name),
            parse_mode="HTML"
        )

        if not self.is_subscribed(message.chat.id):
            self.subscribe_text(message)

    def subscribe_text(self, message):
        self.msg = self.bot.send_message(
            message.chat.id,
            Strings.get_subscribe_text(),
            parse_mode="HTML",
            reply_markup=CustomInlineMarkup.add_inline_button(
                CustomInlineMarkup.inline_linked_keyboard(*channels),
                {Strings.get_check_text(): Strings.get_check_text()}
            ) if not self.is_subscribed(message.chat.id) else None
        ).id

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

    def not_subscribed_alert(self, call):
        self.bot.answer_callback_query(call.id, Strings.get_not_subscribed_text(), True)

    def run(self):
        @self.bot.message_handler(commands=['start'])
        def send_welcome(message):
            self.start(message)

        @self.bot.callback_query_handler(func=lambda call: True)
        def callback_query_handler(call):
            if call.data == Strings.get_check_text():
                if self.is_subscribed(call.from_user.id):
                    self.bot.delete_message(call.message.chat.id, self.msg)
                else:
                    self.not_subscribed_alert(call)

        self.bot.polling(none_stop=True)


if __name__ == "__main__":
    bot = Bot(Strings.get_token())
    bot.run()
