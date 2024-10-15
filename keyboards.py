from telegram import InlineKeyboardButton, InlineKeyboardMarkup

inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Check four class for CLS', callback_data='type:fourclass'), InlineKeyboardButton(text='Is COVID', callback_data='type:iscovid')],
        [InlineKeyboardButton(text='Cancel', callback_data='type:cancel')]
    ]
)