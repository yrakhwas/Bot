import asyncio
from aiogram import Bot, Dispatcher,types
from dotenv import find_dotenv, load_dotenv
import os

from handlers.user_group import user_group_router
from handlers.user_private import user_private_router
from common.bot_cmds_list import listOfCommands

load_dotenv(find_dotenv())

bot = Bot(token=os.getenv('TOKEN'))


dp = Dispatcher()

dp.include_router(user_private_router)
dp.include_routers(user_group_router)

async def main():
    await bot.delete_webhook(drop_pending_updates=True) 
    await bot.set_my_commands(commands=listOfCommands,scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot)


asyncio.run(main())