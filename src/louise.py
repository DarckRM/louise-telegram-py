import time
from telegram import Update
from telegram.ext import Application, ApplicationBuilder, CallbackQueryHandler, CommandHandler, ContextTypes, MessageHandler, Updater

from conf.setting import SETTING
from src.handler.base import BaseHandler
from src.handler.yande import YandeHandler
from src.util.log import Log

class Louise():

  base: BaseHandler = BaseHandler()
  yande:  YandeHandler = YandeHandler()

  def __init__(self):
    self.log: Log = Log(self)
    proxy = 'http://' + SETTING['proxy.host'] + SETTING['proxy.port']
    if SETTING["setting.env"] == 'dev':
      self.bot: Application = ApplicationBuilder().token(SETTING['telegram.token']).proxy_url(proxy).get_updates_proxy_url(proxy).build()
    else:
      self.bot: Application = ApplicationBuilder().token(SETTING['telegram.token']).build()
    # command hanlder
    self.start_handler = CommandHandler('start', self.base.start)
    # message handler
    self.yande_handler = MessageHandler(self.yande.filter_yande, self.yande.yande)
    # inline button handler
    self.menu_handler = CallbackQueryHandler(self.base.menu_callback)

    self.bot.add_handler(self.start_handler)
    self.bot.add_handler(self.yande_handler)
    self.bot.add_handler(self.menu_handler)
    




