import asyncio 

async def work():
    await asyncio.sleep(2)
    print("task complete")

asyncio.run (work()) #event loop



