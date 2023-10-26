from typing import Any, Dict

from conf.setting import SETTING_DEV


SETTING: Dict[str, Any] = {
  "setting.env": "dev",
  # Configuration for telegram
  "telegram.token": "",
  "telegram.proxy.host": "127.0.0.1",
  "telegram.proxy.port": ":7890",

  # Log
  "log_level": "debug"
}

if SETTING["setting.env"] == 'dev':
  SETTING = SETTING_DEV