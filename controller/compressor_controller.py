
from model.image_compressor import ImageCompressor
from tkinter import messagebox

class CompressorController:
    def __init__(self, view):
        self.view = view

    def start_compression(self, input_folder, output_folder, quality, max_width, max_height):
        try:
            compressor = ImageCompressor(
                input_folder, output_folder, quality, max_width, max_height
            )
            total_files = compressor.count_images()

            for i, filename in enumerate(compressor.get_images(), start=1):
                compressor.compress_single_image(filename)
                self.view.update_progress(i, total_files)

            messagebox.showinfo("Sucesso", f"{total_files} imagens comprimidas com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))
