# Asenkron-Programlama-Asyncron-Programing
Buraya gelmişseniz zaten senkronize program işinizi görmediğinden gelmişsinizdir.
Neyse devam edelim !
## Tanım:
Bu tanımlama biraz değilleme gibi olacak ama kusura bakmayın.
Bir fonksiyonun methodun  artık her neyse birbirlerinin sonuçlarını beklemeden sırasız olarak çalıştığı programlama biçimidir. Burada programımız doğrusal bir akışta çalışmaz.


Bu tanımın size hiçbir faydası olmaz. 


### Örnek:

Hastaneye gittiniz. 
Doktor sizi muayene etti ve ilacınızı yazdı. 
**Doktor sizi muayene ettikten sonra "Yok kardeşim ben bu adam iyileşene kadar başka hiç kimseyi muayene etmeyeceğim (başka işlem yapmayacaım)!"** demez.
<br>
**Siz gönderdikten sonra hemen başka bir hasta alır (muayene eder)(İşlemleri gerçekleştirir) ve onuda gönderir .Sonra başka bir hasta, sonra başka bir hasta...**

 **Dikkat edilmesi gereken nokta burasıdır doktor burda asenkron çalışır. Bunu büyütecek Göklere çıkarıcak bir şey değildir. ***

**Sonra sizin kontrol vaktiniz gelir ve doktor. sizi tekrar çağırı ,arar ve sizi muayene eder(tekrar işlemleri kontrol eder) iyileşmişseniz işlemi burada bitirir. iyileşmemişseniz tekrar ilaç yazar ve siz gittiğinizde başka hastaları kontorl etmeye devam eder.Siz iyleşmiş olsaydınızda doktor hastaları muayene etmeye devam edecekti. Tabi bunu biz yazdığımız kodda bitir demiş olmasaydık.

**İyide bunu thread le ne farkı var ?
Thread programlama yaptığınızda yani aynı anda birden fazla akışa sahip oluruz. bu akışlar sonuç bağımlılığından kurtulamaz. asenkron programlama burada programın işlemi bitip bitirmediğiyle ililenmez. !!!

Umarım derdimi analta bilmişimdir. 

Şimdi pastanın malzemelerine bir göz gezdirelim !

#### asyncio:

    import asyncio

Asenkron programlama yapabilmemiz için python dan bununla ilgli bir araca ihtiyacımız var. Bunun yapabilmenin bir kaç yolu daha var fakat bu yol bana daha basit ve anlaşılır geliyor.
### Anahtar kelimeler/Keywords


#### async :

    async def xfonksiyonu():
    
"async " python tarafından bizim için tanımlanmış özel bir anahatar kelimedir. nasıl fonskiyon olduğunu belirtmek istiyorsak "def" kullanıyoruz buda böyle bir şey.

bunun yorumlayıcımızın  bu bir asenkron fonksiyon/method olduğunun farkına varıp çalışırkenki biçimini ona göre almasını sağlamak için.

#### await :

    async def xfonksiyonu():
         print("ıvır zırı")
         awat asyncio.sleep(3)
         await yfosnkiyon()
         
"await"  beklemek demektir.Yani işi bitirene kadar bekle anlamındadır.  asyncio.sleep()  ise sleep methodu ise time.sleep() fonskiyonu ile aynı işlemi yapar.










