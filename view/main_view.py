
import customtkinter as ctk
from tkinter import filedialog, messagebox
from controller.compressor_controller import CompressorController


class MainView:
    def __init__(self, root):
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.root = root
        self.root.title("Compressor de Imagens JPG")
        self.root.geometry("600x500")
        self.root.resizable(False, False)

        self.controller = CompressorController(self)

        self.build_ui()

    def build_ui(self):
        frame = ctk.CTkFrame(self.root)
        frame.pack(padx=20, pady=20, fill="both", expand=True)

        ctk.CTkLabel(frame, text="Pasta de Entrada:").pack(pady=(10, 0))
        self.input_entry = ctk.CTkEntry(frame, width=400)
        self.input_entry.pack()
        ctk.CTkButton(frame, text="Selecionar", command=self.browse_input).pack(pady=5)

        ctk.CTkLabel(frame, text="Pasta de Saída:").pack(pady=(10, 0))
        self.output_entry = ctk.CTkEntry(frame, width=400)
        self.output_entry.pack()
        ctk.CTkButton(frame, text="Selecionar", command=self.browse_output).pack(pady=5)

        ctk.CTkLabel(frame, text="Qualidade da Imagem:").pack(pady=(15, 0))
        self.quality_slider = ctk.CTkSlider(frame, from_=10, to=95, number_of_steps=85)
        self.quality_slider.set(50)
        self.quality_slider.pack(pady=5)

        resolution_frame = ctk.CTkFrame(frame)
        resolution_frame.pack(pady=(10, 0))

        ctk.CTkLabel(resolution_frame, text="Largura Máxima:").grid(row=0, column=0, padx=5)
        self.width_entry = ctk.CTkEntry(resolution_frame, width=80)
        self.width_entry.insert(0, "1920")
        self.width_entry.grid(row=0, column=1, padx=5)

        ctk.CTkLabel(resolution_frame, text="Altura Máxima:").grid(row=0, column=2, padx=5)
        self.height_entry = ctk.CTkEntry(resolution_frame, width=80)
        self.height_entry.insert(0, "1080")
        self.height_entry.grid(row=0, column=3, padx=5)

        self.progress = ctk.CTkProgressBar(frame)
        self.progress.set(0)
        self.progress.pack(pady=20, fill="x", padx=10)

        ctk.CTkButton(frame, text="Iniciar Compressão", command=self.start_compression).pack(pady=10)

    def browse_input(self):
        folder = filedialog.askdirectory()
        if folder:
            self.input_entry.delete(0, "end")
            self.input_entry.insert(0, folder)

    def browse_output(self):
        folder = filedialog.askdirectory()
        if folder:
            self.output_entry.delete(0, "end")
            self.output_entry.insert(0, folder)

    def start_compression(self):
        input_folder = self.input_entry.get()
        output_folder = self.output_entry.get()
        quality = int(self.quality_slider.get())
        max_width = int(self.width_entry.get())
        max_height = int(self.height_entry.get())

        if not input_folder or not output_folder:
            messagebox.showerror("Erro", "Selecione as pastas de entrada e saída.")
            return

        self.controller.start_compression(
            input_folder,
            output_folder,
            quality,
            max_width,
            max_height
        )

    def update_progress(self, current, total):
        self.progress.set(current / total if total > 0 else 0)
