import nonebot
from os import path

import config

if __name__ == '__main__':
    nonebot.init(config)
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'nonebot_plugins'),
        'nonebot_plugins'
    )
    nonebot.run()
