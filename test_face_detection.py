#!/usr/bin/env python
# -*- coding: utf-8 -*-
import elan
import os
import sys
import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description='Elan kütüphanesi yüz algılama testi')
    parser.add_argument('image_path', type=str, help='Test edilecek görüntü dosyasının yolu')
    args = parser.parse_args()
    
    # Görüntü dosyasının varlığını kontrol et
    if not os.path.exists(args.image_path):
        print(f"Hata: Belirtilen görüntü dosyası bulunamadı: {args.image_path}")
        sys.exit(1)
    
    print("\n=== Elan Kütüphanesi Yüz Algılama Testi ===\n")
    
    # Elan kütüphanesini import et
    try:
        
        print("✓ Elan kütüphanesi başarıyla yüklendi.")
    except ImportError as e:
        print(f"✗ Elan kütüphanesi yüklenemedi: {e}")
        print("  Kurulum için: pip install elan")
        sys.exit(1)
    
    # Modül durumlarını kontrol et
    from elan import MODULES_STATUS, print_module_status
    
    # Tüm modüllerin durumunu göster
    print_module_status()
    
    # Eksik modül olsa bile testi çalıştırmaya devam et
    # Testi çalıştır - kullanılabilir özellikleri test et
    try:
        e = elan.elan()
        
        # Görüntü modülü var mı kontrol et
        if e.image is None:
            print("\n✗ Görüntü işleme modülü yüklenmemiş. Test atlanıyor.")
            sys.exit(1)
        
        # Görüntüyü yükle
        print(f"\nGörüntü yükleniyor: {args.image_path}")
        img = e.image.load(args.image_path)
        
        if img is None:
            print("✗ Görüntü yüklenemedi!")
            sys.exit(1)
        
        print(f"✓ Görüntü başarıyla yüklendi. Boyut: {img.shape}")
        
        # Kullanılabilir yüz algılama yöntemlerini dene
        print("\nYüz algılama testleri:")
        
        # Face Recognition yöntemi (dlib tabanlı)
        if MODULES_STATUS['face_recognition']['available']:
            try:
                print("\n- Face Recognition yöntemi ile test ediliyor...")
                faces = e.image.detect_faces(img, method="face_recognition")
                print(f"  ✓ {len(faces)} yüz bulundu!")
            except Exception as ex:
                print(f"  ✗ Test başarısız: {ex}")
        else:
            print("\n- Face Recognition yöntemi test edilemiyor (kütüphane yüklenmemiş).")
        
        # MediaPipe yöntemi
        if MODULES_STATUS['mediapipe']['available']:
            try:
                print("\n- MediaPipe yöntemi ile test ediliyor...")
                faces = e.image.detect_faces(img, method="mediapipe")
                print(f"  ✓ {len(faces)} yüz bulundu!")
            except Exception as ex:
                print(f"  ✗ Test başarısız: {ex}")
        else:
            print("\n- MediaPipe yöntemi test edilemiyor (kütüphane yüklenmemiş).")
        
        # OpenCV yöntemi
        if MODULES_STATUS['opencv']['available']:
            try:
                print("\n- OpenCV (haar cascade) yöntemi ile test ediliyor...")
                faces = e.image.detect_faces(img, method="opencv")
                print(f"  ✓ {len(faces)} yüz bulundu!")
            except Exception as ex:
                print(f"  ✗ Test başarısız: {ex}")
        else:
            print("\n- OpenCV yöntemi test edilemiyor (kütüphane yüklenmemiş).")
        
        print("\nTest tamamlandı!")
    
    except Exception as e:
        print(f"Test sırasında hata oluştu: {e}")
        import traceback
        print(traceback.format_exc())
        sys.exit(1) 

if __name__ == "__main__":
    main() 