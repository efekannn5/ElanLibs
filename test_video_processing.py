from elan import elan
import os
import time
import numpy as np
import cv2

# Elan sınıfını başlat
el = elan()

print("Elan Video İşleme Modülü - Test")
print("=" * 50)

# Test başlangıç zamanı
start_time = time.time()

# Test için örnek video oluştur
def create_test_video(output_file="test_video.mp4", duration_seconds=5, fps=30, width=640, height=480):
    """Test için basit bir video oluştur - hareketli beyaz kare"""
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(output_file, fourcc, fps, (width, height))
    
    if not video_writer.isOpened():
        print("Video dosyası oluşturulamadı!")
        return False
    
    total_frames = duration_seconds * fps
    square_size = 50
    square_pos = [width // 2 - square_size // 2, height // 2 - square_size // 2]
    velocity = [5, 3]  # x ve y yönündeki hız
    
    for i in range(int(total_frames)):
        # Siyah arka plan oluştur
        frame = np.zeros((height, width, 3), dtype=np.uint8)
        
        # Karenin yeni pozisyonunu hesapla
        square_pos[0] += velocity[0]
        square_pos[1] += velocity[1]
        
        # Sınırlara çarptığında yön değiştir
        if square_pos[0] < 0 or square_pos[0] > width - square_size:
            velocity[0] = -velocity[0]
            square_pos[0] += velocity[0]
        if square_pos[1] < 0 or square_pos[1] > height - square_size:
            velocity[1] = -velocity[1]
            square_pos[1] += velocity[1]
        
        # Beyaz kareyi çiz
        x, y = square_pos
        frame[y:y+square_size, x:x+square_size] = 255
        
        # Çerçeveyi videoya ekle
        video_writer.write(frame)
    
    video_writer.release()
    return True

# Test videosu oluştur
test_video_path = "test_video.mp4"
if create_test_video(test_video_path):
    print(f"Test için örnek video oluşturuldu: {test_video_path}")
else:
    print("Test videosu oluşturulamadı, lütfen OpenCV kurulumunu kontrol edin.")
    exit(1)

# Video fonksiyonlarını test et
print("\n1. Video Bilgisi Testi:")
try:
    video_info = el.video.get_video_info(test_video_path)
    print("✓ Video bilgisi alındı:")
    for key, value in video_info.items():
        print(f"  - {key}: {value}")
except Exception as e:
    print(f"✗ Video bilgisi hatası: {e}")

print("\n2. Kare Çıkarma Testi:")
try:
    # Tüm kareleri çıkar
    frames_dir = "test_frames"
    os.makedirs(frames_dir, exist_ok=True)
    frame_paths = el.video.extract_frames(test_video_path, frames_dir, frame_interval=10)
    print(f"✓ {len(frame_paths)} kare video kaydedildi: {frames_dir}")
except Exception as e:
    print(f"✗ Kare çıkarma hatası: {e}")

print("\n3. Video Dönüştürme Testi:")
try:
    # Videoyu dönüştür (küçült)
    output_video = "test_converted.mp4"
    success = el.video.convert_video(test_video_path, output_video, resize=(320, 240))
    print(f"✓ Video dönüştürme {'başarılı' if success else 'başarısız'}: {output_video}")
except Exception as e:
    print(f"✗ Video dönüştürme hatası: {e}")

print("\n4. Video Kırpma Testi:")
try:
    # Videoyu kırp (ilk 2 saniyesini al)
    output_video = "test_trimmed.mp4"
    success = el.video.trim_video(test_video_path, output_video, 0, 2)
    print(f"✓ Video kırpma {'başarılı' if success else 'başarısız'}: {output_video}")
except Exception as e:
    print(f"✗ Video kırpma hatası: {e}")

print("\n5. Filtreleme Testi:")
try:
    # Videoyu gri tonlamalı yap
    output_video = "test_grayscale.mp4"
    success = el.video.apply_filter_to_video(test_video_path, output_video, "grayscale")
    print(f"✓ Gri tonlama filtresi {'başarılı' if success else 'başarısız'}: {output_video}")
except Exception as e:
    print(f"✗ Video filtreleme hatası: {e}")

print("\n6. Metin Ekleme Testi:")
try:
    # Videoya metin ekle
    output_video = "test_with_text.mp4"
    success = el.video.add_text_to_video(test_video_path, output_video, "Elan Test")
    print(f"✓ Metin ekleme {'başarılı' if success else 'başarısız'}: {output_video}")
except Exception as e:
    print(f"✗ Metin ekleme hatası: {e}")

# Test sonuçlarını özetle
test_duration = time.time() - start_time
print(f"\nTest Tamamlandı - Süre: {test_duration:.2f} saniye")
print("Test sonuçları ve oluşturulan videolar şu dizinde bulunabilir:", os.getcwd()) 