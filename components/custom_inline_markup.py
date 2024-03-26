from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


class CustomInlineMarkup(object):

    @staticmethod
    def inline_keyboard(*rows: dict) -> InlineKeyboardMarkup:
        markup = InlineKeyboardMarkup()
        for row in rows:
            inline_row = []
            for key, value in row.items():
                inline_row.append(InlineKeyboardButton(text=key, callback_data=value))
            markup.row(*inline_row)
        return markup

    @staticmethod
    def inline_linked_keyboard(*rows: dict) -> InlineKeyboardMarkup:
        markup = InlineKeyboardMarkup()
        for row in rows:
            inline_row = []
            for text, url in row.items():
                inline_row.append(InlineKeyboardButton(text=text, url=url))
            markup.row(*inline_row)
        return markup

    @staticmethod
    def add_inline_button(markup: InlineKeyboardMarkup, *raws: dict) -> InlineKeyboardMarkup:
        for raw in raws:
            inline_markup = []
            for text, url in raw.items():
                inline_markup.append(InlineKeyboardButton(text=text, callback_data=url))
            markup.row(*inline_markup)
        return markup
