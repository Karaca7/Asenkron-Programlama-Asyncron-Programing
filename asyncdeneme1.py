import asyncio




async def yfosnkiyon():
    print("asdasdsa")
    await asyncio.sleep(3)
    print("safsaf")

async def xfonksiyonu():
    
         asyncio.create_task( yfosnkiyon())

         print("ıvır zırı")
         await asyncio.sleep(3)
         
         

asyncio.run(xfonksiyonu())
         