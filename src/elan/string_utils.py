import os
import json
import urllib.request
import random
import re
import requests
from difflib import get_close_matches
from collections import Counter

class string_utils:
    def __init__(self):
        """Metin işleme yardımcıları sınıfı"""
        # Kelime havuzlarını yükle
        self.words = {
            "tr": self._load_turkish_words(),
            "en": self._load_english_words()
        }
        # Dil algılama için karakter setleri
        self.tr_chars = set('çğıöşüÇĞİÖŞÜ')
        
    def _load_turkish_words(self):
        """Türkçe kelime havuzunu yükle"""
        try:
            # Lokal JSON dosyasını kontrol et
            words_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
            os.makedirs(words_dir, exist_ok=True)
            words_file = os.path.join(words_dir, 'turkish_words.json')
            
            # Dosya varsa, kelime havuzunu yükle
            if os.path.exists(words_file):
                with open(words_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            
            # Dosya yoksa, temel kelime havuzunu oluştur ve indirmeyi dene
            basic_words = [
                # Temel kelimeler
                "merhaba", "selam", "nasıl", "nasılsın", "iyiyim", "teşekkür", "günaydın", 
                "iyi", "kötü", "evet", "hayır", "belki", "lütfen", "tamam", "olur",
                "ben", "sen", "o", "biz", "siz", "onlar", "bu", "şu", "kim", "ne",
                "nerede", "ne zaman", "nasıl", "neden", "çünkü", "hangi", "kaç",
                "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz", "on",
                "gün", "hafta", "ay", "yıl", "zaman", "saat", "dakika", "saniye",
                "güneş", "ay", "yıldız", "dünya", "su", "hava", "ateş", "toprak",
                "ev", "okul", "iş", "araba", "telefon", "bilgisayar", "kitap", "kalem",
                "masa", "sandalye", "kapı", "pencere", "duvar", "tavan", "zemin",
                "anne", "baba", "kardeş", "abla", "ağabey", "aile", "çocuk", "bebek",
                "kedi", "köpek", "kuş", "balık", "at", "inek", "tavuk", "koyun",
                "elma", "armut", "muz", "portakal", "üzüm", "çilek", "kiraz", "karpuz",
                "ekmek", "süt", "su", "çay", "kahve", "peynir", "et", "tavuk", "balık",
                "sabah", "öğle", "akşam", "gece", "dün", "bugün", "yarın",
                "güzel", "çirkin", "büyük", "küçük", "uzun", "kısa", "kalın", "ince",
                "sıcak", "soğuk", "sert", "yumuşak", "kolay", "zor", "hızlı", "yavaş",
                "gelmek", "gitmek", "almak", "vermek", "yapmak", "etmek", "söylemek", "konuşmak",
                "görmek", "duymak", "anlamak", "bilmek", "sevmek", "istemek", "düşünmek",
                "yemek", "içmek", "uyumak", "kalkmak", "oturmak", "koşmak", "yürümek",
                "izlemek", "dinlemek", "okumak", "yazmak", "çizmek", "boyamak",
                "ve", "veya", "ama", "fakat", "çünkü", "eğer", "için", "ile", "gibi",
                "üstünde", "altında", "içinde", "dışında", "önünde", "arkasında", "yanında",
                "istanbul", "ankara", "izmir", "bursa", "antalya", "konya", "adana", "türkiye",
                "pazartesi", "salı", "çarşamba", "perşembe", "cuma", "cumartesi", "pazar",
                "ocak", "şubat", "mart", "nisan", "mayıs", "haziran", "temmuz", "ağustos", "eylül", "ekim", "kasım", "aralık",
                "renk", "kırmızı", "mavi", "yeşil", "sarı", "siyah", "beyaz", "mor", "turuncu", "pembe", "gri",
                "para", "zaman", "sevgi", "mutluluk", "üzüntü", "korku", "öfke", "şaşkınlık"
            ]
            
            # İnternet bağlantısı ile daha fazla kelime indirmeyi dene
            try:
                downloaded_words = self._download_turkish_words()
                if downloaded_words:
                    # Kelime havuzunu birleştir
                    all_words = list(set(basic_words + downloaded_words))
                    # Kelime havuzunu kaydet
                    with open(words_file, 'w', encoding='utf-8') as f:
                        json.dump(all_words, f, ensure_ascii=False, indent=2)
                    return all_words
            except Exception as e:
                print(f"Türkçe kelime indirme hatası: {e}")
            
            # İndirilemezse temel kelime havuzunu kaydet ve kullan
            with open(words_file, 'w', encoding='utf-8') as f:
                json.dump(basic_words, f, ensure_ascii=False, indent=2)
            return basic_words
            
        except Exception as e:
            print(f"Türkçe kelime havuzu yükleme hatası: {e}")
            # Hata durumunda minimal kelime listesi döndür
            return ["merhaba", "nasılsın", "evet", "hayır", "teşekkür"]
    
    def _load_english_words(self):
        """İngilizce kelime havuzunu yükle"""
        try:
            # Lokal JSON dosyasını kontrol et
            words_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
            os.makedirs(words_dir, exist_ok=True)
            words_file = os.path.join(words_dir, 'english_words.json')
            
            # Dosya varsa, kelime havuzunu yükle
            if os.path.exists(words_file):
                with open(words_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            
            # Dosya yoksa, temel kelime havuzunu oluştur ve indirmeyi dene
            basic_words = [
                # Temel kelimeler
                "hello", "hi", "how", "are", "you", "fine", "thank", "thanks", "good", "morning",
                "I", "you", "he", "she", "it", "we", "they", "this", "that", "who", "what",
                "where", "when", "why", "because", "which", "how", "many",
                "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
                "day", "week", "month", "year", "time", "hour", "minute", "second",
                "sun", "moon", "star", "earth", "water", "air", "fire", "land",
                "house", "school", "work", "car", "phone", "computer", "book", "pen",
                "table", "chair", "door", "window", "wall", "ceiling", "floor",
                "mother", "father", "brother", "sister", "family", "child", "baby",
                "cat", "dog", "bird", "fish", "horse", "cow", "chicken", "sheep",
                "apple", "pear", "banana", "orange", "grape", "strawberry", "cherry", "watermelon",
                "bread", "milk", "water", "tea", "coffee", "cheese", "meat", "chicken", "fish",
                "morning", "noon", "evening", "night", "yesterday", "today", "tomorrow",
                "beautiful", "ugly", "big", "small", "long", "short", "thick", "thin",
                "hot", "cold", "hard", "soft", "easy", "difficult", "fast", "slow",
                "come", "go", "take", "give", "do", "make", "say", "speak",
                "see", "hear", "understand", "know", "love", "want", "think",
                "eat", "drink", "sleep", "wake", "sit", "run", "walk",
                "watch", "listen", "read", "write", "draw", "paint",
                "and", "or", "but", "because", "if", "for", "with", "like",
                "on", "under", "in", "out", "front", "back", "beside",
                "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday",
                "january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december",
                "color", "red", "blue", "green", "yellow", "black", "white", "purple", "orange", "pink", "grey",
                "money", "time", "love", "happiness", "sadness", "fear", "anger", "surprise"
            ]
            
            # İnternet bağlantısı ile daha fazla kelime indirmeyi dene
            try:
                downloaded_words = self._download_english_words()
                if downloaded_words:
                    # Kelime havuzunu birleştir
                    all_words = list(set(basic_words + downloaded_words))
                    # Kelime havuzunu kaydet
                    with open(words_file, 'w', encoding='utf-8') as f:
                        json.dump(all_words, f, ensure_ascii=False, indent=2)
                    return all_words
            except Exception as e:
                print(f"İngilizce kelime indirme hatası: {e}")
            
            # İndirilemezse temel kelime havuzunu kaydet ve kullan
            with open(words_file, 'w', encoding='utf-8') as f:
                json.dump(basic_words, f, ensure_ascii=False, indent=2)
            return basic_words
            
        except Exception as e:
            print(f"İngilizce kelime havuzu yükleme hatası: {e}")
            # Hata durumunda minimal kelime listesi döndür
            return ["hello", "how", "are", "you", "yes", "no", "thank"]
            
    def _download_turkish_words(self):
        """İnternetten Türkçe kelime havuzu indir"""
        try:
            # Güvenilir kaynaklardan kelime listeleri
            sources = [
                "https://raw.githubusercontent.com/mertemin/turkish-word-list/master/words.txt",
                "https://raw.githubusercontent.com/otuncelli/turkish-stemmer-python/master/TurkishStemmer/resources/words_tr.txt",
                "https://raw.githubusercontent.com/apie/tr-words/main/words.txt"
            ]
            
            all_words = []
            success = False
            
            for source in sources:
                try:
                    print(f"Türkçe kelime kaynağı deneniyor: {source}")
                    response = requests.get(source, timeout=10)
                    if response.status_code == 200:
                        # Kaynak formatına göre kelime çıkarma
                        if source.endswith('.json'):
                            data = response.json()
                            if isinstance(data, list):
                                words = data
                            elif isinstance(data, dict) and 'words' in data:
                                words = data['words']
                            else:
                                words = []
                        else:
                            # Metin dosyaları için basit bir işleme
                            text = response.text
                            lines = text.splitlines()
                            words = [line.strip() for line in lines if line.strip()]
                        
                        # Boş olmayan ve en az 2 karakter olan kelimeleri ekle
                        words = [word for word in words if word and len(word) >= 2]
                        all_words.extend(words)
                        success = True
                        print(f"{len(words)} kelime başarıyla indirildi.")
                    else:
                        print(f"Kaynak erişim hatası: HTTP {response.status_code}")
                except Exception as e:
                    print(f"Kaynak indirme hatası: {e}")
                    continue
            
            # Yedek plan: Web API'ler ile kelime listeleri oluşturma
            if not success:
                try:
                    print("Alternatif yöntem deneniyor: Web API")
                    # Wiktionary API üzerinden Türkçe kelimeleri alma
                    api_url = "https://tr.wiktionary.org/w/api.php"
                    params = {
                        "action": "query",
                        "list": "categorymembers",
                        "cmtitle": "Kategori:Türkçe_sözcükler",
                        "cmlimit": "500",
                        "format": "json"
                    }
                    response = requests.get(api_url, params=params, timeout=15)
                    if response.status_code == 200:
                        data = response.json()
                        if 'query' in data and 'categorymembers' in data['query']:
                            words = [item['title'] for item in data['query']['categorymembers']]
                            all_words.extend(words)
                            success = True
                            print(f"{len(words)} kelime başarıyla API'den alındı.")
                except Exception as e:
                    print(f"API hata: {e}")
            
            # Kelimeleri temizle ve benzersizleştir
            all_words = list(set([w.lower() for w in all_words if w and isinstance(w, str) and len(w) >= 2]))
            
            print(f"Toplam {len(all_words)} benzersiz Türkçe kelime indirildi.")
            return all_words
        
        except Exception as e:
            print(f"Türkçe kelime indirme genel hatası: {e}")
            return []
    
    def _download_english_words(self):
        """İnternetten İngilizce kelime havuzu indir"""
        try:
            # Güvenilir kaynaklardan kelime listeleri
            sources = [
                "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt",
                "https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english.txt"
            ]
            
            all_words = []
            success = False
            
            for source in sources:
                try:
                    print(f"İngilizce kelime kaynağı deneniyor: {source}")
                    response = requests.get(source, timeout=10)
                    if response.status_code == 200:
                        # Metin dosyaları için basit bir işleme
                        text = response.text
                        lines = text.splitlines()
                        words = [line.strip() for line in lines if line.strip()]
                        
                        # Boş olmayan ve en az 2 karakter olan kelimeleri ekle
                        words = [word for word in words if word and len(word) >= 2]
                        all_words.extend(words)
                        success = True
                        print(f"{len(words)} kelime başarıyla indirildi.")
                    else:
                        print(f"Kaynak erişim hatası: HTTP {response.status_code}")
                except Exception as e:
                    print(f"Kaynak indirme hatası: {e}")
                    continue
            
            # Yedek plan: API ile kelime listeleri oluşturma
            if not success:
                try:
                    print("Alternatif yöntem deneniyor: Web API")
                    # WordsAPI veya benzer bir API üzerinden İngilizce kelimeleri alma
                    api_url = "https://wordsapiv1.p.rapidapi.com/words/"
                    # Örnek olarak, belirli bir kategori veya özelliğe sahip kelime listeleri alınabilir
                    # Not: Bu gerçek bir API kullanımı için yalnızca bir örnektir
                    # Gerçek kullanım için API anahtarı ve doğru parametreler gerekebilir
                    response = requests.get(
                        api_url, 
                        headers={
                            "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com",
                            # API anahtarı gerçek bir anahtar ile değiştirilmelidir
                            "X-RapidAPI-Key": "YOUR_API_KEY"  
                        },
                        timeout=15
                    )
                    # API yanıtını işleme - bu örnekte yapılmıyor
                except Exception as e:
                    print(f"API hata: {e}")
            
            # Alternatif 2: API gerekmeden yaygın İngilizce kelimeler
            if not success:
                # En yaygın 1000 İngilizce kelimeden oluşan bir liste
                common_english = [
                    "the", "be", "to", "of", "and", "a", "in", "that", "have", "I", 
                    "it", "for", "not", "on", "with", "he", "as", "you", "do", "at", 
                    "this", "but", "his", "by", "from", "they", "we", "say", "her", "she", 
                    "or", "an", "will", "my", "one", "all", "would", "there", "their", "what", 
                    "so", "up", "out", "if", "about", "who", "get", "which", "go", "me",
                    "when", "make", "can", "like", "time", "no", "just", "him", "know", "take", 
                    "people", "into", "year", "your", "good", "some", "could", "them", "see", "other", 
                    "than", "then", "now", "look", "only", "come", "its", "over", "think", "also", 
                    "back", "after", "use", "two", "how", "our", "work", "first", "well", "way", 
                    "even", "new", "want", "because", "any", "these", "give", "day", "most", "us"
                ]
                all_words.extend(common_english)
                success = True
                print(f"{len(common_english)} yaygın İngilizce kelime eklendi.")
            
            # Kelimeleri temizle ve benzersizleştir
            all_words = list(set([w.lower() for w in all_words if w and isinstance(w, str) and len(w) >= 2]))
            
            print(f"Toplam {len(all_words)} benzersiz İngilizce kelime indirildi.")
            return all_words
        
        except Exception as e:
            print(f"İngilizce kelime indirme genel hatası: {e}")
            return []
            
    def update_word_database(self, language=None, force=False):
        """Kelime havuzunu internetten güncelle
        
        Args:
            language (str, optional): Güncelleme yapılacak dil (tr/en). None ise tüm diller güncellenir.
            force (bool, optional): True ise mevcut dosyalar olsa bile güncelleme yapar.
            
        Returns:
            bool: Güncelleme başarılı ise True, değilse False
        """
        try:
            success = True
            
            # Türkçe kelime havuzunu güncelle
            if language is None or language == "tr":
                # Kelime havuzu dizini
                words_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
                os.makedirs(words_dir, exist_ok=True)
                words_file = os.path.join(words_dir, 'turkish_words.json')
                
                # Zorla güncelleme veya dosya yoksa
                if force or not os.path.exists(words_file):
                    print("Türkçe kelime havuzu güncelleniyor...")
                    tr_words = self._download_turkish_words()
                    if tr_words:
                        # Mevcut kelimelerle birleştir
                        if not force and "tr" in self.words:
                            tr_words = list(set(self.words["tr"] + tr_words))
                        # Kelime havuzunu kaydet
                        with open(words_file, 'w', encoding='utf-8') as f:
                            json.dump(tr_words, f, ensure_ascii=False, indent=2)
                        # Hafızadaki kelime havuzunu güncelle
                        self.words["tr"] = tr_words
                        print(f"Türkçe kelime havuzu güncellendi. Toplam {len(tr_words)} kelime.")
                    else:
                        print("Türkçe kelime havuzu güncellenemedi.")
                        success = False
            
            # İngilizce kelime havuzunu güncelle
            if language is None or language == "en":
                # Kelime havuzu dizini
                words_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
                os.makedirs(words_dir, exist_ok=True)
                words_file = os.path.join(words_dir, 'english_words.json')
                
                # Zorla güncelleme veya dosya yoksa
                if force or not os.path.exists(words_file):
                    print("İngilizce kelime havuzu güncelleniyor...")
                    en_words = self._download_english_words()
                    if en_words:
                        # Mevcut kelimelerle birleştir
                        if not force and "en" in self.words:
                            en_words = list(set(self.words["en"] + en_words))
                        # Kelime havuzunu kaydet
                        with open(words_file, 'w', encoding='utf-8') as f:
                            json.dump(en_words, f, ensure_ascii=False, indent=2)
                        # Hafızadaki kelime havuzunu güncelle
                        self.words["en"] = en_words
                        print(f"İngilizce kelime havuzu güncellendi. Toplam {len(en_words)} kelime.")
                    else:
                        print("İngilizce kelime havuzu güncellenemedi.")
                        success = False
            
            return success
        
        except Exception as e:
            print(f"Kelime havuzu güncelleme hatası: {e}")
            return False
                
    def add_custom_words(self, words, language):
        """Kelime havuzuna özel kelimeler ekle
        
        Args:
            words (list): Eklenecek kelimeler listesi
            language (str): Dil (tr/en)
            
        Returns:
            int: Eklenen benzersiz kelime sayısı
        """
        if language not in ["tr", "en"]:
            raise ValueError("Desteklenmeyen dil. 'tr' veya 'en' kullanın.")
            
        if not isinstance(words, list):
            raise ValueError("Kelimeler bir liste olarak verilmelidir.")
            
        # Boş olmayan ve string olan kelimeleri filtrele
        valid_words = [w.lower() for w in words if w and isinstance(w, str)]
        
        # Benzersiz yeni kelimeleri ekle
        initial_count = len(self.words[language])
        self.words[language] = list(set(self.words[language] + valid_words))
        
        # Kelime havuzunu kaydet
        try:
            words_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
            os.makedirs(words_dir, exist_ok=True)
            
            filename = 'turkish_words.json' if language == 'tr' else 'english_words.json'
            words_file = os.path.join(words_dir, filename)
            
            with open(words_file, 'w', encoding='utf-8') as f:
                json.dump(self.words[language], f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Kelime kaydetme hatası: {e}")
        
        # Eklenen benzersiz kelime sayısını döndür
        return len(self.words[language]) - initial_count
    
    def detect_language(self, text):
        """Metnin dilini tespit et
        
        Args:
            text (str): Dili tespit edilecek metin
            
        Returns:
            str: Tespit edilen dil kodu (tr/en)
        """
        if not text:
            return "en"  # Varsayılan olarak İngilizce
        
        # Türkçe karakterleri kontrol et
        text_chars = set(text.lower())
        if any(char in self.tr_chars for char in text_chars):
            return "tr"
        
        # Kelime bazlı dil tespiti
        words = re.findall(r'\b\w+\b', text.lower())
        tr_count = 0
        en_count = 0
        
        for word in words:
            if word in self.words["tr"]:
                tr_count += 1
            if word in self.words["en"]:
                en_count += 1
        
        # Dil oranlarını hesapla
        if tr_count > en_count:
            return "tr"
        else:
            return "en"
    
    def suggest_correction(self, word, language=None, max_suggestions=1):
        """Yanlış yazılan kelime için düzeltme önerileri sunma
        
        Args:
            word (str): Düzeltilecek kelime
            language (str, optional): Dil kodu (tr/en). None ise otomatik tespit edilir.
            max_suggestions (int, optional): Maksimum öneri sayısı
            
        Returns:
            list: Önerilen kelimeler listesi
        """
        if not word:
            return []
        
        # Küçük harfe çevir
        word = word.lower()
        
        # Kelime zaten doğruysa kendisini döndür
        if language is None:
            language = self.detect_language(word)
        
        if word in self.words[language]:
            return [word]
        
        # En yakın kelimeleri bul
        suggestions = get_close_matches(word, self.words[language], n=max_suggestions, cutoff=0.6)
        
        # Öneri yoksa Levenshtein mesafesine göre en yakın kelimeleri bul
        if not suggestions:
            word_scores = []
            for dict_word in self.words[language]:
                if abs(len(dict_word) - len(word)) <= 2:  # Uzunluk farkı en fazla 2 karakter
                    # Basit bir Levenshtein mesafesi yaklaşımı
                    score = 0
                    for c1, c2 in zip(word, dict_word):
                        if c1 == c2:
                            score += 1
                    word_scores.append((dict_word, score))
            
            # Skorlara göre sırala ve en yüksek skorlu kelimeleri al
            word_scores.sort(key=lambda x: x[1], reverse=True)
            suggestions = [w[0] for w in word_scores[:max_suggestions]]
        
        return suggestions
    
    def correct_text(self, text, language=None):
        """Metindeki yanlış yazılan kelimeleri düzelt
        
        Args:
            text (str): Düzeltilecek metin
            language (str, optional): Dil kodu (tr/en). None ise otomatik tespit edilir.
            
        Returns:
            str: Düzeltilmiş metin
        """
        if not text:
            return ""
        
        # Dil tespiti
        if language is None:
            language = self.detect_language(text)
        
        # Metni kelimelere ayır
        words = re.findall(r'\b\w+\b', text)
        word_map = {}
        
        # Her kelime için düzeltme öner
        for word in words:
            if word.lower() not in self.words[language] and word.lower() not in word_map:
                suggestions = self.suggest_correction(word, language)
                if suggestions:
                    word_map[word.lower()] = suggestions[0]
        
        # Metin içindeki kelimeleri düzelt
        corrected_text = text
        for wrong, correct in word_map.items():
            # Kelime sınırları ve büyük/küçük harf eşleşmesi için regex kullan
            pattern = r'\b' + re.escape(wrong) + r'\b'
            corrected_text = re.sub(pattern, correct, corrected_text, flags=re.IGNORECASE)
        
        return corrected_text

if __name__ == "__main__":
    string_utils()
    
    
