import os
import glob
import tkinter as tk
from tkinter import filedialog, messagebox

def rename_files(prefix, folder_path):
    for root, dirs, files in os.walk(folder_path):
        for extension in ("*.dwg", "*.dxf"):
            for file_path in glob.glob(os.path.join(root, extension)):
                file_dir, file_name = os.path.split(file_path)
                new_file_name = prefix + "-" + file_name
                new_file_path = os.path.join(file_dir, new_file_name)
                os.rename(file_path, new_file_path)

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_entry.delete(0, tk.END)
        folder_entry.insert(0, folder_path)

def rename():
    prefix = prefix_entry.get()
    folder_path = folder_entry.get()

    if not prefix or not folder_path:
        messagebox.showerror("Error", "Both prefix and folder must be provided")
        return

    try:
        rename_files(prefix, folder_path)
        messagebox.showinfo("Success", "Files renamed successfully")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

root = tk.Tk()
root.title("DWG/DXF File Renamer")

tk.Label(root, text="Prefix:").grid(row=0, column=0, padx=10, pady=10)
prefix_entry = tk.Entry(root)
prefix_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Folder:").grid(row=1, column=0, padx=10, pady=10)
folder_entry = tk.Entry(root)
folder_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Button(root, text="Browse", command=select_folder).grid(row=1, column=2, padx=10, pady=10)
tk.Button(root, text="Rename", command=rename).grid(row=2, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()
