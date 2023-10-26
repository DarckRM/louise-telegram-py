import os
import random
from typing import List

from conf.setting import SETTING

class YandeService():
  
  def __init__(self):
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