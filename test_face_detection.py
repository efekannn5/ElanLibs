from elan import elan
import os
import sys
import cv2
import time

print("Elan Gelişmiş Yüz Algılama - Test")
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
try:
    el = elan()
except Exception as e:
    print(f"Elan kütüphanesi başlatılırken hata oluştu: {e}")
    sys.exit(1)

print(f"\n'{image_path}' üzerinde yüz algılama yapılıyor...")

# İşlem başlangıç zamanı
start_time = time.time()

# MediaPipe ile Yüz Algılama (varsayılan ve en iyi yöntem)
print("\n1. MediaPipe ile Yüz Algılama (önerilen yöntem)")
try:
    # MediaPipe varsayılan
    print("   MediaPipe yüz algılama çalıştırılıyor...")
    image_mp, faces_mp = el.image.detect_faces(
        image_path, 
        method='mediapipe',
        rectangle_color=(255, 0, 0)  # Mavi
    )
    mp_output = os.path.join(results_dir, "mediapipe_yuz_algilama.jpg")
    el.image.save_image(image_mp, mp_output)
    print(f"   {len(faces_mp)} yüz tespit edildi")
    
    # MediaPipe yüz hatları
    print("   MediaPipe yüz hatları ekleniyor...")
    image_mp_landmarks, _ = el.image.detect_faces(
        image_path, 
        method='mediapipe',
        rectangle_color=(255, 0, 255),  # Mor
        draw_landmarks=True
    )
    mp_landmarks_output = os.path.join(results_dir, "mediapipe_yuz_hatlari.jpg")
    el.image.save_image(image_mp_landmarks, mp_landmarks_output)
    
    print("   MediaPipe ile yüz algılama başarıyla tamamlandı!")
except Exception as e:
    print(f"   MediaPipe ile yüz algılama başarısız: {e}")

# Alternatif yöntemler (sadece MediaPipe başarısız olduysa veya karşılaştırma için kullanın)
print("\n2. Alternatif Yüz Algılama Yöntemleri")

# DLIB/face_recognition ile yüz algılama
print("   DLIB/face_recognition ile yüz algılama deneniyor...")
try:
    image_dlib, faces_dlib = el.image.detect_faces(
        image_path, 
        method='dlib',
        rectangle_color=(0, 255, 0)  # Yeşil
    )
    dlib_output = os.path.join(results_dir, "dlib_yuz_algilama.jpg")
    el.image.save_image(image_dlib, dlib_output)
    print(f"   {len(faces_dlib)} yüz tespit edildi")
except Exception as e:
    print(f"   DLIB ile yüz algılama başarısız oldu: {e}")

# OpenCV ile yüz algılama
print("   OpenCV ile yüz algılama deneniyor...")
try:
    image_opencv, faces_opencv = el.image.detect_faces(
        image_path, 
        method='opencv',
        rectangle_color=(0, 0, 255)  # Kırmızı
    )
    opencv_output = os.path.join(results_dir, "opencv_yuz_algilama.jpg")
    el.image.save_image(image_opencv, opencv_output)
    print(f"   {len(faces_opencv)} yüz tespit edildi")
except Exception as e:
    print(f"   OpenCV ile yüz algılama başarısız oldu: {e}")

# İşlem süresini hesapla
duration = time.time() - start_time

print("\nYüz algılama testleri tamamlandı!")
print(f"Toplam süre: {duration:.2f} saniye")
print(f"Sonuçlar '{results_dir}' klasörüne kaydedildi.")

print("\nSONUÇLAR:")
try:
    files = os.listdir(results_dir)
    if not files:
        print("   Hiçbir sonuç üretilemedi. Görüntüdeki yüzleri tespit etmek mümkün olmadı.")
    else:
        print(f"   {len(files)} sonuç dosyası oluşturuldu:")
        for file in sorted(os.listdir(results_dir)):
            file_path = os.path.join(results_dir, file)
            file_size = os.path.getsize(file_path) / 1024  # KB cinsinden
            print(f"   - {file} ({file_size:.1f} KB)")
except Exception as e:
    print(f"   Sonuçlar listelenirken hata oluştu: {e}")

print("\nÖNERİLER:")
print("   - MediaPipe en doğru yüz algılama yöntemidir ve varsayılan olarak kullanılır")
print("   - Eğer MediaPipe sonuçları tatmin edici değilse DLIB veya OpenCV deneyin")
print("   - Yüz tanıma için recognize_faces() metodunu kullanabilirsiniz")
print("   - İyi aydınlatılmış ve net görüntüler en iyi sonuçları verir") 