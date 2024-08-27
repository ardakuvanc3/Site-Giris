import tkinter as tk

def update_coordinates():
    # Fare koordinatlarını al
    x, y = root.winfo_pointerx(), root.winfo_pointery()
    coordinates = f"X: {x} Y: {y}"
    label.config(text=coordinates)
    
    # Bir saniye sonra tekrar çalıştır
    root.after(100, update_coordinates)

# Ana pencereyi oluştur
root = tk.Tk()
root.title("Koordinat")

# Koordinatları göstermek için bir label oluştur
label = tk.Label(root, text="X: 0 Y: 0", font=("Helvetica", 16))
label.pack(padx=20, pady=20)

# Koordinatları güncellemeye başla
update_coordinates()

# Ana döngüyü çalıştır
root.mainloop()
