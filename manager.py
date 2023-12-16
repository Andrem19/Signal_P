import managers_func as mf
import helpers.tlg as tel
from decouple import config
import os
import time
import asyncio
from datetime import datetime
import sys


async def main():
    mf.api_token = config("SIGNAL_BOT")
    while True:
        current_time = datetime.now()
        await mf.check_and_handle_message()
        if current_time.minute in [3, 7, 13, 22, 27, 23, 37, 42, 47, 53, 57] and current_time.second in [32,33,34,35]:
            await mf.watcgdog()
            await mf.check_process_pids()
        time.sleep(3)
        


if __name__ == '__main__':
    asyncio.run(main())
