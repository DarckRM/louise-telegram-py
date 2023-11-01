import os
import random
from typing import List
import urllib3
from telegram import InputFile, InputMediaPhoto, Update
from telegram.ext import ContextTypes, filters

from src.logic.yande import YandeService


class YandeHandler():
    def __init__(self) -> None:
        self.filter_yande = filters.Regex('yande')
        self.http = urllib3.PoolManager()
        self.yande_service = YandeService()

    async def yande(self, update: Update, ctx: ContextTypes.DEFAULT_TYPE):
        '''Handle yande command'''
        text = 'Louise 开始请求图片咯'

        photos: List[InputMediaPhoto] = []
        for photo_bytes in self.yande_service.get_random_setu():
            photos.append(InputMediaPhoto(photo_bytes))

        try:
            await ctx.bot.send_message(chat_id=update.effective_chat.id, text=text)
            await ctx.bot.send_media_group(chat_id=update.effective_chat.id, media=photos)
        except Exception as e:
            pass
        
    async def yande_search(self, update: Update, ctx: ContextTypes.DEFAULT_TYPE):
        '''Handle yande search command'''
        text = 'Louise 开始搜索图片咯'

        photos: List[InputMediaPhoto] = []
        for photo_bytes in self.yande_service.search_yande_image(['萝莉']):
            photos.append(InputMediaPhoto(photo_bytes))
        # photos.append(InputMediaPhoto("http://lights.rmdarck.icu/img/paimon_and_lumine.png"))

        try:
            await ctx.bot.send_message(chat_id=update.effective_chat.id, text=text)
            await ctx.bot.send_media_group(chat_id=update.effective_chat.id, media=photos)
        except Exception as e:
            pass
