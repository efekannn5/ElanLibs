# ElanLibs

**`Efekan Nefesoğlu` ve `Elanur Tuana İşcen` Tarafından Geliştirilmiştir**

## Giriş
Elan, yaygın programlama görevlerini basitleştirmek için tasarlanmış çok yönlü bir Python kütüphanesidir. Matematiksel işlemler, liste manipülasyonları, string işleme ve temel görüntü işleme için yardımcı işlevler sağlar. Kütüphane, projelerinize kolayca entegre edilebilecek şekilde tasarlanmıştır, böylece tekerleği yeniden icat etmek yerine özellikler oluşturmaya odaklanabilirsiniz.

## Amaç
Elan'ın amacı, çeşitli projelere kolayca entegre edilebilecek yeniden kullanılabilir işlevler koleksiyonu sunarak geliştirme süresini ve çabasını azaltmaktır.

## Kurulum
Elan'ı kurmak için, depoyu klonlayın ve `ElanLibs` dizinini projenize dahil edin. Gerekli bağımlılıkların yüklü olduğundan emin olun.

### Bağımlılıklar
- Python 3.x
- OpenCV (görüntü işleme için)

```bash
$ pip install opencv-python
```

### Depoyu Klonlayın
```bash
$ git clone <repository-url>
```

## Kullanım

### Matematiksel İşlevler
`math_utils` sınıfı çeşitli matematiksel işlemler sağlar:

- `add(a, b)`: `a` ve `b` toplamını döndürür.
- `subtract(a, b)`: `a` ve `b` farkını döndürür.
- `multiply(a, b)`: `a` ve `b` çarpımını döndürür.
- `divide(a, b)`: `a`'nın `b`'ye bölümünü döndürür.
- `power(a, b)`: `a`'nın `b` kuvvetini döndürür.
- `square_root(a)`: `a`'nın karekökünü döndürür.
- `cube_root(a)`: `a`'nın küpkökünü döndürür.
- `square(a)`: `a`'nın karesini döndürür.
- `cube(a)`: `a`'nın küpünü döndürür.
- `factorial(n)`: `n` faktöriyelini döndürür.

### Liste İşlevleri
`list_utils` sınıfı liste manipülasyonları için işlevler sağlar:

- `reverse(list)`: Ters çevrilmiş listeyi döndürür.
- `sort(list)`: Listenin sıralanmış bir versiyonunu döndürür.
- `unique(list)`: Benzersiz elemanlardan oluşan bir liste döndürür.

### String İşlevleri
`string_utils` sınıfı çeşitli string manipülasyon işlevleri sunar:

- `reverse(string)`: Ters çevrilmiş stringi döndürür.
- `capitalize(string)`: Stringin ilk karakterini büyük harf yapar.
- `uppercase(string)`: Stringi büyük harfe çevirir.
- `lowercase(string)`: Stringi küçük harfe çevirir.
- `title(string)`: Stringi başlık biçimine çevirir.
- `swapcase(string)`: Stringdeki her karakterin harf durumunu değiştirir.
- `reverse_words(string)`: Stringdeki her kelimeyi ters çevirir.

### Görüntü İşleme İşlevleri
`image_utils` sınıfı temel görüntü işleme işlevleri sağlar:

- `to_grayscale(image_path)`: Belirtilen yoldaki görüntüyü gri tonlamaya çevirir.
- `resize(image_path, width, height)`: Görüntüyü belirtilen genişlik ve yükseklikte yeniden boyutlandırır.
- `rotate(image_path, angle)`: Görüntüyü belirtilen açı kadar döndürür.

## Örnek
Elan kütüphanesinin nasıl kullanılacağına dair hızlı bir örnek:

```python
from ElanLibs.main import main

# Ana sınıfı başlat
elan = main()

# Matematiksel işlemler
print(elan.math.add(5, 3))  # Çıktı: 8
print(elan.math.factorial(5))  # Çıktı: 120

# Liste işlemleri
print(elan.list.reverse([1, 2, 3]))  # Çıktı: [3, 2, 1]
print(elan.list.unique([1, 2, 2, 3]))  # Çıktı: [1, 2, 3]

# String işlemleri
print(elan.string.reverse("Hello"))  # Çıktı: "olleH"
print(elan.string.reverse_words("Hello World"))  # Çıktı: "olleH dlroW"

# Görüntü işlemleri
# Not: Bu işlevler görüntü nesneleri döndürür, bu nesneler OpenCV işlevleri kullanılarak kaydedilebilir veya görüntülenebilir.
gray_image = elan.image.to_grayscale('path/to/image.jpg')
resized_image = elan.image.resize('path/to/image.jpg', 100, 100)
rotated_image = elan.image.rotate('path/to/image.jpg', 90)
```

## Katkı Rehberi
Katkılar memnuniyetle karşılanır! Herhangi bir iyileştirme veya hata düzeltmesi için lütfen depoyu çatallayın ve bir çekme isteği gönderin. Kodunuzun projenin kodlama standartlarına uygun olduğundan ve uygun testler içerdiğinden emin olun.

## SSS
**S: Hangi Python sürümü gereklidir?**
C: Elan, Python 3.x gerektirir.

**S: Gerekli bağımlılıkları nasıl yüklerim?**
C: Görüntü işleme için OpenCV'yi yüklemek için `pip install opencv-python` kullanın.

**S: Elan'ı ticari projelerde kullanabilir miyim?**
C: Evet, Elan, ticari kullanım için izin veren MIT Lisansı altında lisanslanmıştır.

## Lisans
Bu proje MIT Lisansı altında lisanslanmıştır. Detaylar için LICENSE dosyasına bakın.

## İletişim
Herhangi bir soru veya öneri için lütfen Efekan Nefesoğlu ile iletişime geçin.


