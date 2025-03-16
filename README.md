# ElanLibs

**`Efekan Nefesoğlu` ve `Elanur Tuana İşcen` Tarafından Geliştirilmiştir**

## Giriş

Elan, günlük programlama görevlerini kolaylaştırmak için geliştirilmiş çok yönlü bir Python kütüphanesidir. Bu kütüphane, yaygın matematik işlemleri, liste manipülasyonları, string (metin) işleme ve temel görüntü işleme görevleri için kullanımı kolay ve anlaşılır bir arayüz sunar.

Elan kütüphanesi, kod tekrarını azaltmak ve proje geliştirme sürecini hızlandırmak için tasarlanmıştır. Tek bir tutarlı arayüz ile farklı tipteki işlemleri gerçekleştirebilirsiniz.

## Amaç

Elan'ın amacı, tekerleği yeniden icat etmek yerine, yaygın kullanılan işlevleri tek bir pakette toplayarak geliştirme sürecinizi hızlandırmaktır. Kütüphane şu alanlarda yardımcı fonksiyonlar sunar:

- Temel matematiksel işlemleri
- Liste manipülasyonları
- Metin işleme ve dönüştürme
- Görüntü işleme (gri tonlama, boyutlandırma, döndürme)

## Kurulum

Elan kütüphanesi PyPI üzerinden kolayca kurulabilir:

```bash
pip install elan
```

### Bağımlılıklar

Elan kütüphanesinin düzgün çalışması için aşağıdaki gereksinimler otomatik olarak kurulur:

- Python 3.6 veya üzeri
- OpenCV (görüntü işleme işlevleri için)

## Kullanım

Elan kütüphanesini kullanmak için öncelikle ana sınıfı içe aktarmanız ve bir örnek oluşturmanız gerekir:

```python
from elan import elan

# Elan sınıfını başlat
el = elan()
```

Bu örnek üzerinden tüm fonksiyonlara erişebilirsiniz.

### Matematiksel İşlevler

`math` modülü, temel matematiksel işlemler için kullanışlı fonksiyonlar sağlar:

```python
# Toplama işlemi
sonuc = el.math.add(5, 3)  # Sonuç: 8

# Çıkarma işlemi
sonuc = el.math.subtract(10, 4)  # Sonuç: 6

# Çarpma işlemi
sonuc = el.math.multiply(3, 5)  # Sonuç: 15

# Bölme işlemi
sonuc = el.math.divide(10, 2)  # Sonuç: 5.0

# Üs alma
sonuc = el.math.power(2, 3)  # Sonuç: 8 (2³)

# Karekök
sonuc = el.math.square_root(16)  # Sonuç: 4.0

# Küpkök
sonuc = el.math.cube_root(27)  # Sonuç: 3.0

# Kare
sonuc = el.math.square(4)  # Sonuç: 16

# Küp
sonuc = el.math.cube(3)  # Sonuç: 27

# Faktöriyel
sonuc = el.math.factorial(5)  # Sonuç: 120 (5! = 5×4×3×2×1)
```

#### Çoklu Sayı İşlemleri

`math` modülü ayrıca birden fazla sayı ile çalışmanızı sağlayan fonksiyonlar da sunar:

```python
# İstediğiniz kadar sayıyı toplama
sonuc = el.math.sum_all(1, 2, 3, 4, 5)  # Sonuç: 15

# İstediğiniz kadar sayıyı çarpma
sonuc = el.math.multiply_all(1, 2, 3, 4, 5)  # Sonuç: 120

# Sayıların ortalamasını alma
sonuc = el.math.average(1, 2, 3, 4, 5)  # Sonuç: 3.0

# En büyük değeri bulma
sonuc = el.math.max_value(1, 5, 3, 9, 2)  # Sonuç: 9

# En küçük değeri bulma
sonuc = el.math.min_value(1, 5, 3, 9, 2)  # Sonuç: 1

# En büyük ve en küçük değer arasındaki farkı bulma (aralık)
sonuc = el.math.range_value(1, 5, 3, 9, 2)  # Sonuç: 8

# Sayıların medyanını bulma
sonuc = el.math.median(1, 3, 5, 7, 9)  # Sonuç: 5
sonuc = el.math.median(1, 3, 5, 7)  # Sonuç: 4.0 (çift sayıda eleman olduğunda ortadaki iki sayının ortalaması)
```

