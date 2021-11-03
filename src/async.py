import asyncio
#
# async def main_func():
#     print("Start")
#     await second_func("Running second func")
#     print("Done")
#
# async def second_func(msg):
#     print(msg)
#     await asyncio.sleep(2)
#
#
#
# asyncio.run(main_func())
#
#





#
# async def main_func():
#     print('Start')
#     task = asyncio.create_task(second_func('task 2 running'))
#     await asyncio.sleep(1)
#     print('finish 1')
#     await task
#
#
#
#
# async def second_func(msg):
#
#     print(msg)
#     await asyncio.sleep(5)
#     print("Finish 2")
#
#
#
# asyncio.run(main_func())

#
async  def hae_data():
    print("Aloitetaan datan haku")
    await asyncio.sleep(1)
    print("Haku valmis")
    return {'data':1}


async def tulosta_luvut():
    print("Start printing numbers")
    for i in range(10):
        print(i)
        await asyncio.sleep(1)



async def main():

    task1 = asyncio.create_task(hae_data())
    task2 = asyncio.create_task(tulosta_luvut())

    data = await task1

    print(data)

    await task2
#
#
asyncio.run(main())
#
