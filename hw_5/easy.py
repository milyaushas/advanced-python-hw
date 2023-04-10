import aiohttp
import asyncio
import sys


async def get_picture(session, id):
    url = "https://picsum.photos/200.jpg"

    async with session.get(url) as resp:
        path = f"artifacts/easy/{id}.jpg"
        with open(path, "bw") as file:
            file.write(await resp.read())


async def download_pictures(n):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(1, n + 1):
            tasks.append(asyncio.ensure_future(get_picture(session, i)))
        await asyncio.gather(*tasks)


def main():
    n = int(sys.argv[1])
    asyncio.run(download_pictures(n))


if __name__ == "__main__":
    main()
