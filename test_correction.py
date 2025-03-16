from elan import elan

# Elan sınıfını başlat
el = elan()

# Kelime havuzunu güncellemeyi dene (opsiyonel)
try:
    print("Kelime havuzu güncelleniyor... (Bu biraz zaman alabilir)")
    success = el.string.update_word_database()
    if success:
        print("Kelime havuzu başarıyla güncellendi!")
    else:
        print("Kelime havuzu güncellenirken bazı hatalar oluştu.")
except Exception as e:
    print(f"Kelime havuzu güncellenirken hata: {e}")

# Dil testi
print("\n--- Dil Tespit Testi ---")
texts = [
    "merhaba dünya",
    "hello world",
    "merhaba world",
    "hello dünya",
    "bu bir türkçe cümledir",
    "this is an english sentence"
]

for text in texts:
    lang = el.string.detect_language(text)
    print(f"Metin: '{text}' -> Dil: {lang}")

# Türkçe kelime düzeltme testi
print("\n--- Türkçe Kelime Düzeltme Testi ---")
tr_words = ["meraba", "nasilsn", "teşekür", "gunaydın", "iyiim", "kitab", "bilgisayır", "telefn", "istanbıl"]

for yanlis_kelime in tr_words:
    oneriler = el.string.suggest_correction(yanlis_kelime, language="tr", max_suggestions=3)
    print(f"Yanlış: '{yanlis_kelime}' -> Öneriler: {oneriler}")

# İngilizce kelime düzeltme testi
print("\n--- İngilizce Kelime Düzeltme Testi ---")
en_words = ["helo", "worl", "computr", "phne", "progrm", "boook", "softwre", "codng", "thnk"]

for yanlis_kelime in en_words:
    oneriler = el.string.suggest_correction(yanlis_kelime, language="en", max_suggestions=3)
    print(f"Yanlış: '{yanlis_kelime}' -> Öneriler: {oneriler}")

# Otomatik dil tespiti ile düzeltme testi
print("\n--- Otomatik Dil Tespiti ile Düzeltme ---")
yanlis_kelimeler = ["meraba", "helo", "gunaydın", "worl", "telefn", "computr"]

for yanlis_kelime in yanlis_kelimeler:
    oneriler = el.string.suggest_correction(yanlis_kelime, max_suggestions=3)
    lang = el.string.detect_language(yanlis_kelime)
    print(f"Yanlış: '{yanlis_kelime}' (Tespit edilen dil: {lang}) -> Öneriler: {oneriler}")

# Türkçe metin düzeltme testi
print("\n--- Türkçe Metin Düzeltme Testi ---")
yanlis_metin = "meraba nasilsn bugun hva cok guzl"
duzeltilmis_metin = el.string.correct_text(yanlis_metin, language="tr")
print(f"Yanlış metin: '{yanlis_metin}'")
print(f"Düzeltilmiş metin: '{duzeltilmis_metin}'")

# İngilizce metin düzeltme testi
print("\n--- İngilizce Metin Düzeltme Testi ---")
yanlis_metin = "helo worl how ar you tody"
duzeltilmis_metin = el.string.correct_text(yanlis_metin, language="en")
print(f"Yanlış metin: '{yanlis_metin}'")
print(f"Düzeltilmiş metin: '{duzeltilmis_metin}'")

# Kullanıcı girdisi test
print("\n--- Kullanıcı Girdisi Test ---")
kullanici_girdisi = input("Düzeltilecek bir kelime yazın: ")
dil_secimi = input("Dil seçin (tr/en) veya otomatik tespit için boş bırakın: ").strip().lower()

if dil_secimi not in ["tr", "en"]:
    dil_secimi = None
    tespit_edilen_dil = el.string.detect_language(kullanici_girdisi)
    print(f"Tespit edilen dil: {tespit_edilen_dil}")

oneriler = el.string.suggest_correction(kullanici_girdisi, language=dil_secimi, max_suggestions=5)
print(f"'{kullanici_girdisi}' için öneriler: {oneriler}")

# Tüm yanlış yazılan metni düzeltme
print("\n--- Kullanıcı Metin Düzeltme ---")
kullanici_metni = input("Düzeltilecek bir cümle yazın: ")
dil_secimi = input("Dil seçin (tr/en) veya otomatik tespit için boş bırakın: ").strip().lower()

if dil_secimi not in ["tr", "en"]:
    dil_secimi = None
    tespit_edilen_dil = el.string.detect_language(kullanici_metni)
    print(f"Tespit edilen dil: {tespit_edilen_dil}")

duzeltilmis_metin = el.string.correct_text(kullanici_metni, language=dil_secimi)
print(f"Düzeltilmiş metin: '{duzeltilmis_metin}'") 