### String (Metin) İşlevleri

`string` modülü, metinlerle çalışmak için çeşitli yardımcı fonksiyonlar sunar:

```python
# Metni tersine çevirme
sonuc = el.string.reverse("Merhaba")  # Sonuç: "abahreM"

# İlk harfi büyük yapma
sonuc = el.string.capitalize("merhaba dünya")  # Sonuç: "Merhaba dünya"

# Tüm metni büyük harfe çevirme
sonuc = el.string.uppercase("merhaba")  # Sonuç: "MERHABA"

# Tüm metni küçük harfe çevirme
sonuc = el.string.lowercase("MERHABA")  # Sonuç: "merhaba"

# Her kelimenin ilk harfini büyük yapma
sonuc = el.string.title("merhaba dünya")  # Sonuç: "Merhaba Dünya"

# Harflerin büyük/küçük durumunu tersine çevirme
sonuc = el.string.swapcase("Merhaba")  # Sonuç: "mERHABA"

# Metnin sadece harflerden oluşup oluşmadığını kontrol etme
sonuc = el.string.isalpha("Merhaba")  # Sonuç: True
sonuc = el.string.isalpha("Merhaba123")  # Sonuç: False

# Metnin sadece rakamlardan oluşup oluşmadığını kontrol etme
sonuc = el.string.isdigit("12345")  # Sonuç: True
sonuc = el.string.isdigit("12a45")  # Sonuç: False

# Metnin hem harf hem rakam içerip içermediğini kontrol etme
sonuc = el.string.isalnum("abc123")  # Sonuç: True

# Metnin tümünün küçük harf olup olmadığını kontrol etme
sonuc = el.string.islower("merhaba")  # Sonuç: True

# Metnin tümünün büyük harf olup olmadığını kontrol etme
sonuc = el.string.isupper("MERHABA")  # Sonuç: True

# Metnin her kelimesinin ilk harfinin büyük olup olmadığını kontrol etme
sonuc = el.string.istitle("Merhaba Dünya")  # Sonuç: True

# Metnin sadece boşluklardan oluşup oluşmadığını kontrol etme
sonuc = el.string.isspace("   ")  # Sonuç: True

# Metnin yazdırılabilir olup olmadığını kontrol etme
sonuc = el.string.isprintable("Merhaba\n")  # Sonuç: False

# Metnin geçerli bir Python tanımlayıcısı olup olmadığını kontrol etme
sonuc = el.string.isidentifier("valid_name")  # Sonuç: True

# Metindeki her kelimeyi tersine çevirme
sonuc = el.string.reverse_words("Merhaba Dünya")  # Sonuç: "abahreM aynüD"
```

#### Yazım Denetimi ve Düzeltme İşlevleri

`string` modülü, Türkçe ve İngilizce metinlerde yazım hatalarını düzeltmek için gelişmiş işlevler sunar:

```python
# Dil tespiti
dil = el.string.detect_language("merhaba dünya")  # Sonuç: "tr"
dil = el.string.detect_language("hello world")    # Sonuç: "en"

# Türkçe kelime düzeltme
oneriler = el.string.suggest_correction("meraba", language="tr")  
# Sonuç: ['merhaba']

# İngilizce kelime düzeltme 
oneriler = el.string.suggest_correction("helo", language="en")
# Sonuç: ['hello']

# Otomatik dil tespiti ile kelime düzeltme
oneriler = el.string.suggest_correction("meraba")  # Türkçe olarak tespit edilir
# Sonuç: ['merhaba']

oneriler = el.string.suggest_correction("helo")    # İngilizce olarak tespit edilir
# Sonuç: ['hello']

# Birden fazla öneri alma
oneriler = el.string.suggest_correction("selm", language="tr", max_suggestions=3)  
# Sonuç: ['selam', 'ses', 'film'] gibi

# Türkçe metin düzeltme
duzeltilmis_metin = el.string.correct_text("meraba naslsın", language="tr")
# Sonuç: "merhaba nasılsın"

# İngilizce metin düzeltme
duzeltilmis_metin = el.string.correct_text("helo worl", language="en")
# Sonuç: "hello world"

# Otomatik dil tespiti ile metin düzeltme
duzeltilmis_metin = el.string.correct_text("meraba nasilsin")  # Türkçe olarak tespit edilir
# Sonuç: "merhaba nasılsın" 

# Düzeltme mesafesini ayarlama (daha esnek düzeltmeler için)
duzeltilmis_metin = el.string.correct_text("merhba nasilsin", language="tr", max_distance=3)
# Sonuç: "merhaba nasılsın"

# Kelime veri tabanını güncelleme
# Daha fazla kelime ile kelime havuzunu genişletmek için:
success = el.string.update_word_database()  # Hem Türkçe hem İngilizce
success = el.string.update_word_database(language="tr")  # Sadece Türkçe
success = el.string.update_word_database(language="en")  # Sadece İngilizce
```

