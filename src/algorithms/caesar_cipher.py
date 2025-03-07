"""
Caesar Cipher Algoritması

Bu modül, Caesar Cipher şifreleme ve şifre çözme işlemlerini gerçekleştirir.
Caesar Cipher, her harfi alfabede belirli bir sayı kadar kaydırarak şifreleyen 
basit bir şifreleme yöntemidir.
"""

class CaesarCipher:
    def __init__(self):
        # Türkçe alfabesi (büyük ve küçük harfler)
        self.alphabet_tr = 'ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZabcçdefgğhıijklmnoöprsştuüvyz'
        # İngilizce alfabesi (büyük ve küçük harfler)
        self.alphabet_en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        
    def encrypt(self, text, shift, language='tr'):
        """
        Metni Caesar Cipher algoritması ile şifreler.
        
        Args:
            text (str): Şifrelenecek metin
            shift (int): Kaydırma miktarı
            language (str): Kullanılacak dil ('tr' veya 'en')
            
        Returns:
            str: Şifrelenmiş metin
            list: Şifreleme adımları
        """
        encrypted_text = ""
        steps = []
        
        # Kullanılacak alfabeyi belirle
        alphabet = self.alphabet_tr if language == 'tr' else self.alphabet_en
        alphabet_length = len(alphabet)
        
        for char in text:
            step = {}
            step["original_char"] = char
            
            if char in alphabet:
                # Karakterin alfabedeki indeksini bul
                index = alphabet.find(char)
                step["original_index"] = index
                
                # Yeni indeksi hesapla (kaydırma uygulayarak)
                new_index = (index + shift) % alphabet_length
                step["new_index"] = new_index
                
                # Yeni karakteri al
                encrypted_char = alphabet[new_index]
                step["encrypted_char"] = encrypted_char
                
                encrypted_text += encrypted_char
            else:
                # Alfabede olmayan karakterleri olduğu gibi bırak
                encrypted_text += char
                step["encrypted_char"] = char
                step["note"] = "Karakter alfabede bulunmadığı için değiştirilmedi"
            
            steps.append(step)
        
        return encrypted_text, steps
    
    def decrypt(self, encrypted_text, shift, language='tr'):
        """
        Caesar Cipher ile şifrelenmiş metni çözer.
        
        Args:
            encrypted_text (str): Şifrelenmiş metin
            shift (int): Kaydırma miktarı
            language (str): Kullanılacak dil ('tr' veya 'en')
            
        Returns:
            str: Çözülmüş metin
            list: Çözme adımları
        """
        # Şifre çözme, ters yönde kaydırma yapmaktır
        return self.encrypt(encrypted_text, -shift, language)
    
    def brute_force(self, encrypted_text, language='tr'):
        """
        Caesar Cipher ile şifrelenmiş metni kaba kuvvet yöntemiyle çözmeye çalışır.
        
        Args:
            encrypted_text (str): Şifrelenmiş metin
            language (str): Kullanılacak dil ('tr' veya 'en')
            
        Returns:
            list: Tüm olası çözümler
        """
        alphabet = self.alphabet_tr if language == 'tr' else self.alphabet_en
        alphabet_length = len(alphabet) // 2  # Sadece büyük veya küçük harf sayısı
        
        possible_solutions = []
        
        for shift in range(1, alphabet_length + 1):
            decrypted_text, _ = self.decrypt(encrypted_text, shift, language)
            possible_solutions.append({
                "shift": shift,
                "text": decrypted_text
            })
        
        return possible_solutions
    
    def frequency_analysis(self, encrypted_text, language='tr'):
        """
        Şifrelenmiş metinde harf frekansı analizi yapar.
        
        Args:
            encrypted_text (str): Şifrelenmiş metin
            language (str): Kullanılacak dil ('tr' veya 'en')
            
        Returns:
            dict: Harf frekansları
        """
        alphabet = self.alphabet_tr if language == 'tr' else self.alphabet_en
        
        # Sadece küçük harfleri al
        lower_alphabet = alphabet[len(alphabet)//2:]
        
        frequency = {char: 0 for char in lower_alphabet}
        total_chars = 0
        
        for char in encrypted_text.lower():
            if char in lower_alphabet:
                frequency[char] += 1
                total_chars += 1
        
        # Yüzdelik hesapla
        if total_chars > 0:
            for char in frequency:
                frequency[char] = (frequency[char] / total_chars) * 100
        
        return frequency 