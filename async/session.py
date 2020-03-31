import aiohttp
import asyncio
import time

url = 'http://docs.aiohttp.org/en/stable/client_quickstart.html'


async def getapge(session, url):
    async with session.get(url, timeout=5) as resp:
        print(await resp.text())


async def main():
    async with aiohttp.ClientSession() as session:
        await getapge(session, url)

start = time.time()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
end = time.time()
print('spend time is {}'.format(end - start))
