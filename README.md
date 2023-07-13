[![GitHub Repo stars](https://img.shields.io/github/stars/RusskiyPythonist/GameParserByGenre?style=social)](https://github.com/RusskiyPythonist/GameParserByGenre)
[![GitHub forks](https://img.shields.io/github/forks/RusskiyPythonist/GameParserByGenre?style=social)](https://github.com/RusskiyPythonist/GameParserByGenre)

**GameParserByGenre** -- скрипт-парсер для Python.

Данный скрипт берёт и анализирует информацию с сайта https://igromania.ru/games Тем самым парсит заданное количество страниц и выводит в консоль игры по жанру.

<img src="img/img.png">

**GameParserByGenre** -- программа с открытым исходным кодом и бесплатна для использования.

## Характеристики

- Работает на Windows
- Код написан на Python
- Открытый исходный ход
- Предел в кол-ве страниц: 23920

## Как запустить

### Windows

После установки [Python3](https://www.python.org/) (версии 3.7 или выше) необходимо выполнить следующую команду для установки необходимых библиотек:

```sh
pip install -r requirements.txt
```

Далее, Вы можете запустить файл **main.py** через Ваш IDE или выполнить следующую команду:

```sh
python main.py
```

## Как работает

После запуска файла, Вам предложит ввести кол-во страниц для парсинга. Кол-во выводимых игр напрямую зависит от кол-ва необходимых страниц.

### (ПРИМЕЧАНИЕ: Кол-во страниц может быть только **целым числом** и не привышать 23920)
