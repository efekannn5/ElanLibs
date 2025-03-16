from elan.math_utils import math_utils
from elan.string_utils import string_utils
from elan.image_utils import image_utils
from elan.list_utils import list_utils
from elan.video_utils import video_utils


class elan:
    # math
    math = math_utils()
    # string
    string = string_utils()
    # list
    list = list_utils()
    # image
    image = image_utils()
    # video
    video = video_utils()


if __name__ == "__main__":
    elan()

