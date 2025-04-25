from elan.math_utils import math_utils
from elan.string_utils import string_utils
from elan.image_utils import image_utils
from elan.list_utils import list_utils
from elan.video_utils import video_utils


class elan:
    # math - matematiksel işlemler
    math = math_utils()
    mat = math_utils()  # Türkçe alternatif
    
    # string - metin işlemleri
    string = string_utils()
    yazi = string_utils()  # Türkçe alternatif
    
    # list - liste işlemleri
    list = list_utils()
    dizi = list_utils()  # Türkçe alternatif
    
    # image - görüntü işlemleri
    image = image_utils()
    goruntu = image_utils()  # Türkçe alternatif
    
    # video - video işlemleri
    video = video_utils()


if __name__ == "__main__":
    elan()