### Liste İşlevleri

`list` modülü, listelerle çalışmak için kullanışlı fonksiyonlar sunar:

```python
# Listeyi ters çevirme
sonuc = el.list.reverse([1, 2, 3, 4, 5])  # Sonuç: [5, 4, 3, 2, 1]

# Listeyi sıralama
sonuc = el.list.sort([3, 1, 4, 2, 5])  # Sonuç: [1, 2, 3, 4, 5]

# Listeden tekrarlayan öğeleri kaldırma (benzersiz liste)
sonuc = el.list.unique([1, 2, 2, 3, 3, 4, 5, 5])  # Sonuç: [1, 2, 3, 4, 5]
```

### Görüntü İşleme İşlevleri

`image` modülü, temel görüntü işleme işlevleri sunar. Bu işlevler OpenCV kütüphanesini kullanır:

```python
# Bir görüntüyü gri tonlamaya çevirme
gri_resim = el.image.to_grayscale('resim.jpg')

# Bir görüntüyü yeniden boyutlandırma
boyutlandirilmis_resim = el.image.resize('resim.jpg', 800, 600)

# Bir görüntüyü döndürme (açı derece cinsinden)
dondurulmus_resim = el.image.rotate('resim.jpg', 90)  # 90 derece döndürme

# Not: Bu fonksiyonlar OpenCV görüntü nesneleri döndürür.
# Görüntüyü kaydetmek için OpenCV'nin imwrite fonksiyonunu kullanabilirsiniz:
import cv2
cv2.imwrite('gri_resim.jpg', gri_resim)
```

## Örnek Kullanım Senaryoları

### Senaryo 1: Metinsel İşlemler

```python
from elan import elan

el = elan()

# Kullanıcı girdisini işleme
metin = "merhaba dünya"
print(f"Orijinal metin: {metin}")
print(f"Başlık formatında: {el.string.title(metin)}")
print(f"Tersi: {el.string.reverse(metin)}")
print(f"Sadece harflerden mi oluşuyor? {el.string.isalpha(metin.replace(' ', ''))}")
```

### Senaryo 2: Basit Hesaplama Programı

```python
from elan import elan

el = elan()

# Hesaplama işlemleri
sayi1 = 10
sayi2 = 5

print(f"{sayi1} + {sayi2} = {el.math.add(sayi1, sayi2)}")
print(f"{sayi1} - {sayi2} = {el.math.subtract(sayi1, sayi2)}")
print(f"{sayi1} × {sayi2} = {el.math.multiply(sayi1, sayi2)}")
print(f"{sayi1} ÷ {sayi2} = {el.math.divide(sayi1, sayi2)}")
print(f"{sayi1}^{sayi2} = {el.math.power(sayi1, sayi2)}")
print(f"{sayi1}! = {el.math.factorial(sayi1)}")

# Çoklu sayılar ile işlemler
sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Sayıların toplamı: {el.math.sum_all(*sayilar)}")
print(f"Sayıların çarpımı: {el.math.multiply_all(*sayilar)}")
print(f"Sayıların ortalaması: {el.math.average(*sayilar)}")
print(f"En büyük sayı: {el.math.max_value(*sayilar)}")
print(f"En küçük sayı: {el.math.min_value(*sayilar)}")
print(f"Sayıların aralığı: {el.math.range_value(*sayilar)}")
print(f"Sayıların medyanı: {el.math.median(*sayilar)}")
```

### Senaryo 3: Çokdilli Yazım Denetimi ve Düzeltme Uygulaması

