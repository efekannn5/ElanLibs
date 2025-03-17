# ELAN KÜTÜPHANESİ KURULUM TALİMATLARI

## Kurulum Seçenekleri

Elan kütüphanesi modüler bir yapıya sahiptir. İhtiyacınıza göre farklı özellikleri kurabilirsiniz:

### 1. Temel Kurulum

Sadece temel özellikleri (matematik, string, liste işlemleri) içeren temel kurulum için:

```
pip install elan
```

### 2. Görüntü İşleme Özellikleri

Temel özelliklere ek olarak görüntü işleme (OpenCV) için:

```
pip install "elan[image]"
```

**NOT**: Windows PowerShell kullanıyorsanız, tırnak içine almanız gerekebilir:

```
pip install "elan[image]"
```

Windows cmd kullanıyorsanız:

```
pip install elan[image]
```

### 3. Yüz Algılama ve Tanıma Özellikleri

Temel özellikler, görüntü işleme ve yüz algılama/tanıma için:

```
pip install "elan[face]"
```

**NOT**: Windows PowerShell kullanıyorsanız, tırnak içine almanız gerekebilir:

```
pip install "elan[face]"
```

Windows cmd kullanıyorsanız:

```
pip install elan[face]
```

### 4. Tüm Özellikler

Kütüphanenin tüm özelliklerini içeren tam kurulum için:

```
pip install "elan[all]"
```

**NOT**: Windows PowerShell kullanıyorsanız, tırnak içine almanız gerekebilir:

```
pip install "elan[all]"
```

Windows cmd kullanıyorsanız:

```
pip install elan[all]
```

## Windows'ta DLIB Kurulum Sorunları İçin Çözümler

Windows'ta dlib kurulumunda sorun yaşıyorsanız aşağıdaki çözümleri deneyebilirsiniz:

### Yöntem 1: Önceden Derlenmiş Wheel Kullanımı (Önerilen)

```
# Python 3.10 için (64-bit)
pip install https://github.com/jloh02/dlib/releases/download/v19.22/dlib-19.22.99-cp310-cp310-win_amd64.whl

# Ardından face_recognition ve elan yüklenir
pip install face_recognition
pip install "elan[face]"
```

### Yöntem 2: Manuel Derleme

1. [CMake](https://cmake.org/download/) indirin ve kurun
2. [Visual Studio Community](https://visualstudio.microsoft.com/downloads/) (C++ geliştirme araçlarını seçin) indirin ve kurun
3. Daha sonra terminalde: `pip install dlib`
4. Ardından: `pip install face_recognition`
5. Son olarak: `pip install "elan[face]"`

## Kurulum Doğrulama

Kurulumu doğrulamak için:

```python
# Python konsolunda:
import elan
from elan import kurulum_bilgisi

# Kurulum bilgilerini göster
kurulum_bilgisi()
```

## Sorun Giderme

### Birkaç Yaygın Sorun ve Çözümleri

1. **ModuleNotFoundError: No module named 'elan'**
   - Çözüm: `pip install elan` ile temel kurulumu yapın

2. **ModuleNotFoundError: No module named 'cv2'**
   - Çözüm: `pip install "elan[image]"` komutunu kullanın

3. **ModuleNotFoundError: No module named 'dlib'**
   - Çözüm: Yukarıdaki Windows kurulum talimatlarını izleyin veya `pip install "elan[face]"` komutunu kullanın

4. **SyntaxError: invalid syntax when using [image] or [face]**
   - Çözüm: Köşeli parantezleri tırnak içine alın: `pip install "elan[image]"`

5. **pip: error: invalid command 'elan[image]'**
   - Çözüm: Doğru sözdizimi: `pip install "elan[image]"` (tırnak işaretleri dahil)

### Daha Fazla Yardım

Daha fazla yardım için GitHub: [https://github.com/efekannn5/ElanLibs](https://github.com/efekannn5/ElanLibs) 