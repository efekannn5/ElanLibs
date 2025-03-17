from elan import elan
import os
import sys
import cv2
import time

print("Elan Yüz Algılama - Test")
print("=" * 50)

# Komut satırı argümanını kontrol et (test için kullanılacak görüntü)
if len(sys.argv) < 2:
    print("Hata: Görüntü dosyası belirtilmedi!")
    print("Kullanım: python test_face_detection.py <görüntü_dosyası>")
    sys.exit(1)

# Görüntü dosyasını al
image_path = sys.argv[1]

# Dosyanın varlığını kontrol et
if not os.path.exists(image_path):
    print(f"Hata: Görüntü dosyası bulunamadı: {image_path}")
    sys.exit(1)

# Sonuçlar için klasör oluştur
results_dir = "face_detection_results"
if not os.path.exists(results_dir):
    os.makedirs(results_dir)

# Elan kütüphanesini başlat
el = elan()

print(f"\n'{image_path}' üzerinde yüz algılama yapılıyor...")

# İşlem başlangıç zamanı
start_time = time.time()

# 1. Varsayılan parametrelerle yüz algılama
print("1. Varsayılan ayarlarla yüz algılama...")
image_with_faces, faces = el.image.detect_faces(image_path)
default_output = os.path.join(results_dir, "yuzler_varsayilan.jpg")
el.image.save_image(image_with_faces, default_output)
print(f"   {len(faces)} yüz tespit edildi")

# 2. Kırmızı dikdörtgenlerle yüz algılama
print("2. Kırmızı dikdörtgenlerle yüz algılama...")
image_red, faces = el.image.detect_faces(
    image_path, 
    rectangle_color=(0, 0, 255),  # Kırmızı (BGR formatında)
    rectangle_thickness=2
)
red_output = os.path.join(results_dir, "yuzler_kirmizi.jpg")
el.image.save_image(image_red, red_output)

# 3. Yeşil dikdörtgenlerle ve daha kalın çizgilerle yüz algılama
print("3. Yeşil ve kalın dikdörtgenlerle yüz algılama...")
image_green, faces = el.image.detect_faces(
    image_path, 
    rectangle_color=(0, 255, 0),  # Yeşil (BGR formatında)
    rectangle_thickness=3
)
green_output = os.path.join(results_dir, "yuzler_yesil_kalin.jpg")
el.image.save_image(image_green, green_output)

# 4. Daha hassas algılama (daha az yanlış pozitif)
print("4. Daha hassas yüz algılama ayarları...")
image_precise, faces_precise = el.image.detect_faces(
    image_path, 
    scale_factor=1.05,  # Daha küçük scale factor = daha hassas algılama
    min_neighbors=6,    # Daha yüksek min_neighbors = daha az yanlış pozitif
    min_size=(50, 50)   # Daha büyük minimum yüz boyutu
)
precise_output = os.path.join(results_dir, "yuzler_hassas.jpg")
el.image.save_image(image_precise, precise_output)
print(f"   Hassas ayarlarla {len(faces_precise)} yüz tespit edildi")

# İşlem süresini hesapla
duration = time.time() - start_time

print("\nYüz algılama işlemi tamamlandı!")
print(f"Toplam süre: {duration:.2f} saniye")
print(f"Sonuçlar '{results_dir}' klasöründe kaydedildi.")
print("\nOluşturulan dosyalar:")
for file in sorted(os.listdir(results_dir)):
    print(f" - {file}")

print("\nKullanım: Bu test, görüntüdeki yüzleri algılar ve işaretler.")
print("Daha iyi sonuçlar için:")
print(" - İyi aydınlatılmış görüntüler kullanın")
print(" - Yüzler kameraya dönük olmalı")
print(" - scale_factor değerini düşürerek (örn. 1.05) daha hassas algılama yapabilirsiniz")
print(" - min_neighbors değerini artırarak (örn. 6-8) yanlış pozitifleri azaltabilirsiniz") 