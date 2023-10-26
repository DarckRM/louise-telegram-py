from telegram import Update
from telegram.ext import ContextTypes

class BaseHandler():
  def __init__(self) -> None:
    pass

  async def start(self, update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    '''Response command start'''
    text = 'Hello my master!'
    try:
      await ctx.bot.send_message(chat_id=update.effective_chat.id, text=text)
    except Exception as e:
      pass