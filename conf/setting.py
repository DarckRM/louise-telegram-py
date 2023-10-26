from typing import Any, Dict

from conf.setting_dev import SETTING_DEV
from conf.setting_prod import SETTING_PROD


SETTING: Dict[str, Any] = {
  "setting.env": "prod",
  # Configuration for telegram
  "telegram.token": "",
  "telegram.proxy.host": "127.0.0.1",
  "telegram.proxy.port": ":7890",

  # Log
  "log_level": "debug",

  # Custom config
  "bot.cache.images": ""
}

if SETTING["setting.env"] == 'dev':
  SETTING = SETTING_DEV

if SETTING["setting.env"] == 'prod':
  SETTING = SETTING_PROD