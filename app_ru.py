import asyncio
from art import *
from termcolor import colored

from jutsu import JutSu, get_link_and_download


async def main():

    tprint("JutSu, quidix.")

    url = input("🔎Введите ссылку на аниме")

    if url.startswith("http"):
        slug = url.split("/")[3]
        season = url.split("/")[4] if len(url.split("/")) > 4 else None
        print('Anime name:', slug)
        print('Season:', season)
    else:
        return print("⛔Введите правильную ссылку!")

    res = input("🎦Введите разрешение (1080, 720, 480, 360, с разрешением может менятся размер видео):")

    download_type = input("Загружать синхронно?🤔 \nЗагружать синхронно ✅ (1)\nАсинхронная загрузка ❌ (2)\nYour Choice: ")

    if res not in ("1080", "720", "480", "360"):
        return print("⛔Введите правильное разрешение!")

    jutsu = JutSu(slug)

    episodes = await jutsu.get_all_episodes(season=season)
    print(f"Fetched {len(episodes)} episodes")

    if download_type == "1":
        for episode in episodes:
            await get_link_and_download(jutsu, episode, res)

    elif download_type == "2":
        tasks = [get_link_and_download(jutsu, episode, res, False) for episode in episodes]
        await asyncio.gather(*tasks)

    else:
        print(":/")

    await jutsu.close()


if __name__ == "__main__":
    asyncio.run(main())
