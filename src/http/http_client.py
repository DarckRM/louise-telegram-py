import asyncio
import nest_asyncio
import json
import platform
from typing import Any, Dict
import aiohttp
import traceback
from aiohttp import ClientError, TCPConnector
from conf.setting import SETTING

from src.util.log import Log
nest_asyncio.apply()
class HttpClient():
    def __init__(self, proxy: bool = False) -> None:
        self.log = Log(self)
        self.url: str
        if proxy:
            self.proxy_url = "http://" + SETTING['proxy.host'] + SETTING['proxy.port']
        else:
            self.proxy_url = None
    
    def url(self, url: str):
        self.url = url
        return self

    def get_bytes(self):
        return asyncio.get_event_loop().run_until_complete(self._get_bytes(self.url))

    def get(self):
        # 修改默认策略
        return asyncio.get_event_loop().run_until_complete(self._get(self.url))

    async def _get(self, url: str):
        try:
            async with aiohttp.ClientSession(connector=TCPConnector(ssl=False)) as session:
                async with session.get(url, proxy=self.proxy_url) as resp:
                    result = await self._handle_json_response(resp, '<>')
                    return result
        except ClientError as e:
            self.log.fatal(f"请求 {url} client失败: {e}\n{traceback.format_exc()}")
            return []
        except Exception as e:
            self.log.fatal(f"请求 {url} 失败: {e}\n{traceback.format_exc()}")
            return []
    
    async def _get_bytes(self, url: str):
        try:
            async with aiohttp.ClientSession(connector=TCPConnector(ssl=False)) as session:
                async with session.get(url, proxy=self.proxy_url) as resp:
                    result = await resp.read()
                    return result
        except ClientError as e:
            self.log.fatal(f"请求 {url} client失败: {e}\n{traceback.format_exc()}")
            return []
        except Exception as e:
            self.log.fatal(f"请求 {url} 失败: {e}\n{traceback.format_exc()}")
            return []

    # 检查 HTTP 状态码 这是确认请求是否正常
    async def check_statu_code(self, resp: aiohttp.ClientResponse) -> bool:
        if resp.status != 200:
            x = await resp.text(encoding='utf-8')
            if x:
                self.log.error(x[:200])
            else:
                self.log.error("接口返回空数据")
            return False
        else:
            return True

    async def _handle_json_response(self, resp: aiohttp.ClientResponse, endpoint: str) -> Any:
        if await self.check_statu_code(resp) is False:
            return {}
        result = await resp.text(encoding='utf-8')
        if result == "":
            self.log.warn(f"处理 {endpoint} 响应: 接口返回空字符串")
            return {}
        try:
            result_json = json.loads(result)
        except Exception as e:
            self.log.error(f"JSON 序列化异常 {e} 原始数据: {result[:200]}\n{traceback.format_exc()}")
            return {}
        return result_json

if __name__ == '__main__':
    result = HttpClient(True).url("https://yande.re/post.json").get()