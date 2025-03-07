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
        
        self._create_widgets()
        self._create_layout()
    
    def _create_widgets(self):
        """
        Arayüz bileşenlerini oluşturur.
        """
        # Başlık
        self.title_label = ttk.Label(
            self, 
            text="Şifreleme Sanatı", 
            font=("Arial", 20, "bold")
        )
        
        # Logo (placeholder)
        self.logo_frame = ttk.Frame(self, width=200, height=200)
        self.logo_label = ttk.Label(
            self.logo_frame,
            text="[Logo]",
            font=("Arial", 40),
            anchor="center"
        )
        
        # Versiyon
        self.version_label = ttk.Label(
            self, 
            text="Versiyon 1.0", 
            font=("Arial", 12)
        )
        
        # Proje bilgisi
        self.info_frame = ttk.LabelFrame(self, text="Proje Hakkında")
        self.info_text = scrolledtext.ScrolledText(
            self.info_frame, 
            height=10, 
            width=60, 
            wrap=tk.WORD
        )
        self.info_text.insert(tk.END, """
        Şifreleme Sanatı, iki farklı şifreleme algoritması olan Caesar Cipher ve RSA algoritmalarını inceleyen, 
        bu algoritmaların nasıl çalıştığını anlamak ve günlük hayattaki önemini vurgulayan bir uygulamadır.
        
        Bu uygulama, şifreleme algoritmalarının pratikte nasıl işlediğini deneyimletmeyi amaçlamaktadır.
        
        Proje Amacı:
        İki farklı şifreleme algoritması olan Caesar Cipher ve RSA algoritmalarını incelemek, bu algoritmaların 
        nasıl çalıştığını anlamak ve günlük hayattaki önemini vurgulayan bir programla bu algoritmaların pratikte 
        nasıl işlediğini ziyaretçilere deneyimletmek.
        
        Beklenen Sonuç:
        Proje sonunda şifreleme yöntemlerinin nasıl çalıştığı daha iyi anlaşılacak. Python ile yazılan program 
        sayesinde, bu yöntemler daha somut bir şekilde görülecek. Sergi sırasında ziyaretçiler, kendi mesajlarını 
        şifreleyip çözerek hem öğrenecek hem de eğlenecek. Bu sayede siber güvenlik konusunda bilinç artışı olunacak. 
        Bu şekilde şifrelerin daha güçlü ve güvenli bir şekilde değiştirilmesi gerektiği anlaşılacaktır.
        """)
        self.info_text.config(state=tk.DISABLED)
        
        # Telif hakkı
        self.copyright_label = ttk.Label(
            self, 
            text="© 2025 Şifreleme Sanatı Projesi", 
            font=("Arial", 10)
        )
    
    def _create_layout(self):
        """
        Arayüz bileşenlerini düzenler.
        """
        # Başlık
        self.title_label.pack(pady=(20, 5))
        
        # Logo
        self.logo_frame.pack(pady=10)
        self.logo_label.place(relx=0.5, rely=0.5, anchor="center")
        
        # Versiyon
        self.version_label.pack(pady=(0, 20))
        
        # Proje bilgisi
        self.info_frame.pack(fill="both", expand=True, padx=20, pady=10)
        self.info_text.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Telif hakkı
        self.copyright_label.pack(pady=20) 