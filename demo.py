import os
import hashlib
import pyautogui
import time
import subprocess
from pynput import keyboard
from koordinatlar import *

kullanici_adi = "ali"
sifre = "ali.123"
site_linki = ""
chrome_yolu = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
marker_file = "demo_usage.marker"
max_usage = 5

def get_hash(usage_count):
    return hashlib.sha256(str(usage_count).encode()).hexdigest()

def verify_hash(usage_count, stored_hash):
    return get_hash(usage_count) == stored_hash

if os.path.exists(marker_file):
    with open(marker_file, 'r') as file:
        content = file.read().strip().split(':')
        usage_count = int(content[0])
        stored_hash = content[1]

        if not verify_hash(usage_count, stored_hash):
            print("Hata: Dosya manipüle edilmiş. Program kapanıyor.")
            exit()
else:
    usage_count = 0

if usage_count >= max_usage:
    print(f"Bu demo sürümü {max_usage} kez kullanıldı. Program kapanıyor.")
    exit()

stop_program = False

def on_press(key):
    global stop_program
    try:
        if key.char == 'q':
            stop_program = True
            return False
    except AttributeError:
        pass

listener = keyboard.Listener(on_press=on_press)
listener.start()

def run_tasks():
    global stop_program

    subprocess.Popen(chrome_yolu)
    time.sleep(3)

    if stop_program: return
    tıkla(1811, 61)
    if stop_program: return
    tıkla(1617, 213)
    if stop_program: return
    tıkla(1708, 166)
    if stop_program: return
    tıkla(929, 62)
    if stop_program: return
    pyautogui.typewrite(site_linki)
    pyautogui.press("enter")
    time.sleep(5)
    if stop_program: return
    tıkla(1627, 111)
    if stop_program: return
    tıkla(936, 452)
    if stop_program: return
    pyautogui.typewrite(kullanici_adi)
    if stop_program: return
    tıkla(922, 547)
    if stop_program: return
    pyautogui.typewrite(sifre)
    if stop_program: return
    tıkla(967, 751)
    if stop_program: return
    tıkla(20, 1059)
    if stop_program: return
    pyautogui.typewrite("mig")
    pyautogui.press("enter")
    time.sleep(20)
    if stop_program: return
    tıkla(474, 154)
    if stop_program: return
    pyautogui.doubleClick(894, 788)
    if stop_program: return
    pyautogui.hotkey('ctrl', 'c')
    if stop_program: return
    pyautogui.hotkey('alt', 'tab')
    if stop_program: return
    tıkla(958, 535)
    if stop_program: return
    pyautogui.hotkey('ctrl', 'v')
    if stop_program: return
    tıkla(958, 579)
    if stop_program: return
    tıkla(761, 159)

run_tasks()

usage_count += 1
hash_value = get_hash(usage_count)
with open(marker_file, 'w') as file:
    file.write(f"{usage_count}:{hash_value}")

if stop_program:
    print("Program durduruldu.")
