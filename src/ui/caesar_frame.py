"""
Caesar Cipher Kullanıcı Arayüzü

Bu modül, Caesar Cipher şifreleme algoritması için kullanıcı arayüzünü içerir.
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class CaesarFrame(ttk.Frame):
    def __init__(self, parent, caesar_cipher):
        """
        Caesar Cipher arayüz çerçevesini başlatır.
        
        Args:
            parent: Üst widget
            caesar_cipher (CaesarCipher): Caesar Cipher algoritma nesnesi
        """
        super().__init__(parent)
        self.caesar_cipher = caesar_cipher
        
        self._create_widgets()
        self._create_layout()
    
    def _create_widgets(self):
        """
        Arayüz bileşenlerini oluşturur.
        """
        # Başlık
        self.title_label = ttk.Label(
            self, 
            text="Caesar Cipher Şifreleme", 
            font=("Arial", 16, "bold")
        )
        
        # Açıklama
        self.description_label = ttk.Label(
            self,
            text="Caesar Cipher, her harfi alfabede belirli bir sayı kadar kaydırarak şifreleyen basit bir şifreleme yöntemidir.",
            wraplength=600
        )
        
        # Giriş alanı
        self.input_frame = ttk.LabelFrame(self, text="Metin Girişi")
        self.input_text = scrolledtext.ScrolledText(self.input_frame, height=5, width=50, wrap=tk.WORD)
        
        # Dil seçimi
        self.language_frame = ttk.Frame(self.input_frame)
        self.language_label = ttk.Label(self.language_frame, text="Dil:")
        self.language_var = tk.StringVar(value="tr")
        self.language_tr = ttk.Radiobutton(self.language_frame, text="Türkçe", variable=self.language_var, value="tr")
        self.language_en = ttk.Radiobutton(self.language_frame, text="İngilizce", variable=self.language_var, value="en")
        
        # Kaydırma miktarı
        self.shift_frame = ttk.Frame(self.input_frame)
        self.shift_label = ttk.Label(self.shift_frame, text="Kaydırma Miktarı:")
        self.shift_var = tk.IntVar(value=3)
        self.shift_spinbox = ttk.Spinbox(self.shift_frame, from_=1, to=29, textvariable=self.shift_var, width=5)
        
        # Butonlar
        self.button_frame = ttk.Frame(self.input_frame)
        self.encrypt_button = ttk.Button(self.button_frame, text="Şifrele", command=self._encrypt)
        self.decrypt_button = ttk.Button(self.button_frame, text="Şifre Çöz", command=self._decrypt)
        self.clear_button = ttk.Button(self.button_frame, text="Temizle", command=self.clear)
        self.brute_force_button = ttk.Button(self.button_frame, text="Kaba Kuvvet", command=self._brute_force)
        
        # Sonuç alanı
        self.result_frame = ttk.LabelFrame(self, text="Sonuç")
        self.result_text = scrolledtext.ScrolledText(self.result_frame, height=5, width=50, wrap=tk.WORD)
        
        # Adımlar alanı
        self.steps_frame = ttk.LabelFrame(self, text="Şifreleme Adımları")
        self.steps_text = scrolledtext.ScrolledText(self.steps_frame, height=8, width=50, wrap=tk.WORD)
        
        # Frekans analizi grafiği
        self.graph_frame = ttk.LabelFrame(self, text="Harf Frekans Analizi")
        self.figure, self.ax = plt.subplots(figsize=(8, 3))
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.graph_frame)
        self.canvas_widget = self.canvas.get_tk_widget()
    
    def _create_layout(self):
        """
        Arayüz bileşenlerini düzenler.
        """
        # Başlık ve açıklama
        self.title_label.pack(pady=(10, 5))
        self.description_label.pack(pady=(0, 10))
        
        # Giriş alanı
        self.input_frame.pack(fill="both", expand=True, padx=10, pady=5)
        self.input_text.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Dil seçimi
        self.language_frame.pack(fill="x", padx=10, pady=5)
        self.language_label.pack(side=tk.LEFT, padx=(0, 5))
        self.language_tr.pack(side=tk.LEFT, padx=(0, 5))
        self.language_en.pack(side=tk.LEFT)
        
        # Kaydırma miktarı
        self.shift_frame.pack(fill="x", padx=10, pady=5)
        self.shift_label.pack(side=tk.LEFT, padx=(0, 5))
        self.shift_spinbox.pack(side=tk.LEFT)
        
        # Butonlar
        self.button_frame.pack(fill="x", padx=10, pady=5)
        self.encrypt_button.pack(side=tk.LEFT, padx=(0, 5))
        self.decrypt_button.pack(side=tk.LEFT, padx=(0, 5))
        self.brute_force_button.pack(side=tk.LEFT, padx=(0, 5))
        self.clear_button.pack(side=tk.LEFT)
        
        # Sonuç alanı
        self.result_frame.pack(fill="both", expand=True, padx=10, pady=5)
        self.result_text.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Adımlar alanı
        self.steps_frame.pack(fill="both", expand=True, padx=10, pady=5)
        self.steps_text.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Frekans analizi grafiği
        self.graph_frame.pack(fill="both", expand=True, padx=10, pady=5)
        self.canvas_widget.pack(fill="both", expand=True)
    
    def _encrypt(self):
        """
        Metni şifreler ve sonuçları gösterir.
        """
        text = self.input_text.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Uyarı", "Lütfen şifrelenecek bir metin girin.")
            return
        
        shift = self.shift_var.get()
        language = self.language_var.get()
        
        encrypted_text, steps = self.caesar_cipher.encrypt(text, shift, language)
        
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, encrypted_text)
        
        self._show_steps(steps)
        self._show_frequency_analysis(encrypted_text, language)
    
    def _decrypt(self):
        """
        Şifrelenmiş metni çözer ve sonuçları gösterir.
        """
        text = self.input_text.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Uyarı", "Lütfen çözülecek bir metin girin.")
            return
        
        shift = self.shift_var.get()
        language = self.language_var.get()
        
        decrypted_text, steps = self.caesar_cipher.decrypt(text, shift, language)
        
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, decrypted_text)
        
        self._show_steps(steps)
        self._show_frequency_analysis(text, language)
    
    def _brute_force(self):
        """
        Kaba kuvvet yöntemiyle şifre çözmeyi dener.
        """
        text = self.input_text.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Uyarı", "Lütfen çözülecek bir metin girin.")
            return
        
        language = self.language_var.get()
        
        possible_solutions = self.caesar_cipher.brute_force(text, language)
        
        # Sonuçları göster
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, "Olası Çözümler:\n\n")
        
        for solution in possible_solutions:
            self.result_text.insert(tk.END, f"Kaydırma: {solution['shift']}\n")
            self.result_text.insert(tk.END, f"Metin: {solution['text']}\n\n")
        
        # Adımları temizle
        self.steps_text.delete("1.0", tk.END)
        self.steps_text.insert(tk.END, "Kaba kuvvet yöntemi, tüm olası kaydırma değerlerini deneyerek şifreyi çözmeye çalışır.")
        
        # Frekans analizi göster
        self._show_frequency_analysis(text, language)
    
    def _show_steps(self, steps):
        """
        Şifreleme veya şifre çözme adımlarını gösterir.
        
        Args:
            steps (list): Adımlar listesi
        """
        self.steps_text.delete("1.0", tk.END)
        
        for i, step in enumerate(steps):
            if i > 20:  # Sadece ilk 20 adımı göster
                self.steps_text.insert(tk.END, "...\n")
                break
            
            original_char = step["original_char"]
            encrypted_char = step["encrypted_char"]
            
            if "note" in step:
                self.steps_text.insert(tk.END, f"'{original_char}' -> '{encrypted_char}': {step['note']}\n")
            else:
                original_index = step["original_index"]
                new_index = step["new_index"]
                self.steps_text.insert(tk.END, f"'{original_char}' (indeks: {original_index}) -> '{encrypted_char}' (indeks: {new_index})\n")
    
    def _show_frequency_analysis(self, text, language):
        """
        Metin için harf frekans analizi grafiğini gösterir.
        
        Args:
            text (str): Analiz edilecek metin
            language (str): Dil ('tr' veya 'en')
        """
        frequency = self.caesar_cipher.frequency_analysis(text, language)
        
        # Grafiği temizle
        self.ax.clear()
        
        # Verileri hazırla
        chars = list(frequency.keys())
        freqs = list(frequency.values())
        
        # Grafiği çiz
        bars = self.ax.bar(chars, freqs, color='skyblue')
        
        # En yüksek frekansa sahip harfi vurgula
        if freqs:
            max_index = freqs.index(max(freqs))
            bars[max_index].set_color('red')
        
        # Grafiği düzenle
        self.ax.set_title("Harf Frekans Analizi")
        self.ax.set_xlabel("Harfler")
        self.ax.set_ylabel("Frekans (%)")
        
        # Grafiği güncelle
        self.canvas.draw()
    
    def clear(self):
        """
        Tüm alanları temizler.
        """
        self.input_text.delete("1.0", tk.END)
        self.result_text.delete("1.0", tk.END)
        self.steps_text.delete("1.0", tk.END)
        self.ax.clear()
        self.canvas.draw() 