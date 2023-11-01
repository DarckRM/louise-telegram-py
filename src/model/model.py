class BooruTag():
    def __init__(self, tag_id: int, origin_name: str, cn_name: str, alter_name: str, producer: str, info: str) -> None:
        self.tag_id: int = tag_id
        self.origin_name: str = origin_name
        self.cn_name: str = cn_name
        self.alter_name: str = alter_name
        self.producer: str = producer
        self.info: str = info