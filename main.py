"""
Şifreleme Sanatı - Ana Uygulama

Bu dosya, uygulamayı başlatır.
"""

import tkinter as tk
from src.ui.main_window import MainWindow

def main():
    """
    Ana uygulamayı başlatır.
    """
    root = tk.Tk()
    app = MainWindow(root)
    app.run()

if __name__ == "__main__":
    main() 