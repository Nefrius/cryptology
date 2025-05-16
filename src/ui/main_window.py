"""
Şifreleme Sanatı - Ana Uygulama Penceresi

Bu modül, uygulamanın ana penceresini ve kullanıcı arayüzünü içerir.
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import sys
import os

# Proje kök dizinini sys.path'e ekle
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.algorithms.caesar_cipher import CaesarCipher
from src.algorithms.rsa_cipher import RSACipher
from src.ui.caesar_frame import CaesarFrame
from src.ui.rsa_frame import RSAFrame
from src.ui.about_frame import AboutFrame

class MainWindow:
    def __init__(self, root):
        """
        Ana uygulama penceresini başlatır.
        
        Args:
            root (tk.Tk): Tkinter kök penceresi
        """
        self.root = root
        self.root.title("Şifreleme Sanatı")
        self.root.geometry("1000x700")
        self.root.minsize(900, 600)
        
        # Tema ve stil ayarları
        self.style = ttk.Style()
        self.style.theme_use('clam')  # Modern görünüm için clam teması
        
        # Özel renk paleti
        self.style.configure('.',
            background='#f0f0f0',
            foreground='#333333',
            font=('Segoe UI', 10)
        )
        
        # Frame stilleri
        self.style.configure('TFrame',
            background='#ffffff'
        )
        
        # Label stilleri
        self.style.configure('TLabel',
            background='#ffffff',
            font=('Segoe UI', 10)
        )
        
        # Button stilleri
        self.style.configure('TButton',
            padding=6,
            relief='flat',
            background='#007bff',
            foreground='white'
        )
        
        self.style.map('TButton',
            background=[('active', '#0056b3'), ('disabled', '#cccccc')],
            foreground=[('disabled', '#666666')]
        )
        
        # Notebook stilleri
        self.style.configure('TNotebook',
            background='#ffffff',
            padding=5
        )
        
        self.style.configure('TNotebook.Tab',
            padding=[12, 4],
            font=('Segoe UI', 10)
        )
        
        self.style.map('TNotebook.Tab',
            background=[('selected', '#007bff'), ('active', '#e6f3ff')],
            foreground=[('selected', '#ffffff'), ('active', '#007bff')]
        )
        
        # LabelFrame stilleri
        self.style.configure('TLabelframe',
            background='#ffffff',
            relief='solid',
            borderwidth=1
        )
        
        self.style.configure('TLabelframe.Label',
            background='#ffffff',
            font=('Segoe UI', 10, 'bold')
        )
        
        # Entry stilleri
        self.style.configure('TEntry',
            fieldbackground='#ffffff',
            borderwidth=1,
            relief='solid'
        )
        
        # Algoritma nesnelerini oluştur
        self.caesar_cipher = CaesarCipher()
        self.rsa_cipher = RSACipher()
        
        self._create_menu()
        self._create_notebook()
        self._create_status_bar()
        
        # Varsayılan olarak Caesar Cipher sekmesini göster
        self.notebook.select(0)
        
        # Pencere arkaplan rengi
        self.root.configure(bg='#f0f0f0')
    
    def _create_menu(self):
        """
        Uygulama menüsünü oluşturur.
        """
        menubar = tk.Menu(self.root)
        
        # Dosya menüsü
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Yeni", command=self._new_session)
        file_menu.add_separator()
        file_menu.add_command(label="Çıkış", command=self.root.quit)
        menubar.add_cascade(label="Dosya", menu=file_menu)
        
        # Yardım menüsü
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="Şifreleme Hakkında", command=self._show_encryption_info)
        help_menu.add_command(label="Hakkında", command=self._show_about)
        menubar.add_cascade(label="Yardım", menu=help_menu)
        
        self.root.config(menu=menubar)
    
    def _create_notebook(self):
        """
        Sekme yapısını oluşturur.
        """
        self.notebook = ttk.Notebook(self.root)
        
        # Caesar Cipher sekmesi
        self.caesar_frame = CaesarFrame(self.notebook, self.caesar_cipher)
        
        # RSA sekmesi
        self.rsa_frame = RSAFrame(self.notebook, self.rsa_cipher)
        
        # Hakkında sekmesi
        self.about_frame = AboutFrame(self.notebook)
        
        # Sekmeleri ekle
        self.notebook.add(self.caesar_frame, text="Caesar Cipher")
        self.notebook.add(self.rsa_frame, text="RSA")
        self.notebook.add(self.about_frame, text="Hakkında")
        
        self.notebook.pack(expand=True, fill="both", padx=10, pady=10)
    
    def _create_status_bar(self):
        """
        Durum çubuğunu oluşturur.
        """
        self.status_var = tk.StringVar()
        self.status_var.set("Hazır")
        
        self.status_bar = ttk.Label(
            self.root, 
            textvariable=self.status_var, 
            relief=tk.SUNKEN, 
            anchor=tk.W
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def _new_session(self):
        """
        Yeni bir oturum başlatır.
        """
        self.caesar_frame.clear()
        self.rsa_frame.clear()
        self.status_var.set("Yeni oturum başlatıldı")
    
    def _show_encryption_info(self):
        """
        Şifreleme hakkında bilgi penceresini gösterir.
        """
        info_window = tk.Toplevel(self.root)
        info_window.title("Şifreleme Hakkında")
        info_window.geometry("600x400")
        
        notebook = ttk.Notebook(info_window)
        
        # Caesar Cipher bilgisi
        caesar_frame = ttk.Frame(notebook)
        caesar_text = scrolledtext.ScrolledText(caesar_frame, wrap=tk.WORD)
        caesar_text.insert(tk.END, """
        Caesar Cipher (Sezar Şifrelemesi)
        
        Caesar Cipher, Julius Caesar tarafından kullanılan basit bir yer değiştirme şifreleme tekniğidir. 
        Bu şifreleme yönteminde, düz metindeki her harf, alfabede belirli bir sayı kadar kaydırılarak şifrelenir.
        
        Örneğin, 3 birimlik bir kaydırma ile:
        - A harfi D olur
        - B harfi E olur
        - ...
        - Z harfi C olur
        
        Avantajları:
        - Anlaşılması ve uygulanması kolaydır
        - Hızlı şifreleme ve şifre çözme
        
        Dezavantajları:
        - Çok güvenli değildir
        - Frekans analizi ile kolayca kırılabilir
        - Sadece 26 olası anahtar vardır (İngilizce alfabesi için)
        """)
        caesar_text.config(state=tk.DISABLED)
        caesar_text.pack(expand=True, fill="both", padx=10, pady=10)
        
        # RSA bilgisi
        rsa_frame = ttk.Frame(notebook)
        rsa_text = scrolledtext.ScrolledText(rsa_frame, wrap=tk.WORD)
        rsa_text.insert(tk.END, """
        RSA (Rivest-Shamir-Adleman)
        
        RSA, 1977 yılında Ron Rivest, Adi Shamir ve Leonard Adleman tarafından geliştirilen asimetrik bir şifreleme algoritmasıdır.
        Bu algoritma, genel anahtar kriptografisine dayanır ve iki farklı anahtar kullanır:
        - Genel anahtar (public key): Şifreleme için kullanılır ve herkesle paylaşılabilir
        - Özel anahtar (private key): Şifre çözme için kullanılır ve gizli tutulmalıdır
        
        RSA'nın güvenliği, büyük sayıların çarpanlarına ayrılmasının zorluğuna dayanır.
        
        Avantajları:
        - Yüksek güvenlik seviyesi
        - Dijital imza için kullanılabilir
        - Anahtar dağıtımı problemi çözülmüştür
        
        Dezavantajları:
        - Simetrik şifrelemeye göre daha yavaştır
        - Büyük anahtarlar gerektirir
        - Kuantum bilgisayarlar tarafından kırılabilir
        """)
        rsa_text.config(state=tk.DISABLED)
        rsa_text.pack(expand=True, fill="both", padx=10, pady=10)
        
        # Karşılaştırma
        comparison_frame = ttk.Frame(notebook)
        comparison_text = scrolledtext.ScrolledText(comparison_frame, wrap=tk.WORD)
        comparison_text.insert(tk.END, """
        Şifreleme Yöntemlerinin Karşılaştırması
        
        Simetrik Şifreleme (Caesar Cipher gibi):
        - Aynı anahtar hem şifreleme hem de şifre çözme için kullanılır
        - Hızlıdır
        - Anahtar dağıtımı problemi vardır
        - Genellikle büyük veri miktarları için kullanılır
        
        Asimetrik Şifreleme (RSA gibi):
        - Farklı anahtarlar şifreleme ve şifre çözme için kullanılır
        - Daha yavaştır
        - Anahtar dağıtımı problemi çözülmüştür
        - Genellikle anahtar değişimi ve dijital imza için kullanılır
        
        Modern sistemlerde, her iki şifreleme türü de birlikte kullanılır:
        - Asimetrik şifreleme, simetrik anahtarın güvenli bir şekilde paylaşılması için kullanılır
        - Simetrik şifreleme, veri şifreleme için kullanılır
        """)
        comparison_text.config(state=tk.DISABLED)
        comparison_text.pack(expand=True, fill="both", padx=10, pady=10)
        
        notebook.add(caesar_frame, text="Caesar Cipher")
        notebook.add(rsa_frame, text="RSA")
        notebook.add(comparison_frame, text="Karşılaştırma")
        
        notebook.pack(expand=True, fill="both", padx=10, pady=10)
    
    def _show_about(self):
        """
        Hakkında penceresini gösterir.
        """
        messagebox.showinfo(
            "Hakkında", 
            "Şifreleme Sanatı v1.0\n\n"
            "Bu uygulama, şifreleme algoritmalarını öğrenmek ve deneyimlemek için tasarlanmıştır.\n\n"
            "© 2025 Şifreleme Sanatı Projesi"
        )
    
    def run(self):
        """
        Uygulamayı çalıştırır.
        """
        self.root.mainloop() 