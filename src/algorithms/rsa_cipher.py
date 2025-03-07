"""
RSA Şifreleme Algoritması

Bu modül, RSA şifreleme ve şifre çözme işlemlerini gerçekleştirir.
RSA, genel ve özel anahtarlar kullanarak asimetrik şifreleme sağlayan
güçlü bir şifreleme algoritmasıdır.
"""

import rsa
import base64

class RSACipher:
    def __init__(self, key_size=2048):
        """
        RSA şifreleme sınıfını başlatır.
        
        Args:
            key_size (int): Anahtar bit uzunluğu (varsayılan: 2048)
        """
        self.key_size = key_size
        self.public_key = None
        self.private_key = None
        
    def generate_keys(self):
        """
        RSA genel ve özel anahtar çiftini oluşturur.
        
        Returns:
            tuple: (public_key, private_key) anahtar çifti
            dict: Anahtar oluşturma adımları
        """
        steps = []
        
        # Adım 1: İki büyük asal sayı seçimi (kütüphane tarafından yapılır)
        steps.append({
            "step": "İki büyük asal sayı seçimi",
            "description": "RSA algoritması iki büyük asal sayı (p ve q) seçerek başlar. Bu sayılar gizli tutulur."
        })
        
        # Adım 2: n = p * q hesaplanması
        steps.append({
            "step": "Modül hesaplama",
            "description": "n = p * q hesaplanır. Bu değer hem genel hem de özel anahtarda kullanılır."
        })
        
        # Adım 3: Euler's totient function hesaplanması
        steps.append({
            "step": "Euler's totient function hesaplama",
            "description": "φ(n) = (p-1) * (q-1) hesaplanır."
        })
        
        # Adım 4: Genel anahtar e seçimi
        steps.append({
            "step": "Genel anahtar e seçimi",
            "description": "e değeri, 1 < e < φ(n) aralığında ve φ(n) ile aralarında asal olan bir sayı olarak seçilir."
        })
        
        # Adım 5: Özel anahtar d hesaplanması
        steps.append({
            "step": "Özel anahtar d hesaplama",
            "description": "d değeri, (d * e) % φ(n) = 1 eşitliğini sağlayan sayı olarak hesaplanır."
        })
        
        # Adım 6: Anahtar çiftinin oluşturulması
        steps.append({
            "step": "Anahtar çiftinin oluşturulması",
            "description": "Genel anahtar (n, e) ve özel anahtar (n, d) olarak oluşturulur."
        })
        
        # Anahtarları oluştur
        (self.public_key, self.private_key) = rsa.newkeys(self.key_size)
        
        return (self.public_key, self.private_key), steps
    
    def encrypt(self, message):
        """
        Metni RSA algoritması ile şifreler.
        
        Args:
            message (str): Şifrelenecek metin
            
        Returns:
            str: Base64 ile kodlanmış şifrelenmiş metin
            list: Şifreleme adımları
        """
        if self.public_key is None:
            self.generate_keys()
        
        steps = []
        
        # Adım 1: Mesajı byte'lara dönüştürme
        steps.append({
            "step": "Mesajı byte'lara dönüştürme",
            "description": "Metin, byte dizisine dönüştürülür."
        })
        
        # Adım 2: RSA şifreleme
        steps.append({
            "step": "RSA şifreleme",
            "description": "Her bir byte için c = m^e mod n formülü uygulanır."
        })
        
        # Adım 3: Base64 kodlama
        steps.append({
            "step": "Base64 kodlama",
            "description": "Şifrelenmiş veri, Base64 formatına dönüştürülür."
        })
        
        # Şifreleme işlemi
        encrypted_message = rsa.encrypt(message.encode('utf-8'), self.public_key)
        
        # Base64 kodlama
        encoded_message = base64.b64encode(encrypted_message).decode('utf-8')
        
        return encoded_message, steps
    
    def decrypt(self, encrypted_message):
        """
        RSA ile şifrelenmiş metni çözer.
        
        Args:
            encrypted_message (str): Base64 ile kodlanmış şifrelenmiş metin
            
        Returns:
            str: Çözülmüş metin
            list: Çözme adımları
        """
        if self.private_key is None:
            raise ValueError("Şifre çözme için özel anahtar gereklidir.")
        
        steps = []
        
        # Adım 1: Base64 çözme
        steps.append({
            "step": "Base64 çözme",
            "description": "Şifrelenmiş metin, Base64 formatından çözülür."
        })
        
        # Adım 2: RSA şifre çözme
        steps.append({
            "step": "RSA şifre çözme",
            "description": "Her bir şifrelenmiş byte için m = c^d mod n formülü uygulanır."
        })
        
        # Adım 3: Byte'ları metne dönüştürme
        steps.append({
            "step": "Byte'ları metne dönüştürme",
            "description": "Çözülmüş byte dizisi, metne dönüştürülür."
        })
        
        try:
            # Base64 çözme
            decoded_message = base64.b64decode(encrypted_message)
            
            # Şifre çözme
            decrypted_message = rsa.decrypt(decoded_message, self.private_key).decode('utf-8')
            
            return decrypted_message, steps
        except Exception as e:
            return f"Şifre çözme hatası: {str(e)}", steps
    
    def get_key_info(self):
        """
        Anahtar bilgilerini döndürür.
        
        Returns:
            dict: Anahtar bilgileri
        """
        if self.public_key is None or self.private_key is None:
            return {"error": "Anahtarlar henüz oluşturulmamış."}
        
        return {
            "public_key": {
                "n": self.public_key.n,
                "e": self.public_key.e,
                "size": self.key_size
            },
            "private_key": {
                "size": self.key_size,
                "note": "Özel anahtar bilgileri güvenlik nedeniyle gösterilmiyor."
            }
        } 