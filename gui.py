from utils.dialog import Dialogs
from logging import getLogger
import async_eel
import asyncio
import logging


log = getLogger(__name__)
loop = asyncio.get_event_loop()
dialogs = Dialogs()


@async_eel.expose
async def return_hello():
    return "Hello world!!"


@async_eel.expose
async def open_dialog():
    path = dialogs.open_dialog()
    return str(path)


@async_eel.expose
async def nice_meet_you():
    from random import choice
    return choice([
        'Weee are the world',
        'Your name is daigo',
        'Too match eating'
    ])


async def printer(message):
    print('callback: ', message)


async def callback_example():
    try:
        while True:
            await async_eel.my_rand()(printer)
            await asyncio.sleep(4)
    except Exception:
        log.debug("callback_example", exc_info=True)


async def loop_comment():
    try:
        while True:
            data = await async_eel.my_rand()()
            print('comment: ', data)
            await asyncio.sleep(5)
    except Exception:
        log.debug("loop_comment", exc_info=True)


async def main():
    async_eel.init('web')
    await async_eel.start('index.html', mode='edge')
    async_eel.spawn(callback_example)
    async_eel.spawn(loop_comment)
    log.info("success start app")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run_coroutine_threadsafe(main(), loop)
    loop.run_forever()
