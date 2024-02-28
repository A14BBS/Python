import aiohttp
import fake_useragent
from bs4 import BeautifulSoup
import asyncio

ua = fake_useragent.UserAgent().random
headers = {'user-agent': ua} 

async def cha_():
    async with aiohttp.ClientSession(headers=headers) as session:
        response = await session.get('https:_______________', timeout=10)
        html = await response.text()
        soup = BeautifulSoup(html, 'html.parser')
        last_news = soup.find_all('a', class_='newsitem news_item_title')
        print(last_news)

        
        
if __name__ == "__main__":
    asyncio.run(cha_())
