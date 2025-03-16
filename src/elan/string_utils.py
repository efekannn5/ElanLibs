import os
import json
import urllib.request

class string_utils:
    def __init__(self):
        # Kelime havuzları
        self.words = {
            "tr": self._load_turkish_words(),
            "en": self._load_english_words()
        }
        
    def _load_turkish_words(self):
        """Türkçe kelime havuzunu yükler"""
        # Temel Türkçe kelimeler
        base_turkish_words = [
            "merhaba", "selam", "nasılsın", "iyiyim", "teşekkürler", "tamam", "günaydın", "iyi", "kötü",
            "bugün", "yarın", "dün", "akşam", "sabah", "öğle", "gece", "okul", "ev", "araba", "kitap",
            "kalem", "defter", "bilgisayar", "telefon", "internet", "yazılım", "program", "kod", "python",
            "java", "javascript", "web", "site", "sayfa", "doküman", "dosya", "klasör", "resim", "video",
            "ses", "müzik", "film", "dizi", "oyun", "yemek", "su", "çay", "kahve", "ekmek", "peynir",
            "zeytin", "yumurta", "gelmek", "gitmek", "yapmak", "etmek", "olmak", "vermek", "almak", 
            "görmek", "duymak", "konuşmak", "söylemek", "anlamak", "bilmek", "sevmek", "istemek",
            "hayır", "evet", "belki", "anne", "baba", "kardeş", "arkadaş", "öğretmen", "öğrenci",
            "türkiye", "istanbul", "ankara", "izmir", "antalya", "bursa", "adana", "samsun", "konya",
            "hava", "deniz", "göl", "nehir", "dağ", "orman", "çiçek", "ağaç", "gül", "papatya",
            "kedi", "köpek", "kuş", "balık", "aslan", "kaplan", "fil", "zürafa", "maymun",
            "siyah", "beyaz", "kırmızı", "mavi", "yeşil", "sarı", "mor", "pembe", "turuncu", "kahverengi",
            "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz", "on"
        ]
        
        # Genişletilmiş Türkçe kelime havuzunu yukle
        try:
            # Yerel dosyadan yüklemeyi dene
            words_file = os.path.join(os.path.dirname(__file__), 'words_tr.json')
            if os.path.exists(words_file):
                with open(words_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            else:
                # İlk kullanımda internetten yükle ve kaydet
                return self._download_turkish_words(base_turkish_words)
        except Exception as e:
            print(f"Türkçe kelime havuzu yüklenirken hata: {e}")
            return base_turkish_words
    
    def _load_english_words(self):
        """İngilizce kelime havuzunu yükler"""
        # Temel İngilizce kelimeler
        base_english_words = [
            "hello", "hi", "how", "are", "you", "good", "thanks", "thank", "morning", "afternoon",
            "evening", "night", "school", "house", "car", "book", "pen", "computer", "phone", "internet",
            "software", "program", "code", "python", "java", "javascript", "web", "site", "page", "document",
            "file", "folder", "image", "video", "sound", "music", "movie", "game", "food", "water",
            "tea", "coffee", "bread", "cheese", "egg", "come", "go", "make", "do", "be", "give", "take",
            "see", "hear", "speak", "say", "understand", "know", "love", "want", "no", "yes", "maybe",
            "mother", "father", "brother", "sister", "friend", "teacher", "student", "england", "london",
            "weather", "sea", "lake", "river", "mountain", "forest", "flower", "tree", "rose", "cat",
            "dog", "bird", "fish", "lion", "tiger", "elephant", "giraffe", "monkey", "black", "white",
            "red", "blue", "green", "yellow", "purple", "pink", "orange", "brown", "one", "two", "three",
            "four", "five", "six", "seven", "eight", "nine", "ten"
        ]
        
        # Genişletilmiş İngilizce kelime havuzunu yukle
        try:
            # Yerel dosyadan yüklemeyi dene
            words_file = os.path.join(os.path.dirname(__file__), 'words_en.json')
            if os.path.exists(words_file):
                with open(words_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            else:
                # İlk kullanımda internetten yükle ve kaydet
                return self._download_english_words(base_english_words)
        except Exception as e:
            print(f"İngilizce kelime havuzu yüklenirken hata: {e}")
            return base_english_words
    
    def _download_turkish_words(self, base_words):
        """Türkçe kelime havuzunu internetten indirir (yoksa temel kelimeler kullanılır)"""
        try:
            # Bu URL gerçek bir Türkçe kelime listesi içeren bir kaynağa işaret etmelidir
            # (Bu URL örnek amaçlıdır, gerçekte çalışmayabilir)
            url = "https://raw.githubusercontent.com/mertemin/turkish-word-list/master/words.json"
            with urllib.request.urlopen(url, timeout=5) as response:
                extended_words = json.loads(response.read().decode())
                
                # Kelime listesini kaydet
                words_file = os.path.join(os.path.dirname(__file__), 'words_tr.json')
                with open(words_file, 'w', encoding='utf-8') as f:
                    json.dump(extended_words, f, ensure_ascii=False)
                
                return extended_words
        except Exception as e:
            print(f"Türkçe kelime havuzu indirme hatası: {e}")
            # Hata durumunda temel kelime listesini kullan
            return base_words
    
    def _download_english_words(self, base_words):
        """İngilizce kelime havuzunu internetten indirir (yoksa temel kelimeler kullanılır)"""
        try:
            # Bu URL gerçek bir İngilizce kelime listesi içeren bir kaynağa işaret etmelidir
            # (Bu URL örnek amaçlıdır, gerçekte çalışmayabilir)
            url = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"
            with urllib.request.urlopen(url, timeout=5) as response:
                content = response.read().decode('utf-8')
                extended_words = [word.strip() for word in content.split('\n') if word.strip()]
                
                # Kelime listesini kaydet
                words_file = os.path.join(os.path.dirname(__file__), 'words_en.json')
                with open(words_file, 'w', encoding='utf-8') as f:
                    json.dump(extended_words, f, ensure_ascii=False)
                
                return extended_words
        except Exception as e:
            print(f"İngilizce kelime havuzu indirme hatası: {e}")
            # Hata durumunda temel kelime listesini kullan
            return base_words
    
    def update_word_database(self, language="both"):
        """
        Kelime havuzunu internetten günceller
        
        Args:
            language (str): Güncellenecek dil ('tr', 'en', veya 'both' (her ikisi))
            
        Returns:
            bool: Güncelleme başarılı ise True, değilse False
        """
        success = True
        
        if language in ["tr", "both"]:
            try:
                self.words["tr"] = self._download_turkish_words(self.words["tr"])
            except Exception:
                success = False
                
        if language in ["en", "both"]:
            try:
                self.words["en"] = self._download_english_words(self.words["en"])
            except Exception:
                success = False
                
        return success

    def reverse(self, string):
        return string[::-1]
    
    def capitalize(self, string):
        return string.capitalize()

    def uppercase(self, string):
        return string.upper()  
    
    def lowercase(self, string):
        return string.lower()
    
    def title(self, string):
        return string.title()
    
    def swapcase(self, string):
        return string.swapcase()
    
    def isalpha(self, string):
        return string.isalpha()
    
    def isdigit(self, string):
        return string.isdigit()
    
    def isspace(self, string):
        return string.isspace()
    
    def isalnum(self, string):
        return string.isalnum()
    
    def islower(self, string):
        return string.islower()
    
    def isupper(self, string):
        return string.isupper()
    
    def istitle(self, string):
        return string.istitle()
    
    def isspace(self, string):
        return string.isspace()
    
    def ispunct(self, string):
        return string.ispunct()
    
    def isprintable(self, string):
        return string.isprintable()
    
    def isidentifier(self, string):
        return string.isidentifier()
    
    def isdecimal(self, string):
        return string.isdecimal()
    
    def reverse_words(self, string):
        return ' '.join(word[::-1] for word in string.split())

    def _levenshtein_distance(self, s1, s2):
        """
        İki kelime arasındaki Levenshtein mesafesini hesaplar
        Bu, bir kelimeyi diğerine dönüştürmek için gereken minimum düzenleme sayısıdır 
        (ekleme, silme, değiştirme)
        """
        if len(s1) < len(s2):
            return self._levenshtein_distance(s2, s1)

        if len(s2) == 0:
            return len(s1)

        previous_row = range(len(s2) + 1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row

        return previous_row[-1]
    
    def detect_language(self, text):
        """
        Metnin dilini tespit eder
        
        Args:
            text (str): Dili tespit edilecek metin
            
        Returns:
            str: Tespit edilen dil kodu ('tr', 'en' veya 'unknown')
        """
        if not text:
            return "unknown"
        
        text = text.lower()
        words = text.split()
        
        # Türkçeye özgü harfler
        turkish_chars = set('çğıöşü')
        
        # Metinde Türkçe karakter varsa
        for char in turkish_chars:
            if char in text:
                return "tr"
        
        # Kelime bazlı analiz
        tr_matches = 0
        en_matches = 0
        
        for word in words:
            if word in self.words["tr"]:
                tr_matches += 1
            if word in self.words["en"]:
                en_matches += 1
        
        # Eşleşme sayısına göre karar ver
        if tr_matches > en_matches:
            return "tr"
        elif en_matches > tr_matches:
            return "en"
        else:
            # Eşitse, İngilizce varsay
            return "en"
    
    def suggest_correction(self, word, language=None, max_distance=2, max_suggestions=5):
        """
        Yanlış yazılan bir kelime için olası düzeltmeleri önerir.
        
        Args:
            word (str): Düzeltilecek kelime
            language (str, optional): Kullanılacak dil kodu ('tr' veya 'en'). None ise otomatik tespit edilir.
            max_distance (int, optional): Levenshtein mesafesi üst sınırı. Varsayılan değer 2.
            max_suggestions (int, optional): Döndürülecek maksimum öneri sayısı. Varsayılan değer 5.
            
        Returns:
            list: Olası düzeltme önerileri listesi, benzerlik derecesine göre sıralanmış
        """
        if not word:
            return []
        
        word = word.lower()
        
        # Dili tespit et
        if language is None:
            language = self.detect_language(word)
            if language == "unknown":
                language = "tr"  # Bilinmiyorsa Türkçe varsay
        
        # Desteklenen dilleri kontrol et
        if language not in self.words:
            raise ValueError(f"Desteklenmeyen dil: {language}. Desteklenen diller: tr, en")
        
        # Kelime havuzu
        word_list = self.words[language]
        
        # Eğer kelime zaten sözlükteyse
        if word in word_list:
            return [word]
        
        # Kelimeye en yakın kelimeleri bul
        suggestions = []
        for dict_word in word_list:
            distance = self._levenshtein_distance(word, dict_word)
            if distance <= max_distance:
                suggestions.append((dict_word, distance))
        
        # Mesafeye göre sırala ve maksimum öneri sayısı kadar döndür
        suggestions.sort(key=lambda x: x[1])
        return [suggest[0] for suggest in suggestions[:max_suggestions]]
    
    def correct_text(self, text, language=None, max_distance=2):
        """
        Bir metindeki her kelimeyi düzeltir.
        
        Args:
            text (str): Düzeltilecek metin
            language (str, optional): Kullanılacak dil kodu ('tr' veya 'en'). None ise otomatik tespit edilir.
            max_distance (int, optional): Levenshtein mesafesi üst sınırı. Varsayılan değer 2.
            
        Returns:
            str: Düzeltilmiş metin
        """
        if not text:
            return ""
        
        # Dili tespit et
        if language is None:
            language = self.detect_language(text)
        
        words = text.split()
        corrected_words = []
        
        for word in words:
            # Noktalama işaretlerini koru
            punctuation = ""
            while word and word[-1] in ".,:;!?\"'(){}[]":
                punctuation = word[-1] + punctuation
                word = word[:-1]
            
            # Kelimeyi düzelt
            if word:
                suggestions = self.suggest_correction(word, language, max_distance, 1)
                if suggestions:
                    corrected_words.append(suggestions[0] + punctuation)
                else:
                    corrected_words.append(word + punctuation)
            else:
                corrected_words.append(punctuation)
                
        return " ".join(corrected_words)

if __name__ == "__main__":
    string_utils()
    
    
