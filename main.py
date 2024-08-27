import pyautogui
import time
import subprocess
from pynput import keyboard
import pyperclip
from koordinatlar import *

# Kullanıcı bilgileri ve diğer parametreler
kullanici_adi = "kullanici_adi"
sifre = "sifre"
site_linki = "https://ornek-site.com"
chrome_yolu = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Global bir durdurma bayrağı
stop_program = False

def on_press(key):
    global stop_program
    try:
        if key.char == '+':  # '+' tuşuna basılırsa
            stop_program = True
            return False  # Dinleyiciyi durdur
    except AttributeError:
        pass

# Klavye dinleyicisini başlat
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Panodaki verinin bir kod olup olmadığını kontrol eden fonksiyon
def is_valid_code(text):
    return text.isdigit() and len(text) == 6  # Sadece 6 haneli sayısal bir kodu kabul eder

# Programın işlemlerini yapan fonksiyon
def run_tasks():
    global stop_program

    # Chrome'u açacak
    subprocess.Popen(chrome_yolu)
    time.sleep(3)

    if stop_program: return

    # Eklenti sembolüne tıklayacak
    tıkla(1811, 61)

    if stop_program: return

    # Proxy üzerine gelme sembolüne tıklayacak
    tıkla(1617, 213)

    if stop_program: return

    # Proxy sembolüne tıklayacak
    tıkla(1708, 166)

    if stop_program: return

    # URL'ye tıklayacak
    tıkla(929, 62)

    if stop_program: return

    pyautogui.typewrite(site_linki)

    pyautogui.press("enter")

    time.sleep(5)

    if stop_program: return

    # Girişine tıklama
    tıkla(1627, 111)

    if stop_program: return

    # Kullanıcı Adı girişine tıklama
    tıkla(936, 452)

    if stop_program: return

    pyautogui.typewrite(kullanici_adi)

    if stop_program: return

    # Şifre girişine tıklama
    tıkla(922, 547)

    if stop_program: return

    pyautogui.typewrite(sifre)

    if stop_program: return

    # Giriş butonuna tıklama
    tıkla(967, 751)

    if stop_program: return

    # Arama çubuğuna tıklayacağız
    tıkla(20, 1059)

    if stop_program: return

    pyautogui.typewrite("mig")
    pyautogui.press("enter")

    time.sleep(20)

    if stop_program: return

    # SMS adına tıklama
    tıkla(474, 154)


    # SMS Onay Kodunu Bekleme ve Kontrol Etme
    while True:
        time.sleep(10)

        if stop_program: return

        # SMS gelen bölgeye çift tıklama ve kopyalama işlemi
        pyautogui.doubleClick(894, 788)  # Koordinatları ayarlayın
        pyautogui.hotkey('ctrl', 'c')

        # Kopyalanan metni al
        time.sleep(1)  # Clipboard'un dolmasını beklemek için kısa bir gecikme
        clipboard_text = pyperclip.paste()

        # Kopyalanan metnin geçerli bir kod olup olmadığını kontrol et
        if is_valid_code(clipboard_text):
            
                if stop_program: return

                pyautogui.hotkey('alt', 'tab')

                if stop_program: return

                # SMS yerine tıklama
                tıkla(958, 535)

                if stop_program: return

                # SMS'i yapıştırma
                pyautogui.hotkey('ctrl', 'v')

                if stop_program: return

                # Giriş butonuna tıklama
                tıkla(958, 579)

                if stop_program: return

                # Özel Sekmeye tıklama
                tıkla(761, 159)

                print("Onay kodu bulundu ve giriş yapıldı.")
        else:
            print("Kopyalanan metin geçerli bir kod değil, beklemeye devam ediliyor...")

# Görevleri çalıştır
run_tasks()

# Program tamamen durdurulmuşsa
if stop_program:
    print("Program durduruldu.")
