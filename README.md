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

Elan kütüphanesini pip kullanarak kurabilirsiniz:

```
pip install elan
```

Bu komut sadece Elan'ın temel özelliklerini (matematik, string, liste işlemleri) kurar.

### Modüler Kurulum

Elan kütüphanesi modüler bir yapıda tasarlanmıştır. İhtiyacınıza göre sadece belirli özellikleri kurabilirsiniz:

1. **Temel Kurulum** (Matematik, String, Liste işlemleri):
   ```
   pip install elan
   ```

2. **Görüntü İşleme Özellikleri** (OpenCV ile görüntü düzenleme):
   ```
   pip install elan[image]
   ```

3. **Yüz Algılama Özellikleri** (dlib, face_recognition ve mediapipe ile):
   ```
   pip install elan[face]
   ```

4. **Tam Kurulum** (Tüm özellikleri içerir):
   ```
   pip install elan[all]
   ```

#### Windows Kullanıcıları için Önemli Not

Windows platformunda dlib ve face_recognition kurulumunda sorun yaşıyorsanız, iki kurulum yöntemi sunuyoruz:

**1. Kolay Yöntem (Önerilen):** Önceden derlenmiş binary wheel kullanımı:
```
pip install https://github.com/jloh02/dlib/releases/download/v19.22/dlib-19.22.99-cp310-cp310-win_amd64.whl
pip install face_recognition
pip install elan[face]
```

