# 1. Taranacak Resmi Web Siteleri
SOURCES = {
    "kanunlar": "https://www.mevzuat.gov.tr/#kanunlar",
    "cbk": "https://www.mevzuat.gov.tr/#cumhurbaskanligiKararnameleri",
    "uyap_emsal": "https://emsal.uyap.gov.tr/",
    "mfa_anlasmalar": "https://ua.mfa.gov.tr/"
}

# 2. Veritabanını Aç
current_db = load_database()

# 3. İnternetten Yeni Verileri Çek ve Karşılaştır
# Yeni bir Yargıtay kararı veya kanun maddesi varsa ekle

# 4. legal_database.json Dosyasını Yeniden Kaydet
save_database(current_db)
