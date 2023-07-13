import re
import aiohttp
import asyncio
from time import perf_counter
from bs4 import BeautifulSoup

games_list = []
games_list_new = []


async def main(page_num: int):
    async with aiohttp.ClientSession() as request:
        for page in range(1, page_num+1):
            response = await request.get(f'https://www.igromania.ru/games/all/all/all/all/all/0/{page}/')
            soup = BeautifulSoup(await response.text(), 'lxml')
            try:
                find_game = soup.find('div', class_='knb-main isDekstop').find('div', class_='CommonBasePage_page__qeHj5').find('div', class_='CommonBasePage_page_content__3jBIF').find('section', class_='CommonBaseItems_wrap__KOpx4').find(
                    'div', class_='InfiniteScrollWrap_content__e8viv').find('div', class_="knb-list knb-list--gap20 knb-list--row2 knb-list--columns4")
                find_name = find_game.find_all('a', attrs={'class': re.compile('GameCard_title')})

                for game in find_name:
                    genre = game.parent.parent.parent.find('footer', attrs={'class': re.compile('GameCard_footer')}).find_all('div', attrs={'class': re.compile('GameCard_genres')})[0].text
                    game_link = f'https://www.igromania.ru' + game.get('href')
                    games_list.append([game.text, game_link, genre])
            except:
                pass


if __name__ == '__main__':
    page_num = int(input('Введите кол-во страниц: '))
    start = perf_counter()

    if page_num > 0 and page_num <=23920:
        asyncio.run(main(page_num))
        genre = input('Введите жанр игры: ')
        for i in range(len(games_list)):
            if genre in games_list[i][2]:
                games_list_new.append([games_list[i][0], games_list[i][1], games_list[i][2]])

        for i in range(len(games_list_new)):
            print(f'{i + 1}. Название игры - {games_list_new[i][0]} | Описание игры - {games_list_new[i][1]} | Жанр - {games_list_new[i][2]}')
    else:
        print('Лимит: 23920 страниц.')
    print(f'time: {(perf_counter() - start):.02f}')
