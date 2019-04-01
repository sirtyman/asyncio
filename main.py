import asyncio
import random


rpi_ms = 1
number_of_workers = 100


async def myCoroutine(id):
    sleep_time_ms = random.randint(1, 5) / 1000
    await asyncio.sleep(sleep_time_ms)

    while True:
        # print("Coroutine {}: Message sent".format(id))
        await asyncio.sleep(rpi_ms / 1000)


async def main():
    tasks = []
    for i in range(number_of_workers):
        tasks.append(asyncio.ensure_future(myCoroutine(i)))
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
