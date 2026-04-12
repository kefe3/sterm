#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------
# Proje: STerm - Terminal Ekosistemi (Evrensel)
# Ekip: Kapsül Serix Takımı
# Versiyon: 1.8 (Expansion & Auto-Update Edition)
# ------------------------------------------------------------------

import os
import sys
import getpass
import socket
import shutil
import platform
import datetime
import webbrowser
import requests  # pip install requests

# --- YAPILANDIRMA ---
SURUM = "1.8"
GUNCELLEME_URL = "https://raw.githubusercontent.com/kefe3/sterm/refs/heads/main/sterm_guncelleme.py"

def ekrani_temizle():
    os.system('cls' if os.name == 'nt' else 'clear')

def guncelleme_denetle():
    print("\033[1;33m🔄 Serix Bulut Sunucularına Bağlanılıyor...\033[0m")
    try:
        yanit = requests.get(GUNCELLEME_URL, timeout=10)
        if yanit.status_code == 200:
            with open(__file__, "w", encoding="utf-8") as f:
                f.write(yanit.text)
            print("\033[1;32m✅ STerm Başarıyla Güncellendi! Lütfen programı yeniden başlatın.\033[0m")
            sys.exit()
        else:
            print(f"\033[1;31m❌ Güncelleme sunucusuna ulaşılamadı. Hata: {yanit.status_code}\033[0m")
    except Exception as e:
        print(f"\033[1;31m❌ Bağlantı hatası: {e}\033[0m")

def banner_goster():
    ekrani_temizle()
    sistem = platform.system().upper()
    print("\033[1;36m" + "█"*75)
    print(f"  ⚡ STerm v{SURUM} ULTRA - KAPSÜL SERIX EKOSİSTEMİ ⚡")
    print(f"  SİSTEM: {sistem} | CİHAZ: {socket.gethostname()} | GELİŞTİRİCİ: KEMAL & KEFE3")
    print("  " + "█"*75 + "\033[0m")

def yardim_bas():
    print("\n\033[1;35m" + "="*30 + " SERIX KOMUT MERKEZİ " + "="*30)
    print("\033[1;36m[SİSTEM VE GÜNCELLEME]")
    print("  guncelle      : Yazılımı İnternetten Güncelle  | surum          : Versiyon Detayları")
    print("  analiz        : Sistem Bilgilerini Göster      | disk           : Disk Kullanımı")
    print("  temizle       : Ekranı Tazele                  | yardım         : Bu Menüyü Göster")
    
    print("\033[1;32m[DOSYA VE DİZİN YÖNETİMİ]")
    print("  yd [dizin]    : Dizin Değiştir (cd)            | gezgin         : Dosyaları Listele")
    print("  yarat [isim]  : Yeni Klasör Oluştur            | sil [isim]     : Dosya/Klasör Sil")
    print("  ara [isim]    : Dosya Ara                      | boyut [isim]   : Dosya Boyutu (KB)")
    print("  oku [dosya]   : Dosya İçeriğini Oku            | gezgin         : Klasör İçeriği")
    
    print("\033[1;33m[AKILLI ARAÇLAR]")
    print("  hava [sehir]  : Hava Durumunu Göster           | hesapla [işlem]: Matematiksel Çözüm")
    print("  indir [url][ad]: Dosya İndir                   | parola-uret    : Güvenli Şifre")
    print("  web [url]     : Tarayıcıda Site Aç             | ip_bul         : Yerel IP Adresi")
    
    print("\033[1;31m[GÜÇ VE YÖNETİM]")
    print("  kapat         : Bilgisayarı Kapatır            | yeniden        : Yeniden Başlatır")
    print("  kilitle       : Oturumu Kilitleir              | çıkış          : STerm'den Ayrıl")
    print("\033[1;35m" + "="*81 + "\033[0m\n")

