# PyroBot

Simple Base for Users Who wants to make their own Telegram Bots in **[Pyrogram](http://github.com/Pyrogram/Pyrogram)** without any database.

## How to add modules?

- Fork and add your modules in **[pyrobot/modules](https://github.com/DivideProjects/PyroBot/blob/main/pyrobot/plugins)**
- Add Required ENV Variables in **[app.json](https://github.com/DivideProjects/PyroBot/blob/main/app.json)** & in **[vars.py](https://github.com/DivideProjects/PyroBot/blob/main/pyrobot/vars.py)**
- Add required external requirements in **[requirements.txt](https://github.com/DivideProjects/PyroBot/blob/main/requirements.txt)** or/and **[pyproject.toml](https://github.com/DivideProjects/PyroBot/blob/main/pyproject.toml)**

## Hosting

### Heroku

- Heroku Deploy is Very Simple, Just Click the Button Below

    [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/DivideProjects/PyroBot)

### Local Deploy

- `git clone https://github.com/DivideProjects/PyroBot.git`
- `cd PyroBot`
- `pip3 install -r requirements.txt`
- Edit The `vars.py` as per the instruction given there.
- `python3 -m pyrobot`

## Report Bugs

Report Bugs in [@DivideProjectsDiscussion](https://t.me/DivideProjectsDiscussion)

## Credits
- [Dan Tès](https://telegram.dog/haskell) for [Pyrogram Library](https://github.com/Pyrogram/Pyrogram)

## Powered By

[![DivideProjects](https://img.shields.io/badge/Divide-Projects-green?style=for-the-badge&logo=appveyor)](https://t.me/DivideProjectsDiscussion)
