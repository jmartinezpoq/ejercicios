import asyncio
import random
import time
import sys

BOOTS = 0
start_time = 0

async def make_boot():
    global BOOTS
    manufacturing_time = random.choice([1,3,5])
    await asyncio.sleep(manufacturing_time)
    BOOTS += 1

async def print_data():
    while 1:
        global start_time
        await asyncio.sleep(1)
        current_time=loop.time()
        print("seconds: {} boots: {}".format(current_time-start_time,BOOTS))

async def worker():
    while 1:
        await make_boot()

async def main():
    await asyncio.gather(worker(), print_data())

def build_tasks(workers):
    tasks = [
        asyncio.ensure_future(print_data())]
    for _ in range(workers):
        tasks.append(asyncio.ensure_future(worker()))

    return tasks

if __name__ == "__main__":
    workers = int(sys.argv[1])
    loop = asyncio.get_event_loop()
    start_time=loop.time()
    tasks = build_tasks(workers)
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
