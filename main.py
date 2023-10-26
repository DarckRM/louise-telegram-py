import time
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, Application
from conf.setting import SETTING
from src.louise import Louise
from src.util.log import Log

class BootApplication():
  def __init__(self):
    self.log = Log(self)
    self.louise = Louise()


if __name__ == '__main__':

  boot_loader = BootApplication()
  boot_loader.log.info(f"开始启动 Bot")
  boot_loader.louise.bot.run_polling()

  while True:
    time.sleep(3)