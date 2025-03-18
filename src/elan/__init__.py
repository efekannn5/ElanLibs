"""
Elan - Pratik Python yardımcı kütüphanesi
"""

# Temel modüller
from elan.main import elan
from elan.math_utils import math_utils
from elan.string_utils import string_utils
from elan.list_utils import list_utils

# Kurulum bilgisini görmek için
def kurulum_bilgisi():
    """Elan kütüphanesi kurulum bilgilerini gösterir"""
    print("\nELAN KÜTÜPHANESİ KURULUM BİLGİSİ")
    print("=" * 40)
    print("Yüklü olan modüller:")
    print("- Temel modüller (math, string, list)")
    
    try:
        import cv2
        print("- Görüntü işleme (image) ✓")
    except ImportError:
        print("- Görüntü işleme (image) ✗ - Kurulum için: pip install elan[image]")
    
    try:
        import dlib
        print("- DLIB ✓")
    except ImportError:
        print("- DLIB ✗ - Kurulum için: pip install elan[face] veya pip install dlib")
    
    try:
        import face_recognition
        print("- Face Recognition ✓")
    except ImportError:
        print("- Face Recognition ✗ - Kurulum için: pip install elan[face]")
    
    try:
        import mediapipe
        print("- MediaPipe ✓")
    except ImportError:
        print("- MediaPipe ✗ - Kurulum için: pip install elan[face] veya pip install mediapipe")
    
    print("\nKurulum seçenekleri:")
    print("- Temel kurulum: pip install elan")
    print("- Görüntü işleme: pip install elan[image]")
    print("- Yüz algılama: pip install elan[face]") 
    print("- Tam kurulum: pip install elan[all]")
    print("=" * 40)

# İsteğe bağlı modüller
try:
    from elan.image_utils import image_utils
except ImportError:
    # Image modülü içe aktarılmadığında modül yok olarak işaretlenir
    # Exception burada yakalanır ama main.py içinde ImportError fırlatılacak
    pass

try:
    from elan.video_utils import video_utils
except ImportError:
    # Video modülü içe aktarılmadığında modül yok olarak işaretlenir
    # Exception burada yakalanır ama main.py içinde ImportError fırlatılacak
    pass

__version__ = "0.3.6"
__author__ = "Efekan Nefesoğlu"
__license__ = "MIT"