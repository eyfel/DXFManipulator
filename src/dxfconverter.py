import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import os
import glob
import ezdxf
from ezdxf.addons.drawing import RenderContext, Frontend
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend
import matplotlib.pyplot as plt
import re

class DxfConverter:
    def __init__(self):
        self.img_format = '.png'
        self.img_res = 640
        self.bg_color = '#FFFFFF'

    def convert_dxf(self, folder_path, img_format, img_res, bg_color):
        dxf_files = glob.glob(os.path.join(folder_path, '*.dxf'))
        if not dxf_files:
            raise FileNotFoundError("No DXF files found in the selected folder.")
        for file_path in dxf_files:
            doc = ezdxf.readfile(file_path)
            msp = doc.modelspace()
            auditor = doc.audit()
            if len(auditor.errors) != 0:
                print(f"This DXF document is damaged and can't be converted: {file_path}")
                continue
            fig = plt.figure()
            ax = fig.add_axes([0, 0, 1, 1])
            ctx = RenderContext(doc)
            out = MatplotlibBackend(ax)
            ctx.set_current_layout(msp)
            ezdxf.addons.drawing.properties.MODEL_SPACE_BG_COLOR = bg_color
            Frontend(ctx, out).draw_layout(msp, finalize=True)
            img_name = re.sub(r'\.dxf$', img_format, os.path.basename(file_path), flags=re.I)
            fig.savefig(os.path.join(folder_path, img_name), dpi=img_res)
            print(f"{file_path} Converted Successfully to {img_name}")

class GUI:
    def __init__(self, master):
        self.master = master
        self.converter = DxfConverter()
        self.setup_ui()

    def setup_ui(self):
        self.master.title('DXF Converter')
        self.master.geometry('400x320')

        ttk.Label(self.master, text="Select Folder:").pack(pady=5)
        ttk.Button(self.master, text="Browse", command=self.browse_folder).pack(pady=5)

        self.folder_path_var = tk.StringVar()
        self.folder_path_label = ttk.Label(self.master, textvariable=self.folder_path_var)
        self.folder_path_label.pack(pady=5)

        ttk.Label(self.master, text="Image Format:").pack(pady=5)
        self.format_var = tk.StringVar(value='.png')
        self.format_combobox = ttk.Combobox(self.master, textvariable=self.format_var, values=['.png', '.pdf', '.jpg', '.tiff'], state='readonly')
        self.format_combobox.pack(pady=5)

        ttk.Label(self.master, text="Image Resolution (DPI):").pack(pady=5)
        self.res_var = tk.IntVar(value=640)
        self.res_entry = ttk.Entry(self.master, textvariable=self.res_var)
        self.res_entry.pack(pady=5)

        ttk.Label(self.master, text="Background Color:").pack(pady=5)
        self.bg_color_var = tk.StringVar(value='White')
        self.bg_color_combobox = ttk.Combobox(self.master, textvariable=self.bg_color_var, values=['White', 'Black', 'Red', 'Blue'], state='readonly')
        self.bg_color_combobox.pack(pady=5)

        ttk.Button(self.master, text="Convert", command=self.convert).pack(pady=10)

    def browse_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.folder_path_var.set(folder_selected)

    def convert(self):
        folder_path = self.folder_path_var.get()
        img_format = self.format_var.get()
        img_res = int(self.res_var.get())
        bg_color = self.bg_color_combobox.get()

        color_codes = {'White': '#FFFFFF', 'Black': '#000000', 'Red': '#FF0000', 'Blue': '#0000FF'}
        bg_color_code = color_codes[bg_color]

        if not folder_path:
            messagebox.showerror("Error", "Please select a folder containing DXF files.")
            return
        
        try:
            self.converter.convert_dxf(folder_path, img_format, img_res, bg_color_code)
            messagebox.showinfo("Success", "DXF files were successfully converted.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()
