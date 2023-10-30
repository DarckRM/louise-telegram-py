import traceback

from typing import List
from peewee import MySQLDatabase, IntegerField, Model, CharField

from conf.setting import SETTING
from src.model.model import BooruTags
from src.util.log import Log


db: MySQLDatabase = MySQLDatabase(
    database=SETTING['db.name'],
    host=SETTING['db.host'],
    port=SETTING['db.port'],
    user=SETTING['db.user'],
    password=SETTING['db.password'],
    charset="utf8mb4",

)


class DbBooruTags(Model):
    tag_id: int = IntegerField(primary_key=True)
    origin_name: str = CharField()
    cn_name: str = CharField()
    alter_name: str = CharField()
    producer: str = CharField()
    info: str = CharField()

    class Meta:
        database: MySQLDatabase = db
        db_table = "t_booru_tags"


class LousieDatabase():
    def __init__(self) -> None:
        self.log = Log(self)
        self.db: MySQLDatabase = db
        try:
            self.db.connect()
        except Exception as e:
            self.log.error(f"无法连接至基础数据库: {e}\n{traceback.format_exc()}")

    def demo(self) -> List[BooruTags]:
        booru_tags: List[BooruTags] = []
        try:
            db_booru_tags: List[DbBooruTags] = DbBooruTags.select()
            for d in db_booru_tags:
                booru_tags.append(BooruTags(
                    tag_id=d.tag_id,
                    origin_name=d.origin_name,
                    cn_name=d.cn_name,
                    alter_name=d.alter_name,
                    producer=d.producer,
                    info=d.info
                ))
            return booru_tags
        except Exception as e:
            self.log.error(f"获取 BooruTag 列表失败: {e}\n{traceback.format_exc()}")
            return []

database: LousieDatabase = None

def get_database() -> LousieDatabase:
    global database
    if database:
        return database
    database = LousieDatabase()
    return database

if __name__ == '__main__':
    louise = get_database()
    louise.demo()