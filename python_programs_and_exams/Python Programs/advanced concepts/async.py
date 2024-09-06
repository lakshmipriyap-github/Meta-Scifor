import asyncio
async def Sample():
    print ("Waiting using asyncio")
    for i in range(0,5):
        await asyncio.sleep(1)
        print (i)
    print ("Finished waiting.")

obj = Sample()
asyncio.run(obj)

