"""Http client with asyncrounous methods"""
import asyncio

import requests

JSON = int | str | float | bool | None | dict[str, "JSON"] | list["JSON"]
JSONObject = dict[str, JSON]
JSONList = list[JSON]


def get(url: str) -> JSONObject:
    """Get request syncronous"""
    response = requests.get(url, timeout=10)
    return response.json()


async def get_async(url: str) -> JSONObject:
    """Get asyncronous"""
    return await asyncio.to_thread(get, url)
