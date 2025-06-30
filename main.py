import customtkinter as ctk
from view.main_view import MainView

if __name__ == "__main__":
    root = ctk.CTk()
    app = MainView(root)
    root.mainloop()