def main():
    banner_goster()
    yardim_bas()
    gunluk_kayitlar = []

    while True:
        try:
            dizin = os.getcwd().replace(os.path.expanduser("~"), "~")
            kullanici = getpass.getuser()
            is_windows = os.name == 'nt'
            
            # Dinamik Prompt
            if is_windows:
                prompt = f"\033[1;33m[SERIX-WIN]\033[0m \033[1;32m{kullanici}\033[0m:\033[1;34m{dizin}\033[0m> "
            else:
                yetki = "[KÖK-SERIX]" if os.getuid() == 0 else "[SERIX-TITAN]"
                prompt = f"\033[1;33m{yetki}\033[0m \033[1;32m{kullanici}\033[0m:\033[1;34m{dizin}\033[0m$ "
            
            giris = input(prompt).strip()
            if not giris: continue
            
            gunluk_kayitlar.append(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {giris}")
            parcalar = giris.split()
            komut = parcalar[0].lower()
            arguman = " ".join(parcalar[1:])

            # --- SİSTEM ---
            if komut == "guncelle": guncelleme_denetle()
            elif komut == "surum": print(f"Sürüm: {SURUM}\nKod Adı: Amber Expansion\nEkip: Kemal & Kağan Efe")
            elif komut == "temizle": banner_goster()
            elif komut == "yardim" or komut == "yardım": yardim_bas()
            elif komut == "analiz":
                print(f"İşlemci: {platform.processor()}\nOS: {platform.system()} {platform.version()}\nMimari: {platform.machine()}")
            elif komut == "çıkış": break
            
            # --- ARAÇLAR ---
            elif komut == "hava":
                sehir = arguman if arguman else "Konya"
                os.system(f"curl -s wttr.in/{sehir}?format=3" if is_windows else f"curl wttr.in/{sehir}?format=3")
            
            elif komut == "hesapla":
                try: print(f"🔢 Sonuç: {eval(arguman)}")
                except: print("❌ Hatalı işlem!")

            elif komut == "parola-uret":
                import string, random
                k = string.ascii_letters + string.digits + string.punctuation
                print(f"🔐 Şifre: {''.join(random.choice(k) for i in range(12))}")

            elif komut == "indir":
                try:
                    url, isim = arguman.split()
                    r = requests.get(url, stream=True)
                    with open(isim, 'wb') as f:
                        for chunk in r.iter_content(8192): f.write(chunk)
                    print(f"✅ {isim} indirildi.")
                except: print("⚠️ Kullanım: indir [url] [dosya_adı]")

            # --- DOSYA VE DİZİN ---
            elif komut == "yarat": os.makedirs(arguman, exist_ok=True); print(f"📁 Klasör oluşturuldu: {arguman}")
            elif komut == "sil":
                if os.path.isdir(arguman): shutil.rmtree(arguman)
                else: os.remove(arguman)
                print(f"🗑️ Silindi: {arguman}")
            elif komut == "gezgin":
                for oge in os.listdir('.'): print(f"{'📁' if os.path.isdir(oge) else '📄'} {oge}")
            elif komut == "boyut":
                if os.path.exists(arguman): print(f"⚖️ {os.path.getsize(arguman) / 1024:.2f} KB")
            elif komut == "yd":
                try: os.chdir(arguman if arguman else os.path.expanduser("~"))
                except: print("❌ Dizin yok.")
            elif komut == "oku":
                try:
                    with open(arguman, "r", encoding="utf-8") as f: print(f.read())
                except: print("❌ Dosya okunamadı.")
            elif komut == "ara":
                bulunanlar = [f for f in os.listdir('.') if arguman in f]
                print(f"🔍 Bulunanlar: {bulunanlar}" if bulunanlar else "❌ Sonuç yok.")
            
            # --- WEB VE AĞ ---
            elif komut == "web":
                url = arguman if arguman.startswith("http") else f"https://{arguman}"
                webbrowser.open(url); print(f"🌐 {url} açılıyor...")
            elif komut == "ip_bul": print(f"🌐 IP: {socket.gethostbyname(socket.gethostname())}")
            elif komut == "disk":
                t, k, b = shutil.disk_usage("/")
                print(f"💾 Toplam: {t//(2**30)}GB | Kullanılan: {k//(2**30)}GB | Boş: {b//(2**30)}GB")

            # --- GÜÇ ---
            elif komut == "kapat": os.system("shutdown /s /t 1" if is_windows else "shutdown -h now")
            elif komut == "yeniden": os.system("shutdown /r /t 1" if is_windows else "reboot")
            elif komut == "kilitle": os.system("rundll32.exe user32.dll,LockWorkStation" if is_windows else "gnome-screensaver-command -l")

            else: os.system(giris) # Bilinmeyen komutları sisteme gönder

        except KeyboardInterrupt: print("\n'çıkış' yazın.")
        except Exception as e: print(f"❌ Hata: {e}")

if __name__ == "__main__":
    main()
