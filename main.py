import re
import aiohttp
import asyncio
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
                    platform = game.parent.parent.parent.find('header', attrs={'class': re.compile('GameCard_header')}).find('div', attrs={'class': re.compile('GameCard_platforms')}).find_all('a')
                    game_platform = ''
                    for i in platform:
                        game_platform = i.text.split()
                    game_link = f'https://www.igromania.ru' + game.get('href')
                    games_list.append([game.text, game_link, genre, game_platform])
            except:
                pass


if __name__ == '__main__':
    try:
        page_num = int(input('Введите кол-во страниц: '))
        if page_num > 0 and page_num <=23920:
            asyncio.run(main(page_num))
            genre = input('Введите жанр или платформу игры: ')
            for i in range(len(games_list)):
                if genre in games_list[i][2] or genre in games_list[i][3]:
                    games_list_new.append([games_list[i][0], games_list[i][1], games_list[i][2], games_list[i][3]])

            for i in range(len(games_list_new)):
                print(f'{i + 1}. Название игры - {games_list_new[i][0]} | Описание игры - {games_list_new[i][1]} | Жанр - {games_list_new[i][2]} | Платформа - {games_list_new[i][3]}')
        else:
            print('Лимит: 23920 страниц.')
    except:
        print('Возникла ошибка программы. Попробуйте ещё раз.')