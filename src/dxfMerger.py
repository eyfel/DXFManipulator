import ezdxf 
import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import os 

def calculate_max_width(msp):
    max_x = 0
    for e in msp:
        if e.dxftype() == 'LINE':
            points = [e.dxf.start, e.dxf.end]
        elif e.dxftype() == 'LWPOLYLINE':
            points = e.get_points('xy')
        else:
            continue 

        max_point_x = max(points, key=lambda point: point[0])[0]
        max_x = max(max_x, max_point_x)
    
    return max_x 


def merge_dxf_files(dxf_paths, output_path, spacing=100):
    merged_doc = ezdxf.new(dxfversion='R2010')
    merged_msp = merged_doc.modelspace() 
    current_offset = 0 

    for dxf_path in dxf_paths:
        doc = ezdxf.readfile(dxf_path)
        msp = doc.modelspace()

        width = calculate_max_width(msp)
        
        for e in msp:
            e = e.copy()
            if e.dxftype() in {'LINE', 'LWPOLYLINE', 'DIMENSION', 'TEXT', 'MTEXT'}:
                e.translate(current_offset + spacing, 0, 0)
                merged_msp.add_entity(e)

        current_offset += width + spacing

    merged_doc.saveas(output_path)

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DXF Merger")
        self.geometry("400x200")
        self.create_widgets()

    def create_widgets(self):

        ttk.Label(self, text="Select a folder containing DXF files:").pack(pady=10)
        self.folder_path_var = tk.StringVar()
        ttk.Entry(self, textvariable=self.folder_path_var, state='readonly', width=50).pack(pady=5)
        ttk.Button(self, text="Browse", command=self.browse_folder).pack(pady=5)
        ttk.Button(self, text="Merge DXF Files", command=self.merge_files).pack(pady=10)

    def browse_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.folder_path_var.set(folder_selected)

    def merge_files(self):
        folder_path = self.folder_path_var.get()
        if not folder_path:
            messagebox.showerror("Error", "Please select a folder.")
            return

        dxf_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.dxf')]
        if not dxf_files:
            messagebox.showerror("Error", "No DXF files found in the selected folder.")
            return

        output_path = os.path.join(folder_path, 'merged.dxf')
        merge_dxf_files(dxf_files, output_path, spacing=100)
        messagebox.showinfo("Success", f"DXF files have been merged into {output_path}")

if __name__ == "__main__":
    app = Application()
    app.mainloop()
