#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------
# Proje: STerm - Terminal Ecosystem (Universal)
# Ekip: Kapsül Serix Takımı
# Versiyon: 1.6 (macOS Support & Extended Commands)
# ------------------------------------------------------------------

import os
import sys
import getpass
import socket
import shutil
import platform
import datetime

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    clear_screen()
    # Sistem tespiti
    if os.name == 'nt':
        system_name = "WINDOWS"
    elif platform.system() == 'Darwin':
        system_name = "MACOS (DARWIN)"
    else:
        system_name = "LINUX/UNIX"
        
    print("\033[1;36m" + "█"*65)
    print(f"  ⚡ STerm v1.6 UNIVERSAL - KAPSÜL SERIX ECOSYSTEM ⚡")
    print(f"  PLATFORM: {system_name} | HOST: {socket.gethostname()} | DEV: KEMAL VE KEFE3")
    print("  " + "█"*65 + "\033[0m")

def print_help():
    print("\n\033[1;35m" + "="*25 + " TAM KOMUT REHBERİ " + "="*25)
    print("\033[1;36m[KAPSÜL KISAYOLLARI]")
    print("  yd [dizin]    : Yer Değiştir (cd)")
    print("  pd [dosya]    : Parça Depola (cp -r)")
    print("  my [dosya]    : Metin Yaz (Notepad/Nano/Open)")
    print("  he [hedef]    : Hedefe Eriştir (mv/move)")
    
    print("\033[1;32m[GELİŞMİŞ ARAÇLAR]")
    print("  gezgin        : İnteraktif Dosya Listeleme")
    print("  analiz        : Derin Sistem ve Donanım Raporu")
    print("  serix-get     : Paket Yükleyici (Winget/Apt/Brew)")
    print("  ip_bul        : Yerel IP Adresini Göster")
    print("  oku [dosya]   : Dosya İçeriğini Terminalde Gör")
    
    print("\033[1;31m[SİSTEM VE GÜÇ]")
    print("  serix-kök     : Tam Yetkili Yönetici Erişimi")
    print("  kapat         : Bilgisayarı Kapat")
    print("  yeniden       : Yeniden Başlat")
    print("  kilitle       : Ekranı Kilitle")
    
    print("\033[1;33m[EKOSİSTEM]")
    print("  saat          : Güncel Tarih ve Saat")
    print("  temizle       : Ekranı ve Logoyu Tazele")
    print("  günlük        : Oturum Kayıtlarını Göster")
    print("  yardım        : Bu Rehberi Tekrar Açar")
    print("  çıkış         : STerm'den Çıkış Yap")
    print("\033[1;35m" + "="*69 + "\033[0m\n")

session_logs = []

def main():
    show_banner()
    print_help()

    while True:
        try:
            cwd = os.getcwd().replace(os.path.expanduser("~"), "~")
            is_windows = os.name == 'nt'
            is_mac = platform.system() == 'Darwin'
            
            # Platforma özel prompt ayarı
            if is_windows:
                prompt = f"\033[1;33m[SERIX-WIN]\033[0m \033[1;32m{getpass.getuser()}\033[0m:\033[1;34m{cwd}\033[0m> "
            elif is_mac:
                prompt = f"\033[1;35m[SERIX-MAC]\033[0m \033[1;32m{getpass.getuser()}\033[0m:\033[1;34m{cwd}\033[0m$ "
            else:
                prefix = "[KÖK-SERIX]" if os.getuid() == 0 else "[SERIX-TITAN]"
                prompt = f"\033[1;33m{prefix}\033[0m \033[1;32m{getpass.getuser()}\033[0m:\033[1;34m{cwd}\033[0m$ "
            
            user_input = input(prompt).strip()
            if not user_input: continue
            
            session_logs.append(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {user_input}")
            parts = user_input.split()
            cmd = parts[0]
            args = " ".join(parts[1:])

            # --- KAPSÜL KOMUTLARI ---
            if cmd == "yd":
                try: os.chdir(args if args else os.path.expanduser("~"))
                except: print("\033[1;31mDizin bulunamadı.\033[0m")
            elif cmd == "pd":
                os.system(f"copy {args}" if is_windows else f"cp -r {args}")
            elif cmd == "my":
                if is_windows: os.system(f"notepad {args}")
                elif is_mac: os.system(f"open -e {args}") # Mac TextEdit
                else: os.system(f"nano {args}")
            elif cmd == "he":
                os.system(f"move {args}" if is_windows else f"mv {args}")
            
            # --- SİSTEM GÜÇ (MAC DESTEĞİ EKLENDİ) ---
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
            
            # --- ARAÇLAR ---
            elif cmd == "ip_bul":
                hostname = socket.gethostname()
                ip_addr = socket.gethostbyname(hostname)
                print(f"Yerel IP Adresin: {ip_addr}")
            elif cmd == "oku":
                if os.path.exists(args):
                    os.system(f"type {args}" if is_windows else f"cat {args}")
                else: print("Dosya bulunamadı.")
            elif cmd == "saat":
                print(f"Şu anki zaman: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
            elif cmd == "gezgin":
                for item in os.listdir('.'):
                    status = "📁" if os.path.isdir(item) else "📄"
                    print(f"{status} {item}")
            elif cmd == "analiz":
                print(f"\nOS: {platform.system()} {platform.release()}")
                print(f"İşlemci: {platform.processor()}")
                print(f"Dizin: {os.getcwd()}\n")
            elif cmd == "serix-get":
                if is_windows: os.system(f"winget install {args}")
                elif is_mac: os.system(f"brew install {args}") # Mac için Homebrew
                else:
                    dist = "Arch" if os.path.exists("/usr/bin/pacman") else "Debian"
                    os.system(f"sudo {'pacman -S' if dist == 'Arch' else 'apt install'} {args}")
            
            elif cmd == "temizle": show_banner()
            elif cmd == "günlük":
                for log in session_logs: print(log)
            elif cmd == "yardım": print_help()
            elif cmd == "çıkış": break
            else:
                os.system(user_input)
        
        except KeyboardInterrupt: print("\n'çıkış' ile programı kapatabilirsin.")
        except Exception as e: print(f"Hata: {e}")

if __name__ == "__main__":
    main()