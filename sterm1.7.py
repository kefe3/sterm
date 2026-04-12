#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------
# Proje: STerm - Terminal Ecosystem (Universal)
# Ekip: Kapsül Serix Takımı
# Versiyon: 1.7 (Ultra Extended Edition)
# ------------------------------------------------------------------

import os
import sys
import getpass
import socket
import shutil
import platform
import datetime
import webbrowser # Yeni: Web sitelerini açmak için

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    clear_screen()
    if os.name == 'nt': system_name = "WINDOWS"
    elif platform.system() == 'Darwin': system_name = "MACOS (DARWIN)"
    else: system_name = "LINUX/UNIX"
        
    print("\033[1;36m" + "█"*75)
    print(f"  ⚡ STerm v1.7 ULTRA - KAPSÜL SERIX ECOSYSTEM ⚡")
    print(f"  PLATFORM: {system_name} | HOST: {socket.gethostname()} | DEV: KEMAL VE KEFE3")
    print("  " + "█"*75 + "\033[0m")

def print_help():
    print("\n\033[1;35m" + "="*30 + " SERIX KOMUT MERKEZİ " + "="*30)
    print("\033[1;36m[TEMEL KAPSÜL]")
    print("  yd [dizin]    : Yer Değiştir (cd)          | pd [dosya]    : Parça Depola (cp)")
    print("  my [dosya]    : Metin Yaz (Düzenle)        | he [hedef]    : Hedefe Eriştir (mv)")
    print("  sil [dosya]   : Dosya/Klasör Sil           | yarat [isim]  : Yeni Klasör Oluştur")
    
    print("\033[1;32m[GELİŞMİŞ ARAÇLAR]")
    print("  gezgin        : Dosyaları Listele          | analiz        : Sistem Raporu")
    print("  oku [dosya]   : Dosya İçeriğini Gör        | ara [kelime]  : Dosya İsminde Ara")
    print("  ip_bul        : Yerel IP Adresini Gör      | web [url]     : Tarayıcıda Site Aç")
    print("  boyut [dosya] : Dosya Boyutunu Öğren       | ping [host]   : Bağlantı Test Et")
    
    print("\033[1;31m[SİSTEM VE GÜÇ]")
    print("  serix-kök     : Yönetici Erişimi           | kapat / yeniden / kilitle")
    print("  serix-get     : Paket Yükleyici            | disk          : Disk Kullanımı")
    
    print("\033[1;33m[EKOSİSTEM]")
    print("  saat          : Tarih ve Saat              | not-al [not]  : Hızlı Not Kaydet")
    print("  temizle       : Ekranı Tazele              | günlük        : Logları Göster")
    print("  çıkış         : STerm'den Ayrıl            | yardım        : Bu Menü")
    print("\033[1;35m" + "="*81 + "\033[0m\n")

session_logs = []

