import asyncio
import random
import time

BOOTS = 0
start_time = time.time()

async def make_boot():
    global BOOTS
    manufacturing_time = random.choice([1,3,5])
    await asyncio.sleep(manufacturing_time)
    BOOTS += 1

async def print_data():
    while 1:
        global start_time
        await asyncio.sleep(1)
        current_time=time.time()
        print("seconds: {} boots: {}".format(current_time-start_time,BOOTS))

async def worker():
    while 1:
        await make_boot()

async def main():
    await asyncio.gather(worker(), print_data())


asyncio.run(main())
