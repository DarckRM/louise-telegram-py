from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext, ContextTypes

from src.handler.yande import YandeHandler


class BaseHandler():

    def __init__(self) -> None:
        self.yande = YandeHandler()

    async def menu_callback(self, update: Update, ctx: CallbackContext):
        query = update.callback_query
        await query.answer()
        await query.edit_message_text(text=f"选择的值: {query.data}")

        if query.data == 'yande':
            await self.yande.yande(update, ctx)

        if query.data == 'yande_search':
            await self.yande.yande_search(update, ctx)

    async def start(self, update: Update, ctx: ContextTypes.DEFAULT_TYPE):
        '''Response command start'''
        menu = [
            [
                InlineKeyboardButton("随机色图", callback_data='yande'),
                InlineKeyboardButton("搜索涩图", callback_data='yande_search')
            ],
            [
                InlineKeyboardButton("Bottom button", callback_data='under')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(menu)
        await update.message.reply_text("请选择: ", reply_markup=reply_markup)

    async def louise_menu(self, update: Update, ctx: CallbackContext):
        pass
