import os
import random
from typing import List, Tuple
from telegram import InputFile, InputMediaPhoto, Update
from telegram.ext import ContextTypes, filters

from src.logic.yande import YandeService
from util.log import Log


class YandeHandler():
    def __init__(self) -> None:
        self.filter_yande = filters.Regex('^yande')
        self.yande_service = YandeService()

        self.log = Log(self)

    async def yande(self, update: Update, ctx: ContextTypes.DEFAULT_TYPE):
        '''Handle yande command'''
        self.log.debug(f"收到消息: {update.message}")
        in_text: str = update.message.text
        in_text.strip()

        if len(in_text) < 6:
            return

        if '/' in in_text:
            return
        reply = 'Louise 开始搜索图片咯' 
        await ctx.bot.send_message(chat_id=update.effective_chat.id, text=reply)

        page_nation: List[int] = []        
        cn_names: List[str] = []
        photos: List[InputMediaPhoto] = []
        text_array: List[str] = in_text.split(' ')

        text_array.pop(0)
        for word in text_array:
            if word.isdigit():
                page_nation.append(int(word))
            else:
                cn_names.append(word)

        if len(page_nation) == 0:
            page_nation = [1, 3]

        for photo_bytes in self.yande_service.search_yande_image(cn_names, page_nation[0], page_nation[1]):
            photos.append(InputMediaPhoto(photo_bytes))

        try:
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
    
    def yande_search(self):
        pass