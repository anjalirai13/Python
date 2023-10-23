import asyncio

async def print_sum(x, y):
    print("Compute %s + %s ..." % (x, y))
    await asyncio.sleep(1.0)
    return x + y

async def print_sub(x, y):
    print("Compute %s - %s ..." % (x, y))
    await asyncio.sleep(1.0)
    return x - y

async def math_cal(x, y):
    result = await print_sum(x, y)
    print("%s + %s = %s" % (x, y, result))
    result = await  print_sub(x, y)
    print("%s - %s = %s" % (x, y, result))

loop = asyncio.get_event_loop()
loop.run_until_complete(math_cal(3, 2))
loop.close()