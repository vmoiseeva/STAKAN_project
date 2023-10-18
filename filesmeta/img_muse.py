from PIL import Image
from pillow_heif import register_heif_opener


class IMGMuse:
    ex = [".png", ".jpg", ".jpeg", ".tif", ".tiff", ".bmp", ".gif", ".heic", ".svg", ".ico", ".webp", ".raw", ".psd"]

    def get_meta_inf(self, path):
        metadata = {}
        register_heif_opener()
        try:
            with Image.open(path) as img:
                width, height = img.size

        except (FileNotFoundError, PermissionError):
            width, height = None, None

        metadata["Image Width"] = width
        metadata["Image Height"] = height

        return metadata
