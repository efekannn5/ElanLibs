from elan.math_utils import math_utils
from elan.string_utils import string_utils
from elan.list_utils import list_utils

# İsteğe bağlı modüller
try:
    from elan.image_utils import image_utils
    _has_image_utils = True
except ImportError:
    _has_image_utils = False
    # image_utils __init__.py'de dummy sınıf olarak tanımlandı

try:
    from elan.video_utils import video_utils
    _has_video_utils = True
except ImportError:
    _has_video_utils = False
    # video_utils __init__.py'de dummy sınıf olarak tanımlandı


class elan:
    # Temel işlevler
    math = math_utils()
    string = string_utils()
    list = list_utils()
    
    # İsteğe bağlı işlevler - her durumda kullanılabilir
    # (eksik kütüphaneler için uyarı verilecek)
    image = image_utils() if '_has_image_utils' in globals() and _has_image_utils else None
    video = video_utils() if '_has_video_utils' in globals() and _has_video_utils else None
    
    def __init__(self):
        # Eksik modüller hakkında bilgi ver
        if self.image is None:
            print("Uyarı: Görüntü işleme modülleri yüklenemedi. 'pip install elan[image]' komutu ile yükleyin.")
        if self.video is None:
            print("Uyarı: Video işleme modülleri yüklenemedi. 'pip install elan[image]' komutu ile yükleyin.")


if __name__ == "__main__":
    elan()

