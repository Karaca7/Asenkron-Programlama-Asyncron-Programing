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
**Doktor sizi muayene ettikten sonra "Yok kardeşim ben bu adam iyilene kadar başka hiç kimseyi muayene etmeyeceğim (başka işlem yapmayacaım)!"** demez.
<br>
**Siz gönderdikten sonra hemen başka bir hasta alır (muayene eder)(İşlemleri gerçekleştirir) ve onuda gönderir .Sonra başka bir hasta, sonra başka bir hasta...

 Dikkat edilmesi gereken nokta burasıdır doktor burda asenkron çalışır. Bunu büyütecek Göklere çıkarıcak bir şey değildir. 

**Sonra sizin kontrol vaktiniz gelir ve doktor. sizi tekrar çağırı ,arar ve sizi muayene eder(tekrar işlemleri kontrol eder) iyileşmişseniz işlemi burada bitirir. iyileşmemişseniz tekrar ilaç yazar ve siz gittiğinizde başka hastaları kontorl etmeye devam eder.Siz iyleşmiş olsaydınızda doktor hastaları muayene etmeye devam edecekti. Tabi bunu biz yazdığımız kodda bitir demiş olmasaydık.


Umarım derdimi analta bilmişimdir. 

Şimdi pastanın malzemelerine bir göz gezdirelim !
### Anahtar kelimeler/Keywords
#### asyncio:

    import asyncio

asyncron programlama yapabilmemiz için python dan bununla ilgli bir araca ihtiyacımız var. Bunun yapabilmenin bir kaç yolu daha var fakat bu yol bana daha basit ve anlaşılır geliyor.

#### async def x():




