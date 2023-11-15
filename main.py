"""main"""
import asyncio
import hashlib
import os
from datetime import datetime

from dotenv import load_dotenv

from http_client import get_async

load_dotenv()

BASE_URL = "http://gateway.marvel.com/"


async def main() -> None:
    """main()"""

    timestamp = datetime.now()
    public_api_key = os.getenv("PUBLIC_API_KEY")
    private_api_key = os.getenv("PRIVATE_API_KEY")

    to_be_hashed = f"{timestamp}{private_api_key}{public_api_key}"
    md5 = hashlib.md5()
    md5.update(to_be_hashed.encode("utf-8"))
    md5_hex = md5.hexdigest()

    endpoint = "v1/public/characters"

    response = await get_async(
        f"{BASE_URL}{endpoint}?ts={timestamp}&apikey={public_api_key}&hash={md5_hex}"
    )

    print(response)


if __name__ == "__main__":
    asyncio.run(main())
