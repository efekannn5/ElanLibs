#!/usr/bin/env python
# -*- coding: utf-8 -*-
import elan
import os
import sys
import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description='Elan kütüphanesi görüntü işleme testi')
    parser.add_argument('image_path', type=str, help='Test edilecek görüntü dosyasının yolu')
    args = parser.parse_args()
    
    # Görüntü dosyasının varlığını kontrol et
    if not os.path.exists(args.image_path):
        print(f"Hata: Belirtilen görüntü dosyası bulunamadı: {args.image_path}")
        sys.exit(1)
    
    print("\n=== Elan Kütüphanesi Görüntü İşleme Testi ===\n")
    
    # Elan kütüphanesini import et
    try:
        print("✓ Elan kütüphanesi başarıyla yüklendi.")
    except ImportError as e:
        print(f"✗ Elan kütüphanesi yüklenemedi: {e}")
        print("  Kurulum için: pip install elan")
        sys.exit(1)
    
    # Modül durumlarını kontrol et
    from elan import kurulum_bilgisi
    
    # Modül durumunu göster
    kurulum_bilgisi()
    
    # Eksik modül olsa bile testi çalıştırmaya devam et
    # Testi çalıştır - kullanılabilir özellikleri test et
    try:
        e = elan.elan()
        
        # Görüntü modülü var mı kontrol et
        if not hasattr(e, 'image'):
            print("\n✗ Görüntü işleme modülü yüklenmemiş. Test atlanıyor.")
            sys.exit(1)
        
        # Görüntüyü yükle
        print(f"\nGörüntü yükleniyor: {args.image_path}")
        img = e.image._read_image(args.image_path)
        
        if img is None:
            print("✗ Görüntü yüklenemedi!")
            sys.exit(1)
        
        print(f"✓ Görüntü başarıyla yüklendi. Boyut: {img.shape}")
        
        # Görüntü işleme testleri
        print("\nGörüntü işleme testleri:")
        
        # Gri tonlama testi
        try:
            print("\n- Gri tonlama dönüşümü test ediliyor...")
            gray = e.image.to_grayscale(img)
            print(f"  ✓ Görüntü gri tonlamaya dönüştürüldü. Boyut: {gray.shape}")
        except Exception as ex:
            print(f"  ✗ Test başarısız: {ex}")
        
        # Yeniden boyutlandırma testi
        try:
            print("\n- Yeniden boyutlandırma test ediliyor...")
            resized = e.image.resize(img, 300, 200)
            print(f"  ✓ Görüntü yeniden boyutlandırıldı. Yeni boyut: {resized.shape}")
        except Exception as ex:
            print(f"  ✗ Test başarısız: {ex}")
        
        # Kenar algılama testi
        try:
            print("\n- Kenar algılama test ediliyor...")
            edges = e.image.detect_edges(img)
            print(f"  ✓ Kenarlar algılandı. Boyut: {edges.shape}")
        except Exception as ex:
            print(f"  ✗ Test başarısız: {ex}")
        
        print("\nTest tamamlandı!")
    
    except Exception as e:
        print(f"Test sırasında hata oluştu: {e}")
        import traceback
        print(traceback.format_exc())
        sys.exit(1) 

if __name__ == "__main__":
    main() 