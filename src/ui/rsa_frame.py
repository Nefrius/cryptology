"""
RSA Kullanıcı Arayüzü

Bu modül, RSA şifreleme algoritması için kullanıcı arayüzünü içerir.
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class RSAFrame(ttk.Frame):
    def __init__(self, parent, rsa_cipher):
        """
        RSA arayüz çerçevesini başlatır.
        
        Args:
            parent: Üst widget
            rsa_cipher (RSACipher): RSA algoritma nesnesi
        """
        super().__init__(parent)
        self.rsa_cipher = rsa_cipher
        
        self._create_widgets()
        self._create_layout()
    
    def _create_widgets(self):
        """
        Arayüz bileşenlerini oluşturur.
        """
        # Başlık
        self.title_label = ttk.Label(
            self, 
            text="RSA Şifreleme", 
            font=("Arial", 16, "bold")
        )
        
        # Açıklama
        self.description_label = ttk.Label(
            self,
            text="RSA, genel ve özel anahtarlar kullanarak asimetrik şifreleme sağlayan güçlü bir şifreleme algoritmasıdır.",
            wraplength=600
        )
        
        # Anahtar oluşturma
        self.key_frame = ttk.LabelFrame(self, text="Anahtar Yönetimi")
        
        self.key_size_frame = ttk.Frame(self.key_frame)
        self.key_size_label = ttk.Label(self.key_size_frame, text="Anahtar Boyutu (bit):")
        self.key_size_var = tk.IntVar(value=2048)
        self.key_size_combobox = ttk.Combobox(
            self.key_size_frame, 
            textvariable=self.key_size_var, 
            values=[1024, 2048, 3072, 4096],
            width=10,
            state="readonly"
        )
        
        self.generate_key_button = ttk.Button(
            self.key_frame, 
            text="Anahtar Oluştur", 
            command=self._generate_keys
        )
        
        self.key_info_frame = ttk.LabelFrame(self.key_frame, text="Anahtar Bilgileri")
        self.key_info_text = scrolledtext.ScrolledText(
            self.key_info_frame, 
            height=5, 
            width=50, 
            wrap=tk.WORD
        )
        
        # Giriş alanı
        self.input_frame = ttk.LabelFrame(self, text="Metin Girişi")
        self.input_text = scrolledtext.ScrolledText(
            self.input_frame, 
            height=5, 
            width=50, 
            wrap=tk.WORD
        )
        
        # Butonlar
        self.button_frame = ttk.Frame(self.input_frame)
        self.encrypt_button = ttk.Button(
            self.button_frame, 
            text="Şifrele", 
            command=self._encrypt
        )
        self.decrypt_button = ttk.Button(
            self.button_frame, 
            text="Şifre Çöz", 
            command=self._decrypt
        )
        self.clear_button = ttk.Button(
            self.button_frame, 
            text="Temizle", 
            command=self.clear
        )
        
        # Sonuç alanı
        self.result_frame = ttk.LabelFrame(self, text="Sonuç")
        self.result_text = scrolledtext.ScrolledText(
            self.result_frame, 
            height=5, 
            width=50, 
            wrap=tk.WORD
        )
        
        # Adımlar alanı
        self.steps_frame = ttk.LabelFrame(self, text="Şifreleme Adımları")
        self.steps_text = scrolledtext.ScrolledText(
            self.steps_frame, 
            height=8, 
            width=50, 
            wrap=tk.WORD
        )
    
    def _create_layout(self):
        """
        Arayüz bileşenlerini düzenler.
        """
        # Başlık ve açıklama
        self.title_label.pack(pady=(10, 5))
        self.description_label.pack(pady=(0, 10))
        
        # Anahtar oluşturma
        self.key_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        self.key_size_frame.pack(fill="x", padx=10, pady=5)
        self.key_size_label.pack(side=tk.LEFT, padx=(0, 5))
        self.key_size_combobox.pack(side=tk.LEFT)
        
        self.generate_key_button.pack(padx=10, pady=5)
        
        self.key_info_frame.pack(fill="both", expand=True, padx=10, pady=5)
        self.key_info_text.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Giriş alanı
        self.input_frame.pack(fill="both", expand=True, padx=10, pady=5)
        self.input_text.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Butonlar
        self.button_frame.pack(fill="x", padx=10, pady=5)
        self.encrypt_button.pack(side=tk.LEFT, padx=(0, 5))
        self.decrypt_button.pack(side=tk.LEFT, padx=(0, 5))
        self.clear_button.pack(side=tk.LEFT)
        
        # Sonuç alanı
        self.result_frame.pack(fill="both", expand=True, padx=10, pady=5)
        self.result_text.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Adımlar alanı
        self.steps_frame.pack(fill="both", expand=True, padx=10, pady=5)
        self.steps_text.pack(fill="both", expand=True, padx=10, pady=5)
    
    def _generate_keys(self):
        """
        RSA anahtar çiftini oluşturur ve bilgileri gösterir.
        """
        key_size = self.key_size_var.get()
        
        # RSA nesnesini yeni anahtar boyutuyla güncelle
        self.rsa_cipher = type(self.rsa_cipher)(key_size=key_size)
        
        # Anahtarları oluştur
        try:
            (public_key, private_key), steps = self.rsa_cipher.generate_keys()
            
            # Anahtar bilgilerini göster
            key_info = self.rsa_cipher.get_key_info()
            
            self.key_info_text.delete("1.0", tk.END)
            self.key_info_text.insert(tk.END, f"Genel Anahtar (Public Key):\n")
            self.key_info_text.insert(tk.END, f"  Modül (n): {key_info['public_key']['n']}\n")
            self.key_info_text.insert(tk.END, f"  Üs (e): {key_info['public_key']['e']}\n")
            self.key_info_text.insert(tk.END, f"  Boyut: {key_info['public_key']['size']} bit\n\n")
            self.key_info_text.insert(tk.END, f"Özel Anahtar (Private Key):\n")
            self.key_info_text.insert(tk.END, f"  {key_info['private_key']['note']}\n")
            
            # Adımları göster
            self._show_steps(steps)
            
            messagebox.showinfo("Başarılı", "RSA anahtar çifti başarıyla oluşturuldu.")
        except Exception as e:
            messagebox.showerror("Hata", f"Anahtar oluşturma hatası: {str(e)}")
    
    def _encrypt(self):
        """
        Metni RSA ile şifreler ve sonuçları gösterir.
        """
        text = self.input_text.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Uyarı", "Lütfen şifrelenecek bir metin girin.")
            return
        
        try:
            encrypted_text, steps = self.rsa_cipher.encrypt(text)
            
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, encrypted_text)
            
            self._show_steps(steps)
        except Exception as e:
            messagebox.showerror("Hata", f"Şifreleme hatası: {str(e)}")
    
    def _decrypt(self):
        """
        RSA ile şifrelenmiş metni çözer ve sonuçları gösterir.
        """
        text = self.result_text.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Uyarı", "Lütfen çözülecek bir şifrelenmiş metin girin.")
            return
        
        try:
            decrypted_text, steps = self.rsa_cipher.decrypt(text)
            
            # Sonucu göster
            self.input_text.delete("1.0", tk.END)
            self.input_text.insert(tk.END, decrypted_text)
            
            self._show_steps(steps)
        except Exception as e:
            messagebox.showerror("Hata", f"Şifre çözme hatası: {str(e)}")
    
    def _show_steps(self, steps):
        """
        Şifreleme veya şifre çözme adımlarını gösterir.
        
        Args:
            steps (list): Adımlar listesi
        """
        self.steps_text.delete("1.0", tk.END)
        
        for step in steps:
            self.steps_text.insert(tk.END, f"{step['step']}:\n")
            self.steps_text.insert(tk.END, f"{step['description']}\n\n")
    
    def clear(self):
        """
        Tüm alanları temizler.
        """
        self.input_text.delete("1.0", tk.END)
        self.result_text.delete("1.0", tk.END)
        self.steps_text.delete("1.0", tk.END) 