```python
from elan import elan

el = elan()

# Dil tespiti
texts = ["merhaba dünya", "hello world", "merhaba world"]
for text in texts:
    dil = el.string.detect_language(text)
    print(f"'{text}' metni {dil} dilinde")

# Yanlış yazılmış metinleri düzeltme
yanlis_metinler = {
    "tr": "meraba nasilsin bugun hva nasil",
    "en": "helo worl, how ar you tody"
}

for dil, metin in yanlis_metinler.items():
    duzeltilmis = el.string.correct_text(metin, language=dil)
    print(f"\n{dil.upper()} dili:")
    print(f"Orijinal: {metin}")
    print(f"Düzeltilmiş: {duzeltilmis}")

# Kullanıcı girdisi ile yazım denetimi
user_input = input("\nBir kelime yazın: ")
dil = el.string.detect_language(user_input)
print(f"Tespit edilen dil: {dil}")

oneriler = el.string.suggest_correction(user_input, language=dil, max_suggestions=5)
print(f"Öneriler: {oneriler}")
```

### Senaryo 4: Görüntü İşleme Uygulaması

```python
from elan import elan
import cv2

el = elan()

# Orijinal görüntüyü yükle ve işle
resim_yolu = "ornek_resim.jpg"

# Gri tonlama dönüşümü
gri_resim = el.image.to_grayscale(resim_yolu)
cv2.imwrite("gri_resim.jpg", gri_resim)

# Görüntüyü yeniden boyutlandırma
boyutlandirilmis_resim = el.image.resize(resim_yolu, 300, 200)
cv2.imwrite("boyutlandirilmis_resim.jpg", boyutlandirilmis_resim)

# Görüntüyü döndürme
dondurulmus_resim = el.image.rotate(resim_yolu, 45)  # 45 derece döndürme
cv2.imwrite("dondurulmus_resim.jpg", dondurulmus_resim)

print("Görüntü işleme tamamlandı!")
```

## Sorun Giderme

### Sık Karşılaşılan Hatalar

**ImportError: No module named 'elan'**  
Çözüm: Paketi pip ile yüklediğinizden emin olun: `pip install elan`

**ModuleNotFoundError: No module named 'cv2'**  
Çözüm: OpenCV'yi yükleyin: `pip install opencv-python`

**Diğer hata türleri**  
Eğer herhangi bir hata ile karşılaşırsanız, lütfen GitHub deposunda bir issue açın.

## Katkı Rehberi

Elan projesine katkıda bulunmak için:

1. Depoyu fork edin
2. Kendi branch'inizi oluşturun (`git checkout -b yeni-ozellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik ekle'`)
4. Değişikliklerinizi branch'e push edin (`git push origin yeni-ozellik`)
5. Bir Pull Request oluşturun

## Sık Sorulan Sorular

**S: Hangi Python sürümü gereklidir?**  
C: Elan, Python 3.6 veya üstü gerektirir.

**S: Elan kütüphanesini ticari projelerde kullanabilir miyim?**  
C: Evet, Elan MIT Lisansı altında yayınlanmıştır ve ticari kullanıma uygundur.

**S: Elan nasıl telaffuz edilir?**  
C: "E-LAN" şeklinde telaffuz edilir.

**S: Kütüphaneyi nasıl güncellerim?**  
C: `pip install --upgrade elan` komutunu kullanarak kütüphanenin son sürümünü yükleyebilirsiniz.

**S: Görüntü işleme fonksiyonları nasıl çalışır?**  
C: Görüntü işleme fonksiyonları, OpenCV kütüphanesini kullanır ve görüntü işleme işlemleri için bir OpenCV nesnesi döndürür.

**S: Yazım denetimi ve düzeltme işlevleri hangi dilleri destekler?**  
C: Şu anda Türkçe ve İngilizce dillerini destekler. Otomatik dil tespiti özelliği ile yazılan metnin diline göre düzeltmeler yapılabilir.

**S: Kelime veri tabanı ne kadar büyüktür?**  
C: İlk kurulumda temel bir kelime kümesi gelir. `update_word_database()` fonksiyonu ile daha kapsamlı kelime havuzları internet üzerinden indirilebilir.

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

## İletişim

Herhangi bir soru, öneri veya geri bildirim için:

- GitHub: [https://github.com/efekannn5/ElanLibs](https://github.com/efekannn5/ElanLibs)
- E-posta: efekan8190nefesogeu@gmail.com

### Powered By Efekan Nefesoğlu

