import os
import random
from typing import List

from conf.setting import SETTING
from src.db.database import get_database
from src.http.http_client import HttpClient


class YandeService():

    def __init__(self):
        self.db = get_database()
        self.yande_token = ""

    def get_random_setu(self) -> List[bytes]:
        image_path = SETTING['bot.cache.images']
        files: List[str] = os.listdir(image_path)
        photos: List[bytes] = []

        for id in [1, 2, 3]:
            index = random.randint(0, len(files) - 1)
            f = open(image_path + '/' + files[index], 'rb+')
            photos.append(f.read())
            f.close()

        return photos

    def search_yande_image(self, cn_names: List[str], page: int = 1, limit: int = 10) -> List[str]:
        tags: str = ''
        for cn_name in cn_names:
            tag = self.db.get_booru_tag(cn_name) 
            if not tag:
                continue
            tags += tag.origin_name + '+'
        if len(tags) == 0:
            tags = '*+'

        results = HttpClient(True).url(f"https://yande.re/post.json?tag={tags[:-1]}&limit={limit}&page={page}").get()
        photos: List[bytes] = []
        for r in results:
            photos.append(HttpClient(True).url(r['file_url']).get_bytes())
        
        return photos

if __name__ == '__main__':
    service = YandeService()
    result = service.search_yande_image(['神里绫华', '黑丝'])
    print(result)