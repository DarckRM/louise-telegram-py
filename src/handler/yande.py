import os
import random
from typing import List
import urllib3
from telegram import InputFile, InputMediaPhoto, Update
from telegram.ext import ContextTypes, filters


class YandeHandler():
  def __init__(self) -> None:
    self.filter_yande = filters.Regex('yande')
    self.http = urllib3.PoolManager()

  async def yande(self, update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    '''Handle yande command''' 
    text = 'Louise 开始请求图片咯'
    image_path = "E:\Pictures\Yande"
    files: List[str] = []
    photos: List[InputMediaPhoto] = []
    
    files = os.listdir(image_path)
    for id in [1, 2, 3]:
      index = random.randint(0, len(files) - 1)
      f = open(image_path + '/' + files[index], 'rb+')
      photos.append(InputMediaPhoto(f.read()))
      f.close()

    try:
      await ctx.bot.send_message(chat_id=update.effective_chat.id, text=text)
      await ctx.bot.send_media_group(chat_id=update.effective_chat.id, media=photos)
    except Exception as e:
      pass