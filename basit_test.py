#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
###############################################
#                                             #
#           ELAN KÜTÜPHANESİ                 #
#          BASIT YÜZ ALGILAMA                #
#              TEST ARACI                     #
#                                             #
###############################################

Bu test aracı, bir fotoğraftaki yüzleri algılar ve sonuçları kaydeder.
Kullanım: python basit_test.py resim.jpg
"""
from elan import elan
import os
import sys
import argparse

def main():
    # Komut satırı argümanını kontrol et
    if len(sys.argv) < 2:
        print("Hata: Görüntü dosyası belirtilmedi!")
        print("Kullanım: python basit_test.py resim.jpg")
        sys.exit(1)
    
    # Görüntü dosyasını al
    image_path = sys.argv[1]
    
    # Dosyanın varlığını kontrol et
    if not os.path.exists(image_path):
        print(f"Hata: Görüntü dosyası bulunamadı: {image_path}")
        sys.exit(1)
    
    print(f"\n=== {image_path} için Elan Testi ===")
    
    # Elan kütüphanesini import et
    try:
        
        e = elan()
        print("✓ Elan kütüphanesi yüklendi")
    except ImportError as ex:
        print(f"✗ Elan kütüphanesi yüklenemedi: {ex}")
        print("  Kurulum için: pip install elan")
        sys.exit(1)
    
    # Görüntüyü yükle
    try:
        img = e.image.load(image_path)
        print(f"✓ Görüntü yüklendi: {img.shape[1]}x{img.shape[0]} piksel")
    except Exception as ex:
        print(f"✗ Görüntü yüklenemedi: {ex}")
        sys.exit(1)
    
    print("\n--- Görüntü İşleme Sonuçları ---")
    
    # 1. Basit görüntü işleme
    try:
        gray_img = e.image.to_grayscale(img)
        print("✓ Gri tonlama işlemi başarılı")
    except Exception as ex:
        print(f"✗ Gri tonlama işlemi başarısız: {ex}")
    
    # 2. Kenar tespiti
    try:
        edges = e.image.detect_edges(img)
        print("✓ Kenar tespiti başarılı")
    except Exception as ex:
        print(f"✗ Kenar tespiti başarısız: {ex}")
    
    # 3. Yüz algılama (mevcut yöntemleri dene)
    print("\n--- Yüz Algılama Sonuçları ---")
    
    # Yüz algılama yöntemleri
    methods = ['opencv', 'dlib', 'mediapipe']
    successful_method = None
    detected_faces = None
    
    for method in methods:
        try:
            print(f"\nYüz algılama yöntemi: {method.upper()}")
            result_img, faces = e.image.detect_faces(img, method=method)
            print(f"✓ {len(faces)} yüz bulundu!")
            
            # Başarılı yöntemi ve sonuçları kaydet
            successful_method = method
            detected_faces = faces
            
            # Çıktı dizinini oluştur
            output_dir = "basit_test_sonuclari"
            os.makedirs(output_dir, exist_ok=True)
            
            # Sonucu kaydet
            output_path = os.path.join(output_dir, f"sonuc_{method}.jpg")
            e.image.save_image(result_img, output_path)
            print(f"✓ Sonuç kaydedildi: {output_path}")
            
        except Exception as ex:
            print(f"✗ {method.upper()} yöntemi başarısız: {ex}")
    
    # Özet
    print("\n=== Test Özeti ===")
    if successful_method is not None and detected_faces is not None:
        print(f"✓ En başarılı yöntem: {successful_method.upper()}")
        print(f"✓ Bulunan yüz sayısı: {len(detected_faces)}")
        print(f"✓ Sonuçlar 'basit_test_sonuclari' klasörüne kaydedildi")
    else:
        print("✗ Hiçbir yüz algılama yöntemi başarılı olmadı")
        print("  Daha net bir görüntü veya farklı yöntem deneyin")

if __name__ == "__main__":
    main() 