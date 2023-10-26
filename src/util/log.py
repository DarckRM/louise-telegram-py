import datetime
import threading
from enum import Enum
from typing import Any

from conf.setting import SETTING

class LogLevel(Enum):
    FATAL: int = 0
    ERROR: int = 1
    WARN: int = 2
    INFO: int = 3
    DEBUG: int = 4
    TEST: int = 5


class Log:

    def __init__(self, target: Any, level: str = SETTING["log_level"]):
        if type(target) is str:
            class_name = target
        else:
            class_name = target.__class__.__name__
        if level == "fatal":
            self.level = LogLevel.FATAL
        elif level == "error":
            self.level = LogLevel.ERROR
        elif level == "warn":
            self.level = LogLevel.WARN
        elif level == "info":
            self.level = LogLevel.INFO
        elif level == "debug":
            self.level = LogLevel.DEBUG
        elif level == "test":
            self.level = LogLevel.TEST

        if len(class_name) > 12:
            class_name = class_name[0:11]
        self.class_name = class_name

    def output(self, message: str):
        t = threading.current_thread()
        print('[%s][%.8s][%.14s]%s' % (
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), self.class_name, f'{t.ident}-{t.name}', message))

    def fatal(self, message: str):
        self.output(f'[FATAL]: {message}')

    def error(self, message: str):
        if self.level.value > LogLevel.FATAL.value:
            self.output(f'[ERROR]: {message}')

    def warn(self, message: str):
        if self.level.value > LogLevel.ERROR.value:
            self.output(f'[ WARN]: {message}')

    def info(self, message: str):
        if self.level.value > LogLevel.WARN.value:
            self.output(f'[ INFO]: {message}')

    def debug(self, message: str):
        if self.level.value > LogLevel.INFO.value:
            self.output(f'[DEBUG]: {message}')

    def test(self, message: str):
        if self.level.value > LogLevel.DEBUG.value:
            self.output(f'[ TEST]: {message}')
