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

После того, как Вы ввели количество страниц, Вам предложит ввести жанр или платформу игры. Ввести можно следующие жанры и платформы:

## Жанры

- Beat-em-Up
- FPS
- Hack And Slash
- MMO
- MOBA
- Point & Click
- Roguelike
- TD
- TPS
- Аркада
- Визуальная новелла
- Выживание
- Гонки
- Игра для взрослых
- Интерактивное кино
- История
- Квест
- ККИ
- Кооператив
- Менеджер
- Метроидвания
- Музыка
- Настольная игра
- Обучение
- Паззл
- Платформер
- Пошаговая стратегия
- Приключение
- Ролевая игра
- Симулятор
- Симулятор ходьбы
- Спорт
- Стелс
- Стратегия
- Стратегия в реальном времени
- Тактика
- Файтинг
- Хоррор

## Платформы

- PC
- Xbox One
- PlayStation 5
- PS4
- Xbox Series
- Nintendo Switch
- PS3
- Wii
- Xbox 360
- Wii U
- PS Vita
- NDS
- 3DS
- Android
- iOS
- 2DS
- 3DO
- Acorn Archimedes
- Acorn Electron
- Amiga
- Amstrad CPC
- Apple II
- Apple Pippin
- Arcade automats
- Atari
- Atari 2600
- Atari 5200
- Atari 7800
- Atari 8-bit
- Atari Flashback
- Atari Lynx
- Atari ST
- Atari XEGS
- BBC Micro
- BlackBerry
- Capcom Home Arcade
- CD-i
- Classic Macintosh
- ColecoVision
- Commodore 64
- CP System
- Dingoo A320
- Dragon
- Enterprise
- Epoch Cassette Vision
- Facebook
- FM Towns
- FreeBSD
- Fujitsu Micro
- Game & Watch
- Game Gear
- Game.com
- GameCube
- GB
- GBA
- GBC
- Google Stadia
- GP2X Wiz
- HTC Vive
- IBM PC
- Intellivision
- Intellivision Amico
- iQue Player
- Jaguar
- Linux
- Mac
- Mobile Phones
- vMS-DOS
- MSX
- MTX
- N-Gage
- N64
- NEC PC
- Neo Geo Pocket Color
- Neo-Geo
- NES
- New 3DS
- Nintendo Classic Mini: SNES
- Nintendo DSi
- NVIDIA Shield
- NX
- Pocket PC
- PS
- PS VR
- PS VR2
- PS2
- PS4 Pro
- PSP
- SAM Coupe
- Satellaview
- SEGA 32X
- Sega CD
- Sega Dreamcast
- Sega Genesis
- Sega Master System
- Sega Mega-Tech
- Sega Pico
- Sega Saturn
- SG-1000
- Sharp X1
- Sharp X68000
- SNES
- Steam Machines
- SuperGrafx
- Tandy 1000
- Thomson
- TI-99/4A
- Timex Sinclair
- TRS-80
- TurboGrafx-16
- Unix
- Vectrex
- Virtual Boy
- VR
- Web
- Windows Mobile
- WonderSwan
- Xbox
- Xbox One X
- Zeebo
- ZX Spectrum
- Консоли
- Социальные сети
- Электрочайники

При **правильном** вводе жанра игры, консоль выведет сообщение, в формате:
```sh
Название игры - [Название] | Описание игры - [Ссылка на страницу игры на сайте] | Жанр - [Жанр(ы) игры] | Платформа - [Платформа на которой(ых) доступна игра]
```

Если Вы ввели несуществующий жанр или платформу (см. списки выше) или жанр (платформу) которого(ой) нету на странице, то программа ничего не выведет и завершит работу.
