from elan import elan
import os
import time
import numpy as np

# Elan sınıfını başlat
el = elan()

print("Elan Görüntü İşleme Modülü - Test")
print("=" * 50)

# Test başlangıç zamanı
start_time = time.time()

# Test için örnek görüntü oluştur (siyah kare, beyaz dikdörtgen ile)
test_image = np.zeros((300, 400, 3), dtype=np.uint8)
test_image[100:200, 150:250] = 255  # Beyaz dikdörtgen ekle
test_image_path = "test_image.jpg"
el.image.save_image(test_image, test_image_path)
print(f"Test için örnek görüntü oluşturuldu: {test_image_path}")

# Fonksiyonları test et
print("\n1. Temel İşlemler Testi:")

try:
    # Gri tonlama testi
    gray_img = el.image.to_grayscale(test_image)
    el.image.save_image(gray_img, "test_gray.jpg")
    print("✓ Gri tonlama dönüştürme başarılı")
except Exception as e:
    print(f"✗ Gri tonlama hatası: {e}")

try:
    # Yeniden boyutlandırma testi
    resized_img = el.image.resize(test_image, 200, 150)
    el.image.save_image(resized_img, "test_resized.jpg")
    print("✓ Yeniden boyutlandırma başarılı")
except Exception as e:
    print(f"✗ Yeniden boyutlandırma hatası: {e}")

try:
    # Döndürme testi
    rotated_img = el.image.rotate(test_image, 45)
    el.image.save_image(rotated_img, "test_rotated.jpg")
    print("✓ Döndürme başarılı")
except Exception as e:
    print(f"✗ Döndürme hatası: {e}")

try:
    # Kırpma testi
    cropped_img = el.image.crop(test_image, 150, 100, 100, 100)
    el.image.save_image(cropped_img, "test_cropped.jpg")
    print("✓ Kırpma başarılı")
except Exception as e:
    print(f"✗ Kırpma hatası: {e}")

print("\n2. Filtre ve Efekt Testi:")

try:
    # Bulanıklaştırma testi
    blurred_img = el.image.add_blur(test_image, blur_type='gaussian', kernel_size=15)
    el.image.save_image(blurred_img, "test_blurred.jpg")
    print("✓ Bulanıklaştırma başarılı")
except Exception as e:
    print(f"✗ Bulanıklaştırma hatası: {e}")

try:
    # Kenar algılama testi
    edges_img = el.image.detect_edges(test_image, method='canny')
    el.image.save_image(edges_img, "test_edges.jpg")
    print("✓ Kenar algılama başarılı")
except Exception as e:
    print(f"✗ Kenar algılama hatası: {e}")

try:
    # Parlaklık ayarlama testi
    bright_img = el.image.adjust_brightness(test_image, 1.5)
    el.image.save_image(bright_img, "test_brightness.jpg")
    print("✓ Parlaklık ayarlama başarılı")
except Exception as e:
    print(f"✗ Parlaklık ayarlama hatası: {e}")

try:
    # Kontrast ayarlama testi
    contrast_img = el.image.adjust_contrast(test_image, 2.0)
    el.image.save_image(contrast_img, "test_contrast.jpg")
    print("✓ Kontrast ayarlama başarılı")
except Exception as e:
    print(f"✗ Kontrast ayarlama hatası: {e}")

try:
    # Histogram eşitleme testi
    equalized_img = el.image.equalize_histogram(test_image)
    el.image.save_image(equalized_img, "test_equalized.jpg")
    print("✓ Histogram eşitleme başarılı")
except Exception as e:
    print(f"✗ Histogram eşitleme hatası: {e}")

print("\n3. Çizim ve Metin Testi:")

try:
    # Metin ekleme testi
    text_img = el.image.add_text(test_image, "Elan Test", (50, 50), font_size=1.5, color=(0, 0, 255))
    el.image.save_image(text_img, "test_text.jpg")
    print("✓ Metin ekleme başarılı")
except Exception as e:
    print(f"✗ Metin ekleme hatası: {e}")

try:
    # Dikdörtgen çizme testi
    rect_img = el.image.add_rectangle(test_image, (50, 50), (350, 250), color=(0, 255, 0), thickness=2)
    el.image.save_image(rect_img, "test_rectangle.jpg")
    print("✓ Dikdörtgen çizme başarılı")
except Exception as e:
    print(f"✗ Dikdörtgen çizme hatası: {e}")

# Test sonuçlarını özetle
test_duration = time.time() - start_time
print(f"\nTest Tamamlandı - Süre: {test_duration:.2f} saniye")
print("Test sonuçları ve oluşturulan görüntüler şu dizinde bulunabilir:", os.getcwd())

# Test görüntüsünü temizle (isteğe bağlı)
# os.remove(test_image_path) 