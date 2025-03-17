"""
Elan - Pratik Python yardımcı kütüphanesi
"""

import warnings
import sys

# Temel modüller
from elan.main import elan
from elan.math_utils import math_utils
from elan.string_utils import string_utils
from elan.list_utils import list_utils

# Modül durumlarını izlemek için sözlük
MODULES_STATUS = {
    'opencv': {'available': False, 'error': None},
    'dlib': {'available': False, 'error': None},
    'face_recognition': {'available': False, 'error': None},
    'mediapipe': {'available': False, 'error': None}
}

# İsteğe bağlı bağımlılıkları kontrol et
try:
    import cv2
    MODULES_STATUS['opencv']['available'] = True
    from elan.image_utils import image_utils  # OpenCV mevcut olduğunda görüntü işleme özelliklerini yükle
except ImportError as e:
    MODULES_STATUS['opencv']['error'] = str(e)
    warnings.warn(
        f"OpenCV kütüphanesi bulunamadı: {e}. Görüntü işleme özellikleri devre dışı kalacak.",
        ImportWarning
    )
    # Dummy sınıf tanımla
    class image_utils:
        def __init__(self):
            self._missing_opencv_message = "OpenCV kütüphanesi yüklenmedi. Görüntü işleme özellikleri kullanılamaz."
        def __getattr__(self, name):
            warnings.warn(self._missing_opencv_message, RuntimeWarning)
            return self._unavailable_function

        def _unavailable_function(self, *args, **kwargs):
            raise ImportError(self._missing_opencv_message)

# Video işleme özellikleri de OpenCV'ye bağlı
if MODULES_STATUS['opencv']['available']:
    try:
        from elan.video_utils import video_utils
    except ImportError as e:
        warnings.warn(f"Video modülleri yüklenemedi: {e}", ImportWarning)
        class video_utils:
            def __init__(self):
                self._error_message = f"Video modülleri yüklenemedi: {e}"
            def __getattr__(self, name):
                warnings.warn(self._error_message, RuntimeWarning)
                return self._unavailable_function
            def _unavailable_function(self, *args, **kwargs):
                raise ImportError(self._error_message)
else:
    # Dummy sınıf tanımla
    class video_utils:
        def __init__(self):
            self._missing_opencv_message = "OpenCV kütüphanesi yüklenmedi. Video işleme özellikleri kullanılamaz."
        def __getattr__(self, name):
            warnings.warn(self._missing_opencv_message, RuntimeWarning)
            return self._unavailable_function

        def _unavailable_function(self, *args, **kwargs):
            raise ImportError(self._missing_opencv_message)

# Yüz algılama özellikleri için modül kontrolü
try:
    import dlib
    MODULES_STATUS['dlib']['available'] = True
except ImportError as e:
    MODULES_STATUS['dlib']['error'] = str(e)
    warnings.warn(
        f"DLIB kütüphanesi yüklenemedi: {e}. Yüz algılama özellikleri kısıtlı olacak.",
        ImportWarning
    )

try:
    import face_recognition
    MODULES_STATUS['face_recognition']['available'] = True
except ImportError as e:
    MODULES_STATUS['face_recognition']['error'] = str(e)
    warnings.warn(
        f"face_recognition kütüphanesi yüklenemedi: {e}. Yüz tanıma özellikleri kullanılamayacak.",
        ImportWarning
    )

try:
    import mediapipe
    MODULES_STATUS['mediapipe']['available'] = True
except ImportError as e:
    MODULES_STATUS['mediapipe']['error'] = str(e)
    warnings.warn(
        f"MediaPipe kütüphanesi yüklenemedi: {e}. Gelişmiş yüz algılama özellikleri kullanılamayacak.",
        ImportWarning
    )

# Modül durumlarını ekrana yazdır
def print_module_status():
    """Modül durumlarını ve olası kurulum hatalarını ekrana yazdırır"""
    print("\nElan Kütüphanesi - Modül Durumu:")
    print("=" * 50)
    all_available = True
    
    for module, status in MODULES_STATUS.items():
        if status['available']:
            print(f"✓ {module.upper()}: Yüklendi")
        else:
            all_available = False
            print(f"✗ {module.upper()}: Yüklenemedi - {status['error']}")
    
    if not all_available:
        print("\nKurulum İpuçları:")
        if not MODULES_STATUS['opencv']['available']:
            print("- OpenCV için: pip install opencv-python")
        
        if not MODULES_STATUS['dlib']['available']:
            print("- DLIB için (Windows):")
            print("  * Kolay yöntem: pip install https://github.com/jloh02/dlib/releases/download/v19.22/dlib-19.22.99-cp310-cp310-win_amd64.whl")
            print("  * Manuel kurulum: CMake ve Visual Studio yükleyin, sonra: pip install dlib")
        
        if not MODULES_STATUS['face_recognition']['available'] and MODULES_STATUS['dlib']['available']:
            print("- Face Recognition için: pip install face_recognition")
        
        if not MODULES_STATUS['mediapipe']['available']:
            print("- MediaPipe için: pip install mediapipe")
    
    print("=" * 50)
    print("Not: Eksik özellikler olmadan da kütüphanenin diğer özellikleri kullanılabilir.")

# Modül durumlarını kontrol etmeyi sağlayan fonksiyon
def check_modules():
    """Modül durumlarını kontrol eder ve sonucu döndürür"""
    return MODULES_STATUS

__version__ = "0.3.3"
__author__ = "Efekan Nefesoğlu"
__license__ = "MIT"