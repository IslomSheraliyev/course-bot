from telebot.types import KeyboardButton, ReplyKeyboardMarkup


class CustomKeyboardMarkup(object):
    @staticmethod
    def keyboard(*rows: list) -> ReplyKeyboardMarkup:
        markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        for row in rows:
            inline_row = []
            for text in row:
                inline_row.append(KeyboardButton(text=text))
            markup.row(*inline_row)
        return markup

    @staticmethod
    def get_number_keyboard():
        markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        markup.add(KeyboardButton("Raqamimni yuborish", request_contact=True))
        return markup
