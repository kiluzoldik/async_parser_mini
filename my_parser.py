import aiohttp
import aiofiles
from bs4 import BeautifulSoup
from base_func import create_table, insert_product
import asyncio


# async def fetch(session, url, cookies, headers):
#     async with session.get(url, cookies=cookies, headers=headers) as response:
#         return await response.text()


async def get_data():
    #     url = 'https://xn----8sbznhlgig.xn--p1ai/katalog/ventilyaciya/'
    #     cookies = {
    #         'SSESS5c499e5050c481d0dd662f3874ca5c92': '0d81781ab8dc62399522e6d64fce6d57',
    #         '_ym_uid': '1715628812950650244',
    #         '_ym_d': '1715628812',
    #         'cted': 'modId%3Druiqbb8v%3Bya_client_id%3D1715628812950650244',
    #         '_ym_isad': '1',
    #         '_ym_visorc': 'w',
    #     }

    #     headers = {
    #         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    #         'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    #         'priority': 'u=0, i',
    #         'referer': 'https://xn----8sbznhlgig.xn--p1ai/katalog/arenda-instrumenta-i-tehniki/',
    #         'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    #         'sec-ch-ua-mobile': '?0',
    #         'sec-ch-ua-platform': '"Windows"',
    #         'sec-fetch-dest': 'document',
    #         'sec-fetch-mode': 'navigate',
    #         'sec-fetch-site': 'same-origin',
    #         'sec-fetch-user': '?1',
    #         'upgrade-insecure-requests': '1',
    #         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    #     }

    #     async with aiohttp.ClientSession() as session:
    #         html = await fetch(session, url, cookies, headers)

    #     async with aiofiles.open('res.html', 'w', encoding='utf-8') as file:
    #         await file.write(html)

    async with aiofiles.open('res.html', encoding='utf-8') as file:
        src = await file.read()

    soup = BeautifulSoup(src, "lxml")
    product_name = soup.find_all("div", class_="product__top-block")

    for name in product_name:
        text_name = name.find("a", class_='product__name').text
        text_price = name.find("div", class_='product__price').text
        text_price = float(" ".join(text_price.split('руб. / шт')))
        text_article = name.find('div', class_="vendor-code").find('span').text
        insert_product(text_name, text_price, text_article)

if __name__ == '__main__':
    create_table()
    asyncio.run(get_data())
