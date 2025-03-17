from elan.math_utils import math_utils
from elan.string_utils import string_utils
from elan.list_utils import list_utils

# İsteğe bağlı modüller
try:
    from elan.image_utils import image_utils
    _has_image = True
except ImportError:
    _has_image = False

try:
    from elan.video_utils import video_utils
    _has_video = True
except ImportError:
    _has_video = False


class elan:
    # Temel işlevler
    math = math_utils()
    string = string_utils()
    list = list_utils()
    
    def __init__(self):
        # Görüntü işleme (isteğe bağlı)
        if '_has_image' in globals() and _has_image:
            self.image = image_utils()
        else:
            # Görüntü işleme kurulu değil - bu özellikler kullanıldığında
            # hata fırlatacak şekilde ayarla
            self._setup_missing_image()
        
        # Video işleme (isteğe bağlı)
        if '_has_video' in globals() and _has_video:
            self.video = video_utils()
        else:
            # Video işleme kurulu değil - bu özellikler kullanıldığında
            # hata fırlatacak şekilde ayarla
            self._setup_missing_video()
    
    def _setup_missing_image(self):
        """Görüntü işleme modülü eksikse uygun hata veren bir nesne oluştur"""
        class MissingImageModule:
            def __init__(self):
                self.error_message = "Görüntü işleme modülü yüklenmemiş! Kurulum için: pip install elan[image]"
                
            def __getattr__(self, name):
                """Herhangi bir özelliğe erişildiğinde ImportError fırlat"""
                raise ImportError(self.error_message)
        
        self.image = MissingImageModule()
    
    def _setup_missing_video(self):
        """Video işleme modülü eksikse uygun hata veren bir nesne oluştur"""
        class MissingVideoModule:
            def __init__(self):
                self.error_message = "Video işleme modülü yüklenmemiş! Kurulum için: pip install elan[image]"
                
            def __getattr__(self, name):
                """Herhangi bir özelliğe erişildiğinde ImportError fırlat"""
                raise ImportError(self.error_message)
        
        self.video = MissingVideoModule()


if __name__ == "__main__":
    from elan import kurulum_bilgisi
    
    print("\nElan - Çok Yönlü Python Yardımcı Kütüphanesi")
    print("-" * 46)
    print("Kullanım: import elan; e = elan.elan()")
    
    # Kurulum bilgisini göster
    kurulum_bilgisi()