def main():
    show_banner()
    print_help()

    while True:
        try:
            cwd = os.getcwd().replace(os.path.expanduser("~"), "~")
            is_windows = os.name == 'nt'
            is_mac = platform.system() == 'Darwin'
            
            # Prompt ayarı
            if is_windows: prompt = f"\033[1;33m[SERIX-WIN]\033[0m \033[1;32m{getpass.getuser()}\033[0m:\033[1;34m{cwd}\033[0m> "
            elif is_mac: prompt = f"\033[1;35m[SERIX-MAC]\033[0m \033[1;32m{getpass.getuser()}\033[0m:\033[1;34m{cwd}\033[0m$ "
            else:
                prefix = "[KÖK-SERIX]" if os.getuid() == 0 else "[SERIX-TITAN]"
                prompt = f"\033[1;33m{prefix}\033[0m \033[1;32m{getpass.getuser()}\033[0m:\033[1;34m{cwd}\033[0m$ "
            
            user_input = input(prompt).strip()
            if not user_input: continue
            
            session_logs.append(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {user_input}")
            parts = user_input.split()
            cmd = parts[0]
            args = " ".join(parts[1:])

            # --- YENİ EKLENEN KOMUTLAR VE MANTIĞI ---
            if cmd == "yarat":
                os.makedirs(args, exist_ok=True)
                print(f"📁 '{args}' klasörü oluşturuldu.")
            
            elif cmd == "sil":
                if os.path.isdir(args): shutil.rmtree(args)
                else: os.remove(args)
                print(f"🗑️ '{args}' başarıyla silindi.")
            
            elif cmd == "web":
                url = args if args.startswith("http") else f"https://{args}"
                webbrowser.open(url)
                print(f"🌐 {url} açılıyor...")
            
            elif cmd == "not-al":
                with open("sterm_notlar.txt", "a", encoding="utf-8") as f:
                    f.write(f"[{datetime.datetime.now()}] {args}\n")
                print("📝 Not kaydedildi (sterm_notlar.txt).")
            
            elif cmd == "boyut":
                if os.path.exists(args):
                    s = os.path.getsize(args)
                    print(f"⚖️ Boyut: {s / 1024:.2f} KB")
                else: print("Dosya bulunamadı.")
            
            elif cmd == "ara":
                found = [f for f in os.listdir('.') if args.lower() in f.lower()]
                print(f"🔍 Bulunanlar: {found}" if found else "Sonuç yok.")
            
            elif cmd == "ping":
                os.system(f"ping -n 4 {args}" if is_windows else f"ping -c 4 {args}")
            
            elif cmd == "disk":
                total, used, free = shutil.disk_usage("/")
                print(f"💾 Toplam: {total // (2**30)}GB | Kullanılan: {used // (2**30)}GB | Boş: {free // (2**30)}GB")

            # --- ESKİ KOMUTLAR (GÜNCEL) ---
            elif cmd == "yd":
                try: os.chdir(args if args else os.path.expanduser("~"))
                except: print("\033[1;31mDizin bulunamadı.\033[0m")
            elif cmd == "pd": os.system(f"copy {args}" if is_windows else f"cp -r {args}")
            elif cmd == "my":
                if is_windows: os.system(f"notepad {args}")
                elif is_mac: os.system(f"open -e {args}")
                else: os.system(f"nano {args}")
            elif cmd == "he": os.system(f"move {args}" if is_windows else f"mv {args}")
            elif cmd == "kapat":
                if is_windows: os.system("shutdown /s /t 0")
                elif is_mac: os.system("osascript -e 'tell app \"System Events\" to shut down'")
                else: os.system("sudo shutdown -h now")
            elif cmd == "yeniden":
                if is_windows: os.system("shutdown /r /t 0")
                elif is_mac: os.system("osascript -e 'tell app \"System Events\" to restart'")
                else: os.system("sudo reboot")
            elif cmd == "kilitle":
                if is_windows: os.system("rundll32.exe user32.dll,LockWorkStation")
                elif is_mac: os.system("pmset displaysleepnow")
                else: os.system("xdg-screensaver lock")
            elif cmd == "ip_bul":
                print(f"🌐 IP: {socket.gethostbyname(socket.gethostname())}")
            elif cmd == "oku":
                if os.path.exists(args): os.system(f"type {args}" if is_windows else f"cat {args}")
                else: print("Dosya bulunamadı.")
            elif cmd == "saat": print(f"⏰ {datetime.datetime.now().strftime('%H:%M:%S')}")
            elif cmd == "gezgin":
                for item in os.listdir('.'):
                    print(f"{'📁' if os.path.isdir(item) else '📄'} {item}")
            elif cmd == "analiz":
                print(f"💻 OS: {platform.system()} | İşlemci: {platform.processor()}")
            elif cmd == "serix-get":
                if is_windows: os.system(f"winget install {args}")
                elif is_mac: os.system(f"brew install {args}")
                else: os.system(f"sudo apt install {args}")
            elif cmd == "temizle": show_banner()
            elif cmd == "günlük":
                for log in session_logs: print(log)
            elif cmd == "yardım": print_help()
            elif cmd == "çıkış": break
            else: os.system(user_input)
        
        except KeyboardInterrupt: print("\n'çıkış' yaz.")
        except Exception as e: print(f"Hata oluştu: {e}")

if __name__ == "__main__":
    main()