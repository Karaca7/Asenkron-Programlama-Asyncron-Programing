
import asyncio





async def hasta1():
     print("hastalığın belirtelirini anlatıyor.1")
     await asyncio.sleep(4)
     print("hasta tedavi oluyor ilaç falan 1")
    



async def hasta2():
     print("hastalığın belirtelirini anlatıyor.2")
     await asyncio.sleep(2)
     print("hasta tedavi oluyor ilaç falan 2")
    

async def hasta3():
     print("hastalığın belirtelirini anlatıyor.3")
     await asyncio.sleep(6)
     print("hasta tedavi oluyor ilaç falan 3")
async def doktor():
    task1=asyncio.create_task(hasta1())
    task2=asyncio.create_task(hasta2())
    task2=asyncio.create_task(hasta3())
    
    
    while True:
        print("ıvır zıvır")
        
    
        
        
        await asyncio.sleep(4)
    
    

asyncio.run(doktor())
    