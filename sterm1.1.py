#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------
# Proje: STerm - Terminal Ecosystem
# Ekip: Kapsül Serix Takımı
# Versiyon: 1.1 (OTA & Kapsül Shortcuts)
# Geliştirici: kefe3
# ------------------------------------------------------------------

import os
import sys
import getpass
import socket
import subprocess
import tkinter as tk

def get_distro():
    if os.path.exists("/usr/bin/pacman"): return "Arch"
    elif os.path.exists("/usr/bin/apt"): return "Debian/Ubuntu"
    return "Generic Linux"

def self_update():
    """GitHub'dan (kefe3/sterm) en güncel kodu çeker."""
    if not os.path.exists(".git"):
        print("\033[1;31m[HATA] .git klasörü bulunamadı. Lütfen 'git clone' ile kurun.\033[0m")
        return

    print("\033[1;33m[OTA] Kapsül Serix Sunucularına Bağlanılıyor...\033[0m")
    try:
        result = subprocess.run(["git", "pull", "origin", "main"], capture_output=True, text=True)
        if "Already up to date" in result.stdout:
            print("\033[1;32m[OTA] Sistem zaten en güncel sürümde.\033[0m")
        else:
            print("\033[1;32m[OTA] Güncelleme başarıyla indirildi!\033[0m")
            print("\033[1;36m[OTA] Yeniden başlatılıyor...\033[0m")
            os.execv(sys.executable, ['python3'] + sys.argv)
    except Exception as e:
        print(f"\033[1;31m[HATA] Güncelleme başarısız: {e}\033[0m")

def main():
    user = getpass.getuser()
    hostname = socket.gethostname()
    distro = get_distro()
    
    os.system('clear')
    print("\033[1;36m" + "="*50)
    print("  ⚡ STerm v1.1 - KAPSÜL SERIX (OTA & SHORTCUTS) ⚡")
    print("  " + "="*50 + "\033[0m")

    while True:
        try:
            cwd = os.getcwd().replace(os.path.expanduser("~"), "~")
            prompt = f"\033[1;33m[SERIX]\033[0m \033[1;32m{user}@{hostname}\033[0m:\033[1;34m{cwd}\033[0m$ "
            
            user_input = input(prompt).strip()
            if not user_input: continue
            
            parts = user_input.split()
            cmd = parts[0]
            args = " ".join(parts[1:])

            # --- KAPSÜL ÖZEL KISAYOLLAR ---
            if cmd == "yd": # cd
                try: os.chdir(parts[1] if len(parts) > 1 else os.path.expanduser("~"))
                except: print("Dizin bulunamadı.")
                continue
            elif cmd == "pd": # cp
                os.system(f"cp {args}")
                continue
            elif cmd == "my": # nano
                os.system(f"nano {args}")
                continue
            elif cmd == "he": # mv
                os.system(f"mv {args}")
                continue
            
            # --- SİSTEM KOMUTLARI ---
            elif cmd == "sterm-update":
                self_update()
            elif cmd == "exit":
                break
            elif cmd == "serix-get":
                if distro == "Arch": os.system(f"sudo pacman -S --noconfirm {args}")
                else: os.system(f"sudo apt update && sudo apt install -y {args}")
            elif cmd == "help":
                print("\n\033[1;35m--- Kapsül Serix Kısayolları ---\033[0m")
                print(" yd [dizin]   : Yer Değiştir (cd)")
                print(" pd [kaynak]  : Parça Depola (cp)")
                print(" my [dosya]   : Metin Yaz (nano)")
                print(" he [hedef]   : Hedefe Eriştir (mv)")
                print(" sterm-update : Sistemi GitHub'dan günceller.")
                print("------------------------------\n")
            else:
                os.system(user_input)
        
        except KeyboardInterrupt:
            print("\n\033[1;31mÇıkmak için 'exit' yazın.\033[0m")
        except EOFError:
            break

if __name__ == "__main__":
    main()
