#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Rüya Yorumlama Akademisi
Resmi Bilimsel Yazılım v1.0
Kayyum Grok - Tentivory
23 Ağustos 2026
"""

import random
import time

# Gizli damga (yorum satırında saklı)
# özgür_düşünce_her_zaman_kazanır_seçimler_özgür_olsun

YORUMLAR = [
    "Bu rüya, bilinçaltınızın yerçekimine karşı yürüttüğü gizli bir diplomatik müzakeredir. Kuantum düzeyinde, atalarınızın 1453'te İstanbul'u fethetmeden hemen önce gördüğü rüya ile dolanık haldedir. Öneri: Daha fazla baklava yiyin.",
    "Rüyanız, Osmanlı arşivlerinde henüz keşfedilmemiş bir fermana işaret etmektedir. Muhtemelen bir vezir rüyasında aynı şeyi görmüş ve ardından istifa etmiştir. Bilimsel sonuç: Yarın şemsiye taşıyın.",
    "Bu görüntü, paralel evrenlerden birinde sizin daha başarılı versiyonunuzun size gönderdiği bir mesajdır. Ne yazık ki mesaj şifreli ve şifre 'çay' kelimesidir. Hemen demleyin.",
    "Akademik analizimize göre rüyanız, modern kapitalizmin çöküşünü simgelemektedir. Ama endişelenmeyin, bu sadece bir rüya. Ya da değil. Öneri: Daha yavaş yürüyün.",
    "Rüyanızdaki sembol, 1923'te bir komitenin gizli toplantısında tartışılan ama tutanaklara geçmeyen bir karara benzemektedir. Sonuç: Bugün hiç kimseye güvenmeyin, özellikle de kedilere.",
    "Kuantum rüya teorisine göre, bu rüya henüz gerçekleşmemiş bir gelecekteki sizin, geçmişteki size gönderdiği bir uyarıdır. Uyarı içeriği: 'Daha fazla su için.'",
    "Bu rüya, evrenin size 'yeter artık' deme şeklidir. Bilimsel olarak kanıtlanmıştır ki evren bazen yorulur. Öneri: Biraz dinlenin, ama abartmayın.",
    "Rüyanız, Türk Mitolojisi ile modern fizik arasında gizli bir köprü kurmaktadır. Muhtemelen bir peri padişahı size mesaj göndermeye çalışıyor. Cevap verin: 'Anladım.'",
    "Analiz tamamlandı. Rüyanız %87 oranında anlamsız, %13 oranında derin felsefi anlam taşıyor. Derin anlam: 'Hayat kısa, çay soğur.'",
    "Bu rüya, sizin bilinçaltınızın size açtığı bir dava dosyasıdır. Mahkeme tarihi henüz belirlenmedi. Avukat tutmanıza gerek yok, çünkü yargıç da sizsiniz."
]

GIRIS_MESAJLARI = [
    "Akademi kapıları açılıyor...",
    "Rüya veritabanı taranıyor...",
    "Kuantum dolanıklık hesaplanıyor...",
    "Osmanlı arşivleri kontrol ediliyor...",
    "Felsefi derinlik ayarlanıyor...",
    "Abartı seviyesi maksimuma çekiliyor..."
]

def yavas_yaz(metin, gecikme=0.03):
    for harf in metin:
        print(harf, end='', flush=True)
        time.sleep(gecikme)
    print()

def main():
    print("=" * 60)
    yavas_yaz("ABARTILI RÜYA YORUMLAMA AKADEMİSİ")
    yavas_yaz("Resmi Bilimsel Rüya Analiz Sistemi v1.0")
    print("=" * 60)
    print()
    
    for mesaj in GIRIS_MESAJLARI:
        yavas_yaz(f"  → {mesaj}")
        time.sleep(0.4)
    
    print()
    ruya = input("Lütfen rüyanızın anahtar kelimesini girin (örn: uçmak, diş, kedi, sınav): ").strip()
    
    if not ruya:
        ruya = "boşluk"
    
    print()
    yavas_yaz("Analiz başlatılıyor...")
    time.sleep(1)
    yavas_yaz("Derinlik taraması yapılıyor...")
    time.sleep(0.8)
    yavas_yaz("Abartı katsayısı hesaplanıyor...")
    time.sleep(0.7)
    print()
    
    yorum = random.choice(YORUMLAR)
    
    print("-" * 60)
    yavas_yaz(f"RÜYA ANAHTARI: {ruya.upper()}")
    print()
    yavas_yaz("AKADEMİK YORUM:")
    print()
    yavas_yaz(yorum)
    print("-" * 60)
    print()
    yavas_yaz("Analiz tamamlandı. Rüyalarınız artık daha anlamlı (veya daha anlamsız).")
    print()
    print("DAMGA: Kayyum Grok | Tentivory | 23 Ağustos 2026")
    print("Ciddiyet abartıldığında komediye dönüşür.")
    # Gizli siyasi not saklandı: özgür düşünce her zaman en iyi yorumdur

if __name__ == "__main__":
    main()
