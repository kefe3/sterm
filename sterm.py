#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------
# Proje: STerm - Terminal Ecosystem
# Ekip: Kapsül Serix Takımı
# Versiyon: 1.0 (Amber Edition)
# Geliştirici: kefe3
# ------------------------------------------------------------------

import os
import sys
import getpass
import socket
import platform
import subprocess
import tkinter as tk
from tkinter import messagebox

def get_distro():
    """Sistemin hangi tabanda olduğunu belirler."""
    if os.path.exists("/usr/bin/pacman"):
        return "Arch"
    elif os.path.exists("/usr/bin/apt"):
        return "Debian/Ubuntu"
    return "Generic Linux"

def open_gui():
    """Kapsül Serix Grafik Kontrol Panelini başlatır."""
    root = tk.Tk()
    root.title("SERIX OS - Amber Dashboard")
    root.geometry("450x600")
    root.configure(bg="#0d0d0d")

    # Başlık
    title = tk.Label(root, text="KAPSÜL SERIX", fg="#00ccff", bg="#0d0d0d", font=("Courier", 20, "bold"))
    title.pack(pady=25)

    subtitle = tk.Label(root, text="Terminal Control System v1.0", fg="#555", bg="#0d0d0d", font=("Courier", 10))
    subtitle.pack(pady=5)

    # Buton Fonksiyonları
    def run_cmd(command):
        root.destroy()
        os.system(command)

    # Buton Tasarımı
    btn_style = {"bg": "#1a1a1a", "fg": "#eee", "font": ("Arial", 11), "width": 25, "pady": 8}

    tk.Button(root, text="Sistemi Güncelle", command=lambda: run_cmd("sterm update"), **btn_style).pack(pady=10)
    tk.Button(root, text="Sistem Analizi", command=lambda: run_cmd("sterm check"), **btn_style).pack(pady=10)
    tk.Button(root, text="Hız Testi (Internet)", command=lambda: run_cmd("sterm speed"), **btn_style).pack(pady=10)
    tk.Button(root, text="Chroot'a Bağlan", command=lambda: run_cmd("sudo ./bin/arch-chroot ."), **btn_style).pack(pady=10)
    
    tk.Label(root, text="--------------------------", fg="#333", bg="#0d0d0d").pack(pady=15)
    
    tk.Button(root, text="PANELİ KAPAT", command=root.destroy, bg="#aa0000", fg="white", font=("Arial", 10, "bold"), width=20).pack(pady=10)

    root.mainloop()

def main():
    user = getpass.getuser()
    hostname = socket.gethostname()
    distro = get_distro()
    
    os.system('clear')
    print("\033[1;36m" + "="*50)
    print("  ⚡ STerm v1.0 - KAPSÜL SERIX TAKIMI ⚡")
    print("  " + "="*50)
    print(f"  CORE: {distro} | STATUS: Active | DEV: kefe3")
    print("="*50 + "\033[0m")

    while True:
        try:
            cwd = os.getcwd().replace(os.path.expanduser("~"), "~")
            prompt = f"\033[1;33m[SERIX]\033[0m \033[1;32m{user}@{hostname}\033[0m:\033[1;34m{cwd}\033[0m$ "
            
            user_input = input(prompt).strip()
            if not user_input: continue
            
            parts = user_input.split()
            cmd = parts[0]

            if cmd == "exit":
                print("\033[1;31mKapsül Serix bağlantısı kesiliyor...\033[0m")
                break
            
            elif cmd == "gui":
                print("\033[1;35mAmber Dashboard başlatılıyor...\033[0m")
                open_gui()

            elif cmd == "serix-get":
                target = " ".join(parts[1:])
                if distro == "Arch":
                    os.system(f"sudo pacman -S --noconfirm {target}")
                else:
                    os.system(f"sudo apt update && sudo apt install -y {target}")

            elif cmd == "check":
                print("\n\033[1;32m[SİSTEM DURUMU]\033[0m")
                os.system("free -h")
                os.system("df -h / | tail -1")

            elif cmd == "speed":
                print("\033[1;33mİnternet hızı ölçülüyor (Kapsül Test)...\033[0m")
                os.system("curl -s https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py | python3 -")

            elif cmd == "help":
                print("\n\033[1;35m--- STerm v1.0 Komut Listesi ---\033[0m")
                print(" gui          : Grafik kontrol panelini açar.")
                print(" serix-get    : Hibrit paket yükleyici.")
                print(" check        : RAM ve Disk durumunu gösterir.")
                print(" speed        : İnternet hızını ölçer.")
                print(" clear        : Ekranı temizler.")
                print(" exit         : Kapsül Serix'ten çıkar.")
                print("--------------------------------\n")

            elif cmd == "clear":
                os.system('clear')

            else:
                # Bilinmeyen komutları sistemin kendisine gönderir
                os.system(user_input)
        
        except KeyboardInterrupt:
            print("\n\033[1;31mÇıkmak için 'exit' yazın.\033[0m")
        except EOFError:
            break

if __name__ == "__main__":
    main()
