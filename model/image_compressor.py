
import os
from PIL import Image

class ImageCompressor:
    def __init__(self, input_folder, output_folder, quality, max_width, max_height):
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.quality = quality
        self.max_width = max_width
        self.max_height = max_height

        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

    def get_images(self):
        return [f for f in os.listdir(self.input_folder) if f.lower().endswith(('.jpg', '.jpeg'))]

    def count_images(self):
        return len(self.get_images())

    def compress_single_image(self, filename):
        filepath = os.path.join(self.input_folder, filename)
        with Image.open(filepath) as img:
            img = img.convert("RGB")
            img.thumbnail((self.max_width, self.max_height))
            output_path = os.path.join(self.output_folder, filename)
            img.save(output_path, "JPEG", optimize=True, quality=self.quality)
