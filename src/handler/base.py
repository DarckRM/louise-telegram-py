from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext, ContextTypes

class BaseHandler():
  
  def __init__(self) -> None:
    pass

  async def menu_callback(self, update: Update, ctx: CallbackContext):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=f"选择的值: {query.data}")

  async def start(self, update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    '''Response command start'''
    menu = [
      [
        InlineKeyboardButton("随机色图", callback_data='yande'),
        InlineKeyboardButton("Moe button", callback_data='moe moe')
      ],
      [
        InlineKeyboardButton("Bottom button", callback_data='under')
      ]
    ]
    reply_markup = InlineKeyboardMarkup(menu)
    await update.message.reply_text("请选择: ", reply_markup=reply_markup)

  
  async def louise_menu(self, update: Update, ctx: CallbackContext):
    pass
