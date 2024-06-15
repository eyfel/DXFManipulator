import tkinter as tk
from tkinter import filedialog, messagebox
import ezdxf

def get_codes_and_quantities(dxf_file):
    try:
        doc = ezdxf.readfile(dxf_file)
        mtexts = doc.modelspace().query('MTEXT')
        codes = {}
        
        for mtext in mtexts:
            text = mtext.text
            if "KOD:" in text and "SAYI:" in text:
                kod = text.split("KOD:")[1].split()[0]
                sayi = int(text.split("SAYI:")[1].split()[0])
                codes[kod] = sayi
        return codes
    except Exception as e:
        print(f"Dosya okunurken hata oluştu: {str(e)}")
        return {}

def compare_dxf_files():
    if not file1_path.get() or not file2_path.get():
        print("Hata: Lütfen her iki dosyayı da seçin")
        return

    codes1 = get_codes_and_quantities(file1_path.get())
    codes2 = get_codes_and_quantities(file2_path.get())

    if not codes1 or not codes2:
        return

    codes1_set = set(codes1.keys())
    codes2_set = set(codes2.keys())
    
    not_in_file2 = codes1_set - codes2_set
    different_quantities = [code for code in codes1_set & codes2_set if codes1[code] != codes2[code]]
    
    print("2. dosyada olmayanlar:")
    if not not_in_file2:
        print("Yok")
    else:
        for item in not_in_file2:
            print(item)
    
    print("\nAdetleri tutmayanlar:")
    if not different_quantities:
        print("Yok")
    else:
        for item in different_quantities:
            print(item)

def select_file1():
    file_path = filedialog.askopenfilename(filetypes=[("DXF Files", "*.dxf")])
    if file_path:
        file1_path.set(file_path)

def select_file2():
    file_path = filedialog.askopenfilename(filetypes=[("DXF Files", "*.dxf")])
    if file_path:
        file2_path.set(file_path)

# Tkinter arayüzü
root = tk.Tk()
root.title("DXF Dosya Karşılaştırma")

file1_path = tk.StringVar()
file2_path = tk.StringVar()

tk.Label(root, text="Yeni Dosya Seç:").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=file1_path, width=50).grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Gözat", command=select_file1).grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Eski Dosya Seç:").grid(row=1, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=file2_path, width=50).grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Gözat", command=select_file2).grid(row=1, column=2, padx=10, pady=10)

tk.Button(root, text="Karşılaştır", command=compare_dxf_files).grid(row=2, column=0, columnspan=3, padx=10, pady=20)

root.mainloop()
