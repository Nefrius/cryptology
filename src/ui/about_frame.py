"""
Hakkında Sekmesi

Bu modül, uygulama hakkında bilgi içeren sekme için kullanıcı arayüzünü içerir.
"""

import tkinter as tk
from tkinter import ttk, scrolledtext

class AboutFrame(ttk.Frame):
    def __init__(self, parent):
        """
        Hakkında sekmesi çerçevesini başlatır.
        
        Args:
            parent: Üst widget
        """
        super().__init__(parent)
        
        # Stil ayarları
        self.style = ttk.Style()
        
        # ScrolledText stilleri
        self.text_font = ('Segoe UI', 10)
        self.text_bg = '#ffffff'
        self.text_fg = '#333333'
        
        self._create_widgets()
        self._create_layout()
    
    def _create_widgets(self):
        """
        Arayüz bileşenlerini oluşturur.
        """
        # Ana çerçeve
        self.main_frame = ttk.Frame(self)
        
        # Başlık
        self.title_label = ttk.Label(
            self.main_frame,
            text="Şifreleme Sanatı",
            font=('Segoe UI', 24, 'bold'),
            foreground='#007bff'
        )
        
        # Alt başlık
        self.subtitle_label = ttk.Label(
            self.main_frame,
            text="Modern Şifreleme Teknikleri",
            font=('Segoe UI', 14),
            foreground='#6c757d'
        )
        
        # Versiyon
        self.version_label = ttk.Label(
            self.main_frame,
            text="Versiyon 1.0",
            font=('Segoe UI', 12),
            foreground='#28a745'
        )
        
        # Proje bilgisi
        self.info_frame = ttk.LabelFrame(
            self.main_frame,
            text="Proje Hakkında",
            padding=15
        )
        
        self.info_text = scrolledtext.ScrolledText(
            self.info_frame,
            height=12,
            width=60,
            wrap=tk.WORD,
            font=self.text_font,
            bg=self.text_bg,
            fg=self.text_fg
        )
        
        self.info_text.insert(tk.END, """
Şifreleme Sanatı, modern şifreleme tekniklerini öğrenmek ve uygulamak için tasarlanmış bir eğitim aracıdır.

Desteklenen Şifreleme Algoritmaları:

1. Caesar Cipher (Sezar Şifrelemesi)
   - Klasik yer değiştirme şifrelemesi
   - Türkçe ve İngilizce alfabe desteği
   - Frekans analizi görselleştirmesi
   - Kaba kuvvet çözümleme

2. RSA (Rivest-Shamir-Adleman)
   - Asimetrik şifreleme
   - 1024-4096 bit anahtar desteği
   - Güvenli anahtar üretimi
   - Adım adım şifreleme/çözme gösterimi

Bu uygulama, kriptografi öğrenmek isteyenler için pratik bir araç olarak tasarlanmıştır. Kullanıcı dostu arayüzü ve detaylı açıklamalarıyla, şifreleme kavramlarını anlamayı kolaylaştırır.

Güvenlik Notu: Bu uygulama eğitim amaçlıdır. Hassas verilerin şifrelenmesi için profesyonel güvenlik çözümleri kullanılmalıdır.
        """)
        self.info_text.config(state=tk.DISABLED)
        
        # Telif hakkı
        self.copyright_label = ttk.Label(
            self.main_frame,
            text="© 2024 Tüm hakları saklıdır.",
            font=('Segoe UI', 9),
            foreground='#6c757d'
        )
    
    def _create_layout(self):
        """
        Arayüz bileşenlerini düzenler.
        """
        # Ana çerçeve
        self.main_frame.pack(expand=True, fill="both", padx=40, pady=20)
        
        # Başlık ve alt başlık
        self.title_label.pack(pady=(20, 5))
        self.subtitle_label.pack(pady=(0, 20))
        
        # Versiyon
        self.version_label.pack(pady=(0, 30))
        
        # Proje bilgisi
        self.info_frame.pack(fill="both", expand=True)
        self.info_text.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Telif hakkı
        self.copyright_label.pack(pady=20) 