

import asyncio
"""


async def x():
        asyncio.create_task(y())
    
    #while True:
        print("x1")
        
        await asyncio.sleep(10)
        
        print("x2")
    
    
async  def y():
    while True:
        print("y1")
        
        await asyncio.sleep(5)
        
        print("y2")
    
    
loop=asyncio.get_event_loop()

#asyncio.ensure_future(x())


loop.run_until_complete(x())

#   task.cancel()  görevi iptal eder.

# task.done( )  görev tamamlandıysa döndürür

#result() görev sonucu döndürür.

#asyncio.all_tasks() bitmemiş tüm görevleri döndürür.
#asyncio.current_task( döngü = Yok )  hiç görev kalmadısysa dödürür.
#not benim çıkarımlarıma göre create_task() ı sadece main fonksiyonun içinde çalıştıra bilirm
#sebebi ise run_until_complete(x())fonksiyonu main fonksiyon olarak çalışıyor






#Yukarıda ki olay ise şunu ifade eder 2 çeşit asenkron programlama yapabilirim.
#kısa süreli veya sonsuz döngüde bir while döngüsü kullanmam main içinde yeterli olacaktır.


"""
                            #            #

#aşağıda sonsuz döngülü bir main fonksiyonu içinde farklı asenkron 
#çalışan fonksiyonlara görevler verilecek. ve main içinde kendi işlemleride olacak.


async  def main():
    
    while True:
        task1=asyncio.create_task(f1())
        task2=asyncio.create_task(f2())
        
        task2_dönendeğer= await task2 
        print(task2_dönendeğer)
        
        
        print("main ilk ")
        await asyncio.sleep(3)
        
        print("main iki")


async def f1():
    print("f1 ilk")
    await asyncio.sleep(5)
    print("f1 iki")

async  def f2():
    
    print("f2 ilk")
    await asyncio.sleep(1)
    return 12
    #print("f2 iki")
    



asyncio.run(main())


#NOT MAİN YAPACAKSAm loop run_forever çalışmaz bu yüzden sadece run() kullanılır.
#daha doğrusu taskler olduğu için 

#not: asenkron çalışan bir fonksiyonda dönder değeri almak için bir değişkene
#atıp o değerin fonksiyon çalıştığında alınmasını beklemek lazım.



