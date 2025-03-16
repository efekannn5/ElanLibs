from elan import elan
import time

# Elan sınıfını başlat
el = elan()

print("Elan Kelime Düzeltme Sistemi - Gelişmiş Test")
print("=" * 50)

# Test başlangıç zamanı
start_time = time.time()

# Mevcut kelime havuzlarını kontrol et
print("\n1. Kelime Havuzu Durumu:")
tr_words_count = len(el.string.words["tr"])
en_words_count = len(el.string.words["en"])
print(f"Türkçe kelime sayısı: {tr_words_count}")
print(f"İngilizce kelime sayısı: {en_words_count}")

# Kelime havuzunu güncellemeyi dene (isteğe bağlı)
try:
    print("\n2. Yeni Kelime Ekleme Testi:")
    tr_new_words = ["programlama", "algoritma", "fonksiyon", "parametre", "değişken"]
    added_count = el.string.add_custom_words(tr_new_words, language="tr")
    print(f"Eklenen yeni Türkçe kelime sayısı: {added_count}")
    
    en_new_words = ["programming", "algorithm", "function", "parameter", "variable"]
    added_count = el.string.add_custom_words(en_new_words, language="en")
    print(f"Eklenen yeni İngilizce kelime sayısı: {added_count}")
except Exception as e:
    print(f"Kelime ekleme hatası: {e}")

try:
    print("\n3. Alternatif Kelime Kaynakları Testi:")
    update_choice = input("Kelime havuzunu internetten güncellemek ister misiniz? (e/h): ").lower()
    if update_choice == 'e':
        force_update = input("Zorla güncelleme yapmak ister misiniz? (e/h): ").lower() == 'e'
        print("Kelime havuzu güncelleniyor... (Bu biraz zaman alabilir)")
        success = el.string.update_word_database(force=force_update)
        if success:
            print("Kelime havuzu başarıyla güncellendi!")
            # Güncelleme sonrası kelime sayılarını tekrar göster
            tr_words_count = len(el.string.words["tr"])
            en_words_count = len(el.string.words["en"])
            print(f"Güncellenmiş Türkçe kelime sayısı: {tr_words_count}")
            print(f"Güncellenmiş İngilizce kelime sayısı: {en_words_count}")
        else:
            print("Kelime havuzu güncellenirken bazı hatalar oluştu.")
    else:
        print("Güncelleme işlemi atlandı.")
except Exception as e:
    print(f"Kelime havuzu güncellenirken hata: {e}")

# Dil tespiti
print("\n4. Dil Tespit Testi:")
texts = [
    "merhaba dünya",
    "hello world",
    "merhaba world", 
    "hello dünya",
    "bu bir türkçe cümledir",
    "this is an english sentence",
    "çğıöşü ile türkçe karakterler",
    "complex english with numbers 12345"
]

for text in texts:
    lang = el.string.detect_language(text)
    print(f"Metin: '{text}' -> Dil: {lang}")

# Türkçe kelime düzeltme testi
print("\n5. Türkçe Kelime Düzeltme Testi:")
tr_words = ["meraba", "nasilsn", "teşekür", "gunaydın", "iyiim", "kitab", "bilgisayır", "telefn", "istanbıl"]

for yanlis_kelime in tr_words:
    start = time.time()
    oneriler = el.string.suggest_correction(yanlis_kelime, language="tr", max_suggestions=3)
    elapsed = time.time() - start
    print(f"Yanlış: '{yanlis_kelime}' -> Öneriler: {oneriler} ({elapsed:.3f}s)")

# İngilizce kelime düzeltme testi
print("\n6. İngilizce Kelime Düzeltme Testi:")
en_words = ["helo", "worl", "computr", "phne", "progrm", "boook", "softwre", "codng", "thnk"]

for yanlis_kelime in en_words:
    start = time.time()
    oneriler = el.string.suggest_correction(yanlis_kelime, language="en", max_suggestions=3)
    elapsed = time.time() - start
    print(f"Yanlış: '{yanlis_kelime}' -> Öneriler: {oneriler} ({elapsed:.3f}s)")

# Otomatik dil tespiti ile düzeltme testi
print("\n7. Otomatik Dil Tespiti ile Düzeltme:")
yanlis_kelimeler = ["meraba", "helo", "gunaydın", "worl", "telefn", "computr"]

for yanlis_kelime in yanlis_kelimeler:
    start = time.time()
    lang = el.string.detect_language(yanlis_kelime)
    oneriler = el.string.suggest_correction(yanlis_kelime, max_suggestions=3)
    elapsed = time.time() - start
    print(f"Yanlış: '{yanlis_kelime}' (Tespit edilen dil: {lang}) -> Öneriler: {oneriler} ({elapsed:.3f}s)")

# Türkçe metin düzeltme testi
print("\n8. Türkçe Metin Düzeltme Testi:")
yanlis_metin = "meraba nasilsn bugun hva cok guzl istanbulda"
start = time.time()
duzeltilmis_metin = el.string.correct_text(yanlis_metin, language="tr")
elapsed = time.time() - start
print(f"Yanlış metin: '{yanlis_metin}'")
print(f"Düzeltilmiş metin: '{duzeltilmis_metin}' ({elapsed:.3f}s)")

# İngilizce metin düzeltme testi
print("\n9. İngilizce Metin Düzeltme Testi:")
yanlis_metin = "helo worl how ar you tody? The weathr is beatiful"
start = time.time()
duzeltilmis_metin = el.string.correct_text(yanlis_metin, language="en")
elapsed = time.time() - start
print(f"Yanlış metin: '{yanlis_metin}'")
print(f"Düzeltilmiş metin: '{duzeltilmis_metin}' ({elapsed:.3f}s)")

# Kullanıcı girdisi test
print("\n10. Kullanıcı Girdisi Test:")
print("Not: Çıkmak için boş bir değer girin.")

while True:
    kullanici_girdisi = input("\nDüzeltilecek bir kelime yazın: ")
    if not kullanici_girdisi.strip():
        break
        
    dil_secimi = input("Dil seçin (tr/en) veya otomatik tespit için boş bırakın: ").strip().lower()

    if dil_secimi not in ["tr", "en"]:
        dil_secimi = None
        tespit_edilen_dil = el.string.detect_language(kullanici_girdisi)
        print(f"Tespit edilen dil: {tespit_edilen_dil}")
        dil_secimi = tespit_edilen_dil

    start = time.time()
    oneriler = el.string.suggest_correction(kullanici_girdisi, language=dil_secimi, max_suggestions=5)
    elapsed = time.time() - start
    print(f"'{kullanici_girdisi}' için öneriler: {oneriler} ({elapsed:.3f}s)")

# Toplam çalışma süresi
total_time = time.time() - start_time
print(f"\nToplam çalışma süresi: {total_time:.2f} saniye")
print("\nTest tamamlandı!") 