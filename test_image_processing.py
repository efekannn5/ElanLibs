from elan import elan
import os
import sys
import time
import cv2

# Giriş kontrolü
if len(sys.argv) < 2:
    print("Hata: Görüntü dosyası belirtilmedi!")
    print("Kullanım: python test_image_processing.py <görüntü_dosyası>")
    sys.exit(1)

# Görüntü dosyasını al
input_image_path = sys.argv[1]

# Dosyanın varlığını kontrol et
if not os.path.exists(input_image_path):
    print(f"Hata: Görüntü dosyası bulunamadı: {input_image_path}")
    sys.exit(1)

# Sonuçlar için klasör oluştur
results_dir = "sonuclar"
if not os.path.exists(results_dir):
    os.makedirs(results_dir)

# Elan kütüphanesini başlat
el = elan()

print(f"\n{input_image_path} dosyası üzerinde işlemler yapılıyor...")
print("=" * 50)

# İşlem başlangıç zamanı
start_time = time.time()

# 1. Gri Tonlama
print("1. Gri tonlamaya dönüştürülüyor...")
gray_img = el.image.to_grayscale(input_image_path)
gray_output = os.path.join(results_dir, "gri_tonlama.jpg")
el.image.save_image(gray_img, gray_output)

# 2. Kenar Algılama
print("2. Kenarlar algılanıyor...")
edges_img = el.image.detect_edges(input_image_path, method='canny')
edges_output = os.path.join(results_dir, "kenarlar.jpg")
el.image.save_image(edges_img, edges_output)

# 3. Bulanıklaştırma
print("3. Bulanıklaştırma uygulanıyor...")
blurred_img = el.image.add_blur(input_image_path, blur_type='gaussian', kernel_size=11)
blurred_output = os.path.join(results_dir, "bulanık.jpg")
el.image.save_image(blurred_img, blurred_output)

# 4. Karikatür Efekti
print("4. Karikatür efekti uygulanıyor...")
cartoon_img = el.image.apply_filter(input_image_path, filter_type='cartoon')
cartoon_output = os.path.join(results_dir, "karikatür.jpg")
el.image.save_image(cartoon_img, cartoon_output)

# 5. Sepya Efekti
print("5. Sepya efekti uygulanıyor...")
sepia_img = el.image.apply_filter(input_image_path, filter_type='sepia')
sepia_output = os.path.join(results_dir, "sepya.jpg")
el.image.save_image(sepia_img, sepia_output)

# 6. Döndürme
print("6. 45 derece döndürülüyor...")
rotated_img = el.image.rotate(input_image_path, angle=45)
rotated_output = os.path.join(results_dir, "döndürülmüş.jpg")
el.image.save_image(rotated_img, rotated_output)

# 7. Boyut Değiştirme
print("7. Boyut değiştiriliyor...")
resized_img = el.image.resize(input_image_path, width=800, height=600)
resized_output = os.path.join(results_dir, "yeniden_boyutlandırılmış.jpg")
el.image.save_image(resized_img, resized_output)

# İşlem süresini hesapla
duration = time.time() - start_time

print("\nİşlemler tamamlandı!")
print(f"Toplam süre: {duration:.2f} saniye")
print(f"Sonuçlar '{results_dir}' klasöründe kaydedildi.")
print("\nOluşturulan dosyalar:")
for file in sorted(os.listdir(results_dir)):
    print(f" - {file}") 