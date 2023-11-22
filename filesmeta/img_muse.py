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
                resolution = img.info.get("dpi")
                compression = img.info.get("compression")
                orientation = img.info.get("exif")


        except (FileNotFoundError, PermissionError):
            width, height = None, None
            resolution = None
            compression = None
            orientation = None

        metadata["Image Width"] = width
        metadata["Image Height"] = height
        metadata["Resolution"] = resolution
        metadata["Compression"] = compression
        metadata["Orientation"] = orientation

        return metadata
