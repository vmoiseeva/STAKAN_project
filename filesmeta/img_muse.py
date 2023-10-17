from PIL import Image
from pillow_heif import register_heif_opener

class IMGMuse:
    ex = [".png", ".jpg", ".jpeg", ".tif", ".tiff", ".bmp", ".gif", ".heic", ".svg", ".ico", ".webp", ".raw", ".psd" ]

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

if __name__ == "__main__":
    # Create an instance of the class with the path to the CSV file
    collector = IMGMuse()

    # Collect and add file meta information to the CSV
    print(collector.get_meta_inf('/Users/valeriiamoiseeva/Downloads/IMG_5417.heic'))