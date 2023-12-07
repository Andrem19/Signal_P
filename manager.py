import managers_func as mf
import helpers.tlg as tel
from decouple import config
import os
import time
import asyncio
import sys


async def main():
    mf.api_token = config("SIGNAL_BOT")
    while True:
        await mf.check_and_handle_message()
        await mf.check_process_pids()
        time.sleep(2)
        


if __name__ == '__main__':
    asyncio.run(main())
