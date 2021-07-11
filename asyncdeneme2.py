

import asyncio

# NOT : aşşağıdan yukarı oku , İŞİNİ zorlaştırma.














async def f1():
        #while True:
            
            task = asyncio.create_task(f2())
        
            print("a")
            
            await asyncio.sleep(1)
            print("b")
            cevap= await f2()
            print("cevap: {}".format(cevap))
            #return 12
            
        
async def f2():
        
        print("1")
        await asyncio.sleep(2)
        print("2")
        return 15



loop=asyncio.get_event_loop() #loop oluşturur.

asyncio.ensure_future(f1())  #bu sonsuza dek çalı.tırmak için görev atama işlemidir
asyncio.ensure_future(f2())
loop.run_forever() #sonsuza dek çalış. görevlerin bitmiş olması önemli değildir.
#loop.run_until_complete(f1()) #içindeki görev bitne kadar çalış./diğerleri bitmeden 
#kendini kapatır diğer görevlerin önemi yoktur.
  
#asyncio.run(f1())









"""

async def f1():
        while True:
            
            task = asyncio.create_task(f2())
        
            print("a")
            
            await asyncio.sleep(1)
            print("b")
            cevap= await f2()
            print("cevap: {}".format(cevap))
            #return 12
            
        
async def f2():
        
        print("1")
        await asyncio.sleep(2)
        print("2")
        return 15



    
asyncio.run(f1())



# async while döngüsüne çıkartıp her hangi bir yerine 
#return attırsak fonksiyon döner ve işlemi bitirir.

#f1 ana/ main fonksiyon gibi düşünülmeli. bu yüzden devamlı
# bir işlem yapılması planlanıyorysa while içinde bulunmalı. başka fonksiyondan
#return alınabilir
#bunun dışında ana fonksiyon kapatılmadığı sürece her heşey yapılabilir.
#tek sıkıntısı fonksiyonun çağrıldığında kaldığı yerden değilde baştan kendini 
#çağırması.

#TODO BU BAŞTAN BAŞLAMA SORUNU araştıracağım.


#Coroutine terimi await eden fonksiyon anlamında bekleyen fonksiyon nesne.

"""

"""
async def f1():
        task = asyncio.create_task(f2())
    
        print("a")
        
        await asyncio.sleep(1)
        print("b")
        await f2()
    
async def f2():
    
    print("1")
    await asyncio.sleep(2)
    print("2")
    

asyncio.run(f1())


# task için daha güzel bir örnek : create_task şunu yapıyor.
# başla görev var bunu bir kenara koy boş olduğunda geçeriz
#print(a) yı bas  bekle şunu yap : -> bekle 1 saniye 
#şimdi bekliyoruz create taskta görev vardı onu yapalım boşuz. diyor
#1 saniye dolunca neyse daha sonra bakarız.
#print(b)  işlemini yapalım
#await f2() is yazmamın sebebi f2 fonksiyonu kaldığı yerden devam etmesi için.
#ancak awair f2() çalıştırınca görevi baştan başlıyor ve bitince ilk çağrılan f2()
#fonksiyonu çağrılıyor işini tamamlıyor bitiriyor.

"""




"""
async def f1():
    while True:
        print("a")
        
        await f2()
        print("b")
        await f2()
    
async def f2():
    
    print("1")
    await asyncio.sleep(2)
    print("2")
    
    
asyncio.run(f1())
"""
    

#NOTLAR:

#async bir kayword'dür yani anahtar kelimedir asenkron olduğunu yorumlayıcıya belirtir.
#bir askentron bir fonksiyon ancak başka bir asycnron fonksiyon ile çalışır.

#async  yazmadan await işlemi yapılamaz.

#await bekle -> beklerken şunu yap yada  şu işlemi yap demektir. 

#asyncio.run( asenkron olan bir fonksiyon çalıştırmalı)

#Ö N: bir main fonksiyon oluşturulup etrafında asyncron fonksiyonlar oluşturup
      #bir asenkton çalışan sistem yazılabilir.