**2. Manuel Derleme Yöntemi:**
- [CMake](https://cmake.org/download/) indirin ve kurun
- [Visual Studio Community](https://visualstudio.microsoft.com/downloads/) (C++ geliştirme araçlarını seçin) indirin ve kurun
- Daha sonra terminalde: `pip install dlib`
- Ardından: `pip install face_recognition`
- Son olarak: `pip install elan[face]`

### Kurulum Doğrulama

Kurulumu doğrulamak için:

```python
import elan

# Temel özellikleri test et
print(elan.math.add(5, 3))  # 8 yazmalı

# Görüntü işleme modülünü kontrol et
try:
    img = elan.image.load("resim.jpg")
    print("Görüntü işleme özellikleri çalışıyor!")
except ImportError:
    print("Görüntü işleme özellikleri kurulu değil - pip install elan[image]")

# Yüz algılama modülünü kontrol et
try:
    yuzler = elan.image.detect_faces("resim.jpg")
    print(f"{len(yuzler)} yüz bulundu!")
except ImportError:
    print("Yüz algılama özellikleri kurulu değil - pip install elan[face]")
```

### Kurulum Sorunları ve Çözümleri

Kurulum sırasında sorunlarla karşılaşırsanız:

1. **OpenCV (Görüntü İşleme) Sorunları:**
   ```
   pip install --upgrade opencv-python
   ```

2. **Dlib / Face Recognition Sorunları:**
   - Windows: Yukarıdaki özel kurulum talimatlarını izleyin
   - Linux/macOS: `sudo apt-get install -y build-essential cmake` veya `brew install cmake`

3. **Eksik Özellikler:**
   - Elan, eksik modüller için otomatik olarak uyarı verecektir
   - İlgili modülü `pip install elan[image]` veya `pip install elan[face]` ile kurabilirsiniz

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

`image` modülü, gelişmiş görüntü işleme işlevleri sunar. Bu modül OpenCV kütüphanesini arka planda kullanır ancak kullanıcının OpenCV bilmesine gerek kalmadan kolay bir arayüz sağlar:

```python
# Bir görüntüyü gri tonlamaya çevirme
gri_resim = el.image.to_grayscale('resim.jpg')
# veya işlenmiş görüntüyü doğrudan kaydetme
el.image.to_grayscale('resim.jpg', output_path='gri_resim.jpg')

# Bir görüntüyü yeniden boyutlandırma
boyutlandirilmis_resim = el.image.resize('resim.jpg', 800, 600)
# En-boy oranını koruyarak boyutlandırma
el.image.resize('resim.jpg', 800, 0, keep_aspect_ratio=True, output_path='boyutlandirilmis_resim.jpg')

# Bir görüntüyü döndürme (açı derece cinsinden)
dondurulmus_resim = el.image.rotate('resim.jpg', 90)  # 90 derece döndürme

# Görüntüyü kırpma (x, y, genişlik, yükseklik)
kirpilmis_resim = el.image.crop('resim.jpg', 100, 100, 300, 200)

# Görüntüye bulanıklık ekleme
bulanik_resim = el.image.add_blur('resim.jpg', blur_type='gaussian', kernel_size=5)
# Farklı bulanıklık tipleri: 'gaussian', 'median', 'box'

# Kenar tespiti yapma
kenarlar = el.image.detect_edges('resim.jpg', method='canny', threshold1=100, threshold2=200)
# Farklı kenar tespit yöntemleri: 'canny', 'sobel'

# Parlaklık ayarlama (1.0 değişim yok, >1.0 daha parlak, <1.0 daha karanlık)
parlak_resim = el.image.adjust_brightness('resim.jpg', factor=1.5)

# Kontrast ayarlama (1.0 değişim yok, >1.0 daha fazla kontrast, <1.0 daha az kontrast)
kontrastli_resim = el.image.adjust_contrast('resim.jpg', factor=1.3)

# Histogram eşitleme (görüntü iyileştirme)
iyilestirilmis_resim = el.image.equalize_histogram('resim.jpg')

# Görüntüye metin ekleme
resim_metin = el.image.add_text('resim.jpg', 'Merhaba Dünya', position=(50, 50), 
                               font_size=1, color=(255, 0, 0), thickness=2)

# Görüntüye dikdörtgen ekleme
resim_dikdortgen = el.image.add_rectangle('resim.jpg', top_left=(50, 50), 
                                         bottom_right=(150, 150), color=(0, 255, 0))

# Yüz tespiti
resim_yuzler, yuzler = el.image.detect_faces('resim.jpg', draw_rectangles=True)
print(f"Tespit edilen yüz sayısı: {len(yuzler)}")

# Sanatsal filtreler uygulama
sepya_resim = el.image.apply_filter('resim.jpg', filter_type='sepia')
negatif_resim = el.image.apply_filter('resim.jpg', filter_type='negative')
karakalem_resim = el.image.apply_filter('resim.jpg', filter_type='sketch')
karikatur_resim = el.image.apply_filter('resim.jpg', filter_type='cartoon')

# İki görüntüyü birleştirme (harmanlanma)
birlesik_resim = el.image.merge_images('resim1.jpg', 'resim2.jpg', 
                                      weight1=0.7, weight2=0.3)

# Görüntüyü kaydetme
el.image.save_image(iyilestirilmis_resim, 'sonuc.jpg')

# Not: Tüm fonksiyonlar hem dosya yolları hem de NumPy dizileri ile çalışabilir
# Ayrıca tüm fonksiyonlarda işlem sonucunu dosyaya kaydetmek için opsiyonel
# output_path parametresi kullanılabilir
```

### Görüntü İşleme Çoklu İşlem Örneği

```python
from elan import elan

el = elan()

# Adım adım görüntü işleme
resim_yolu = "ornek_resim.jpg"

# 1. Görüntüyü yükle ve boyutlandır
resim = el.image.resize(resim_yolu, 800, 600, keep_aspect_ratio=True)

# 2. Parlaklık ve kontrast ayarla
resim = el.image.adjust_brightness(resim, factor=1.2)  # Biraz daha parlak
resim = el.image.adjust_contrast(resim, factor=1.1)    # Biraz daha kontrastlı

# 3. Görüntüye hafif bulanıklık ekle (gürültüyü azaltmak için)
resim = el.image.add_blur(resim, blur_type='gaussian', kernel_size=3)

# 4. Histogram eşitleme ile detayları iyileştir
resim = el.image.equalize_histogram(resim)

# 5. Yüzleri tespit et ve dikdörtgen ile işaretle
resim, yuzler = el.image.detect_faces(resim, draw_rectangles=True)

# 6. Tespit sonucunu metin olarak ekle
if len(yuzler) > 0:
    metin = f"{len(yuzler)} yüz tespit edildi"
    resim = el.image.add_text(resim, metin, position=(20, 30), 
                             font_size=0.8, color=(0, 255, 0), thickness=2)

# 7. Sonuç görüntüsünü kaydet
el.image.save_image(resim, "islenmiş_resim.jpg")

print("Görüntü işleme tamamlandı!")
```

### Görüntü Filtreleri ve Efektler Örneği

```python
from elan import elan
import os

el = elan()

# Orjinal görüntü üzerinde farklı filtreler uygulama
resim_yolu = "ornek_resim.jpg"
sonuc_klasoru = "filtre_sonuclari"

# Sonuç klasörünü oluştur
os.makedirs(sonuc_klasoru, exist_ok=True)

# Tüm filtre tiplerini uygula
filtreler = ['sepia', 'negative', 'sketch', 'cartoon']

for filtre in filtreler:
    sonuc_yolu = os.path.join(sonuc_klasoru, f"{filtre}_resim.jpg")
    el.image.apply_filter(resim_yolu, filter_type=filtre, output_path=sonuc_yolu)
    print(f"{filtre} filtresi uygulandı: {sonuc_yolu}")

# Kenar tespiti
kenar_yolu = os.path.join(sonuc_klasoru, "kenarlar.jpg")
el.image.detect_edges(resim_yolu, method='canny', 
                     threshold1=100, threshold2=200, 
                     output_path=kenar_yolu)
print(f"Kenar tespiti tamamlandı: {kenar_yolu}")

# Farklı bulanıklık tipleri
bulaniklik_tipleri = ['gaussian', 'median', 'box']
for tip in bulaniklik_tipleri:
    bulanik_yolu = os.path.join(sonuc_klasoru, f"{tip}_bulanik.jpg")
    el.image.add_blur(resim_yolu, blur_type=tip, kernel_size=9, output_path=bulanik_yolu)
    print(f"{tip} bulanıklık uygulandı: {bulanik_yolu}")

print("Tüm filtreler ve efektler uygulandı!")
```

### Video İşleme İşlevleri

`video` modülü, kapsamlı video işleme özellikleri sunar. Bu modül OpenCV'yi arka planda kullanır ancak kullanıcının doğrudan OpenCV ile ilgilenmesine gerek kalmaz:

```python
from elan import elan

el = elan()

# Video hakkında bilgi alma
video_bilgisi = el.video.get_video_info("ornek_video.mp4")
print(f"Video çözünürlüğü: {video_bilgisi['width']}x{video_bilgisi['height']}")
print(f"FPS: {video_bilgisi['fps']}")
print(f"Toplam süre: {video_bilgisi['duration_formatted']}")

# Videodan belirli aralıklarla kare çıkarma
kareler = el.video.extract_frames(
    "ornek_video.mp4",
    output_dir="kareler",
    frame_interval=30,  # Her 30 karede bir kare çıkar
    max_frames=10       # En fazla 10 kare çıkar
)
print(f"{len(kareler)} kare çıkarıldı")

# Karelerden video oluşturma
el.video.create_video_from_frames(
    "kareler",
    "yeni_video.mp4",
    fps=30.0
)

# Videoyu farklı formata dönüştürme
el.video.convert_video(
    "ornek_video.mp4",
    "donusturulmus_video.mp4",
    codec="mp4v",
    resize=(640, 480)
)

# Video kırpma (belirli bir zaman aralığını alma)
el.video.trim_video(
    "ornek_video.mp4",
    "kirpilmis_video.mp4",
    start_time=10.5,    # 10.5 saniyeden başla
    end_time=20.0       # 20. saniyede bitir
)

# Videoya filtre uygulama
el.video.apply_filter_to_video(
    "ornek_video.mp4",
    "gri_video.mp4",
    filter_type="grayscale"  # Gri tonlama filtresi
)

# Videoya sepya filtresi uygulama
el.video.apply_filter_to_video(
    "ornek_video.mp4",
    "sepya_video.mp4",
    filter_type="sepia"
)

# Videoya bulanıklık filtresi uygulama
el.video.apply_filter_to_video(
    "ornek_video.mp4",
    "bulanik_video.mp4",
    filter_type="blur",
    kernel_size=15,
    blur_type="gaussian"
)

# Videoda hareket algılama
hareket_bilgileri = el.video.detect_motion(
    "ornek_video.mp4",
    "hareket_algilama.mp4",  # Hareketlerin belirtildiği çıktı videosu
    sensitivity=25.0,
    min_area=500
)

for hareket in hareket_bilgileri:
    print(f"Hareket algılandı: {hareket['timestamp_formatted']}")

# Videoya metin ekleme
el.video.add_text_to_video(
    "ornek_video.mp4",
    "metin_video.mp4",
    text="Elan Video İşleme",
    position=(50, 50),
    font_scale=1.0,
    color=(0, 255, 0),  # Yeşil
    thickness=2
)

# Video hızını değiştirme
el.video.speed_change(
    "ornek_video.mp4",
    "hizli_video.mp4",
    speed_factor=2.0  # 2 kat hızlı
)
el.video.speed_change(
    "ornek_video.mp4",
    "yavas_video.mp4",
    speed_factor=0.5  # 2 kat yavaş
)

# Birden fazla videoyu birleştirme
el.video.combine_videos(
    ["video1.mp4", "video2.mp4", "video3.mp4"],
    "birlesik_video.mp4",
    transition_frames=15  # 15 karelik yumuşak geçiş
)

# Videoda yüz algılama
yuz_bilgileri = el.video.detect_faces_in_video(
    "ornek_video.mp4",
    "yuz_algilama.mp4",
    scale_factor=1.1,
    min_neighbors=5,
    min_size=(30, 30),
    rectangle_color=(0, 0, 255)  # Kırmızı dikdörtgenler
)

print(f"Toplam {len(yuz_bilgileri)} karede yüz tespit edildi")
for bilgi in yuz_bilgileri:
    print(f"Kare {bilgi['frame']}: {bilgi['face_count']} yüz tespit edildi")

# Videoda yüz tanıma (face recognition)
# Not: Bu özellik için 'pip install face_recognition' gereklidir
tanima_bilgileri = el.video.recognize_faces_in_video(
    "ornek_video.mp4",
    "bilinen_kisiler",  # Her kişi için bir klasör içeren ana klasör
    "yuz_tanima.mp4",
    tolerance=0.6,  # Eşleşme hassasiyeti (düşük değer = daha kesin eşleşme)
    skip_frames=5    # Her 5 karede bir tanıma yap (performans için)
)

print(f"Toplam {len(tanima_bilgileri)} karede yüz tanıma yapıldı")
for bilgi in tanima_bilgileri:
    for yuz in bilgi['recognized_faces']:
        print(f"Tanınan kişi: {yuz['name']}, güven: {yuz['confidence']:.2f}")
```

### Video İşleme Senaryoları

#### Senaryo 1: Video Düzenleme İşlemi

```python
from elan import elan
import os

el = elan()

# Video düzenleme projesi
kaynak_video = "ham_video.mp4"
sonuc_klasoru = "video_projesi"
os.makedirs(sonuc_klasoru, exist_ok=True)

# 1. Video bilgilerini al
video_bilgisi = el.video.get_video_info(kaynak_video)
print(f"İşlenen video: {video_bilgisi['duration_formatted']} süre, {video_bilgisi['width']}x{video_bilgisi['height']} çözünürlük")

# 2. Videoyu parçalara ayır
bol1 = os.path.join(sonuc_klasoru, "bolum1.mp4")
bol2 = os.path.join(sonuc_klasoru, "bolum2.mp4")
bol3 = os.path.join(sonuc_klasoru, "bolum3.mp4")

# İlk 10 saniye
el.video.trim_video(kaynak_video, bol1, 0, 10)

# 15-25 saniye arası
el.video.trim_video(kaynak_video, bol2, 15, 25)

# 30-40 saniye arası
el.video.trim_video(kaynak_video, bol3, 30, 40)

# 3. Parçalara efekt uygula
efektli_bol1 = os.path.join(sonuc_klasoru, "efekt_bolum1.mp4")
efektli_bol2 = os.path.join(sonuc_klasoru, "efekt_bolum2.mp4")
efektli_bol3 = os.path.join(sonuc_klasoru, "efekt_bolum3.mp4")

# Birinci bölüme gri filtre
el.video.apply_filter_to_video(bol1, efektli_bol1, "grayscale")

# İkinci bölüme sepya filtre
el.video.apply_filter_to_video(bol2, efektli_bol2, "sepia")

# Üçüncü bölüme negatif filtre
el.video.apply_filter_to_video(bol3, efektli_bol3, "negative")

# 4. Efektli parçaları birleştir
sonuc_video = os.path.join(sonuc_klasoru, "sonuc_video.mp4")
el.video.combine_videos(
    [efektli_bol1, efektli_bol2, efektli_bol3],
    sonuc_video,
    transition_frames=10
)

# 5. Son videoya metin ekle
son_video = os.path.join(sonuc_klasoru, "final_video.mp4")
el.video.add_text_to_video(
    sonuc_video,
    son_video,
    text="Elan ile düzenlenmiştir",
    position=(20, 30),
    font_scale=0.8,
    color=(0, 255, 255)  # Sarı
)

print(f"Video düzenleme tamamlandı: {son_video}")
```

#### Senaryo 2: Hareket Algılama ve Zaman Atlamalı Video

```python
from elan import elan
import os
import datetime

el = elan()

# Hareket algılama ve zaman atlamalı video oluşturma
kaynak_video = "guvenlik_kamerasi.mp4"
sonuc_klasoru = "hareket_analizi"
os.makedirs(sonuc_klasoru, exist_ok=True)

# 1. Videoda hareket algılama
hareket_dosyasi = os.path.join(sonuc_klasoru, "hareket_video.mp4")
hareketler = el.video.detect_motion(
    kaynak_video,
    hareket_dosyasi,
    sensitivity=20.0,
    min_area=300
)

print(f"Toplam {len(hareketler)} hareket tespit edildi")

# 2. Hareket olan kısımları ayıkla
hareket_parcalari = []
if hareketler:
    video_bilgisi = el.video.get_video_info(kaynak_video)
    fps = video_bilgisi['fps']
    
    for i, hareket in enumerate(hareketler):
        # Hareket başlangıcından 2 saniye öncesi ve 3 saniye sonrasını al
        baslangic = max(0, hareket['timestamp'] - 2)
        bitis = min(video_bilgisi['duration'], hareket['timestamp'] + 3)
        
        # Bu parçayı video olarak çıkart
        parca_dosya = os.path.join(sonuc_klasoru, f"hareket_{i+1:03d}.mp4")
        el.video.trim_video(kaynak_video, parca_dosya, baslangic, bitis)
        hareket_parcalari.append(parca_dosya)
        
        print(f"Hareket {i+1}: {hareket['timestamp_formatted']} - alan: {hareket['max_area']:.0f} piksel")

# 3. Hareket parçalarını birleştir ve tarih bilgisi ekle
if hareket_parcalari:
    ozet_video = os.path.join(sonuc_klasoru, "ozet_video.mp4")
    el.video.combine_videos(hareket_parcalari, ozet_video, transition_frames=5)
    
    final_video = os.path.join(sonuc_klasoru, "final_hareket_ozeti.mp4")
    tarih = datetime.datetime.now().strftime("%d.%m.%Y")
    el.video.add_text_to_video(
        ozet_video,
        final_video,
        text=f"Hareket Özeti - {tarih}",
        position=(20, 30),
        font_scale=1.0,
        color=(0, 0, 255)  # Kırmızı
    )
    
    print(f"Hareket özet videosu oluşturuldu: {final_video}")
else:
    print("Hareket tespit edilemedi veya dosyalar oluşturulamadı")
```

#### Senaryo 3: Yüz Tanıma ve Takip Sistemi

```python
from elan import elan
import os
import datetime
import shutil

el = elan()

# Yüz tanıma ve takip sistemi
kaynak_video = "toplanti_kaydi.mp4"
sonuc_klasoru = "yuz_takip_sonuclari"
os.makedirs(sonuc_klasoru, exist_ok=True)

# Bilinen kişiler klasörü
bilinen_kisiler = "bilinen_kisiler"
if not os.path.exists(bilinen_kisiler):
    os.makedirs(bilinen_kisiler)
    
    # ÖRNEK: Gerçek uygulamada burası kişilere ait görüntülerle doldurulmalıdır
    # Burada yalnızca klasör yapısını gösteriyoruz
    for kisi in ["Ahmet", "Ayşe", "Mehmet"]:
        os.makedirs(os.path.join(bilinen_kisiler, kisi), exist_ok=True)

# 1. Önce tüm yüzleri tespit et
yuz_algilama_video = os.path.join(sonuc_klasoru, "yuz_algilama.mp4")
tespit_edilen_yuzler = el.video.detect_faces_in_video(
    kaynak_video,
    yuz_algilama_video,
    min_size=(50, 50)  # Daha büyük yüzleri tespit et
)

print(f"Toplam {len(tespit_edilen_yuzler)} karede yüz tespit edildi")

# 2. Tespit edilen yüzleri kullanarak yüz tanıma yap
yuz_tanima_video = os.path.join(sonuc_klasoru, "yuz_tanima.mp4")
tanima_sonuclari = el.video.recognize_faces_in_video(
    kaynak_video,
    bilinen_kisiler,
    yuz_tanima_video,
    tolerance=0.6,
    skip_frames=3  # Performans için her 3 karede bir tanıma yap
)

# 3. Kişi bazlı analiz yap
kisi_istatistikleri = {}

for bilgi in tanima_sonuclari:
    for yuz in bilgi['recognized_faces']:
        kisi = yuz['name']
        if kisi not in kisi_istatistikleri:
            kisi_istatistikleri[kisi] = {
                'ilk_gorunme': bilgi['timestamp'],
                'son_gorunme': bilgi['timestamp'],
                'toplam_sure': 0,
                'gorunme_sayisi': 1,
                'ortalama_guven': yuz['confidence']
            }
        else:
            # Kişi istatistiklerini güncelle
            kisi_istatistikleri[kisi]['son_gorunme'] = bilgi['timestamp']
            kisi_istatistikleri[kisi]['gorunme_sayisi'] += 1
            kisi_istatistikleri[kisi]['ortalama_guven'] += yuz['confidence']

# İstatistikleri hesapla ve rapor oluştur
rapor_dosyasi = os.path.join(sonuc_klasoru, "kisi_raporu.txt")
with open(rapor_dosyasi, 'w', encoding='utf-8') as f:
    f.write(f"Yüz Tanıma Raporu - {datetime.datetime.now().strftime('%d.%m.%Y %H:%M')}\n")
    f.write(f"Kaynak video: {kaynak_video}\n\n")
    
    for kisi, istatistik in kisi_istatistikleri.items():
        # Toplam süreyi hesapla
        toplam_sure = istatistik['son_gorunme'] - istatistik['ilk_gorunme']
        ortalama_guven = istatistik['ortalama_guven'] / istatistik['gorunme_sayisi']
        
        f.write(f"Kişi: {kisi}\n")
        f.write(f"  İlk görünme: {str(datetime.timedelta(seconds=int(istatistik['ilk_gorunme'])))}\n")
        f.write(f"  Son görünme: {str(datetime.timedelta(seconds=int(istatistik['son_gorunme'])))}\n")
        f.write(f"  Toplam süre: {str(datetime.timedelta(seconds=int(toplam_sure)))}\n")
        f.write(f"  Görünme sayısı: {istatistik['gorunme_sayisi']}\n")
        f.write(f"  Ortalama güven: {ortalama_guven:.2f}\n\n")

print(f"Kişi raporu oluşturuldu: {rapor_dosyasi}")

# 4. Sonuç videosu oluştur
print(f"Yüz algılama sonuç videosu: {yuz_algilama_video}")
print(f"Yüz tanıma sonuç videosu: {yuz_tanima_video}")
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

### Test Görüntü İşleme Aracı Kullanımı

Elan kütüphanesinin görüntü işleme özelliklerini test etmek için `test_image_processing.py` aracını kullanabilirsiniz:

```bash
python test_image_processing.py resim.jpg
```

Bu komut, belirtilen görüntü dosyası üzerinde çeşitli görüntü işleme tekniklerini uygular ve sonuçları `sonuclar` klasörüne kaydeder:

- Gri tonlama dönüşümü
- Kenar algılama
- Bulanıklaştırma
- Karikatür efekti
- Sepya efekti
- 45 derece döndürme
- Yeniden boyutlandırma (800x600)

Tüm sonuçlar program tarafından otomatik olarak oluşturulan `sonuclar` klasörüne kaydedilir, böylece orijinal görüntünüz değişmeden kalır.

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

### Yüz Algılama ve Tanıma

Elan kütüphanesi, görüntülerdeki yüzleri otomatik olarak algılayıp işaretleyebilir ve tanıyabilir. Üç farklı yüz algılama yöntemi sunar: OpenCV (hızlı), DLIB (doğru) ve MediaPipe (modern ve hassas).

#### 1. Yüz Algılama

```python
from elan import elan

el = elan()

# 1. OpenCV ile yüz algılama (hızlı ama daha az doğru)
image_opencv, faces_opencv = el.image.detect_faces(
    "fotograf.jpg",
    method='opencv',  # Varsayılan
    rectangle_color=(0, 0, 255),  # Kırmızı dikdörtgenler
    rectangle_thickness=2,
    scale_factor=1.1,
    min_neighbors=4, 
    min_size=(30, 30)
)
print(f"OpenCV ile tespit edilen yüz sayısı: {len(faces_opencv)}")

# 2. DLIB (face_recognition) ile yüz algılama (daha doğru)
image_dlib, faces_dlib = el.image.detect_faces(
    "fotograf.jpg",
    method='dlib',  # face_recognition kütüphanesini kullanır
    rectangle_color=(0, 255, 0)  # Yeşil dikdörtgenler
)
print(f"DLIB ile tespit edilen yüz sayısı: {len(faces_dlib)}")

# 3. MediaPipe ile yüz algılama (en modern ve hassas)
image_mp, faces_mp = el.image.detect_faces(
    "fotograf.jpg",
    method='mediapipe',  # Google'ın MediaPipe kütüphanesini kullanır
    rectangle_color=(255, 0, 0),  # Mavi dikdörtgenler
    draw_landmarks=True  # Yüz hatlarını da çizer
)
print(f"MediaPipe ile tespit edilen yüz sayısı: {len(faces_mp)}")

# Her birini dosyaya kaydetme
el.image.save_image(image_opencv, "opencv_yuzler.jpg")
el.image.save_image(image_dlib, "dlib_yuzler.jpg")
el.image.save_image(image_mp, "mediapipe_yuzler.jpg")
```

#### 2. Yüz Tanıma

```python
from elan import elan

el = elan()

# Yüz tanıma (face_recognition kütüphanesini kullanır)
# Bilinen kişiler klasöründe her kişi için ayrı klasör olmalıdır:
# bilinen_kisiler/
#   ├── Ahmet/
#   │   ├── resim1.jpg
#   │   └── resim2.jpg
#   ├── Ayşe/
#   │   ├── resim1.jpg
#   └── Mehmet/
#       └── resim1.jpg

image_with_names, recognition_results = el.image.recognize_faces(
    "grup_fotografi.jpg",
    known_faces_dir="bilinen_kisiler",
    tolerance=0.6,  # Eşleşme eşiği (düşük = daha kesin eşleşme)
    draw_labels=True,  # İsim etiketleri çiz
    label_color=(0, 255, 0)  # Yeşil etiketler
)

# Tanıma sonuçlarını göster
for result in recognition_results:
    name = result['name']
    confidence = result['confidence']
    x, y, w, h = result['location']
    
    print(f"Kişi: {name}, Güven: {confidence:.2f}, Konum: ({x},{y},{w},{h})")

# Sonucu kaydet
el.image.save_image(image_with_names, "taninmis_yuzler.jpg")
```

#### Farklı Yüz Algılama Yöntemlerinin Karşılaştırması

| Yöntem | Doğruluk | Hız | Kurulum | Özel Özellikler |
|--------|----------|-----|---------|----------------|
| OpenCV | Orta | Hızlı | Otomatik | Basit, hafif |
| DLIB | Yüksek | Orta | `pip install face_recognition` | Yüz tanıma yeteneği |
| MediaPipe | Çok Yüksek | Orta-Hızlı | `pip install mediapipe` | Yüz hatları tespiti |

#### Yüz Algılama Test Aracı

Farklı yüz algılama yöntemlerini test etmek için `test_face_detection.py` aracını kullanabilirsiniz:

```bash
python test_face_detection.py fotograf.jpg
```

Bu komut, belirtilen görüntü üzerinde üç farklı algılama yöntemiyle yüz algılama yapar ve sonuçları `face_detection_results` klasörüne kaydeder:

1. OpenCV ile yüz algılama
2. DLIB (face_recognition) ile yüz algılama
3. MediaPipe ile yüz algılama
4. MediaPipe ile yüz hatları (landmarks) tespiti

#### Yüz Algılama İpuçları

- Daha iyi sonuçlar için iyi aydınlatılmış görüntüler kullanın
- Yüzler kameraya dönük olmalı
- Doğruluk önemliyse MediaPipe veya DLIB yöntemlerini kullanın
- Hız önemliyse OpenCV yöntemini kullanın
- MediaPipe, yüz hatlarını da tespit edebilir
- Yüz tanıma için reference görüntülerinde net yüz fotoğrafları kullanın
- `tolerance` parametresi ile eşleşme hassasiyetini ayarlayabilirsiniz (0.4-0.6 önerilir)

#### Kurulum Gereksinimleri

Yüz algılama ve tanıma özelliklerini tam olarak kullanabilmek için şu paketleri kurmalısınız:

```bash
# OpenCV otomatik olarak Elan ile kurulur
# DLIB tabanlı yüz algılama ve tanıma için
pip install face_recognition
# MediaPipe ile gelişmiş yüz algılama için
pip install mediapipe
```

## Gelişmiş Kullanım

### Modüler Yapı Kullanımı

Elan kütüphanesi modüler yapısı sayesinde, sadece ihtiyacınız olan bileşenleri kurmanıza olanak tanır. 
Örnek kullanım:

```python
import elan

# Temel özellikleri kullan
sonuc = elan.math.add(5, 3)
metin = elan.string.reverse("Merhaba")

# Görüntü işleme özellikleri - elan[image] kurulumu gerektirir
try:
    goruntu = elan.image.load("foto.jpg")
    gri_tonlu = elan.image.to_grayscale(goruntu)
    elan.image.save_image(gri_tonlu, "gri_foto.jpg")
except ImportError:
    print("Görüntü işleme için: pip install elan[image]")

# Yüz algılama özellikleri - elan[face] kurulumu gerektirir
try:
    goruntu, yuzler = elan.image.detect_faces("foto.jpg")
    print(f"{len(yuzler)} yüz bulundu!")
    elan.image.save_image(goruntu, "yuz_algilama_sonuc.jpg")
except ImportError:
    print("Yüz algılama için: pip install elan[face]")
```