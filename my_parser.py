import asyncio
import aiohttp
import time
from bs4 import BeautifulSoup
from base_func import create_table, insert_product


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as resp:
                print(f'{resp.status} - {url}')
                if resp.status == 200:
                    return await resp.text()
        except Exception as e:
            print(f'Ошибка {url}: {e}')


def parse_html(task):
    html = task.result()
    if html:
        soup = BeautifulSoup(html, "lxml")
        product_name = soup.find_all("div", class_="product__top-block")
        for name in product_name:
            text_name = name.find("a", class_='product__name').text
            text_price = name.find("div", class_='product__price').text
            text_price = float(" ".join(text_price.split('руб. / шт')))
            text_article = name.find(
                'div', class_="vendor-code").find('span').text
            insert_product(text_name, text_price, text_article)


async def main():
    create_table()
    url = 'https://xn----8sbznhlgig.xn--p1ai/katalog/ventilyaciya/'
    task = asyncio.create_task(fetch(url))
    task.add_done_callback(parse_html)
    await task  # Ожидаем завершения задачи

if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main())
    end_time = time.time()
    print(f"Время выполнения: {end_time - start_time} секунд")
