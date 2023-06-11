from __future__ import print_function
from PIL import Image


def version(module, version):
    if v := getattr(module.core, f"{version}_version", None):
        print(version, v)


version(Image, "jpeglib")
version(Image, "zlib")
version(Image, "libtiff")

try:
    from PIL import ImageFont
except ImportError:
    pass
else:
    version(ImageFont, "freetype2")

try:
    from PIL import ImageCms
except ImportError:
    pass
else:
    version(ImageCms, "littlecms")
