import pyautogui
import time


def tıkla(x,y):
    pyautogui.click(x,y)
    
    
def secim_yap(start_x, start_y, end_x, end_y):

    # 1 saniye bekleyin, sonra fareyi başlangıç noktasına taşıyın ve tıklayın
    time.sleep(1)
    pyautogui.moveTo(start_x, start_y)
    pyautogui.mouseDown()

    # Fareyi sola doğru sürükleyerek metni seçin
    pyautogui.dragTo(end_x, end_y, duration=0.5)

    # Fareyi serbest bırakın
    pyautogui.mouseUp()

    # Ctrl + C ile seçilen metni kopyalayın
    pyautogui.hotkey('ctrl', 'c')
