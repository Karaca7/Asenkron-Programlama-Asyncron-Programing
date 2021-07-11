import asyncio



import time

async  def hastene():
    
    await doktor("Tip1 hasta")
    
    await doktor("Tip2 hasta")
    
    await doktor("Tip3 hasta")
    

async def doktor(hasta_tipi):
    while True:
        
        print("hasta_tipi,tedaviye başlandı:{}".format(hasta_tipi))
        await asyncio.sleep(3)
        print("hasta_tipi iyileşti:{}".format(hasta_tipi))
    

asyncio.run(hastene())