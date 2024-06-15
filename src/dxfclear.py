import ezdxf
import tkinter as tk
from tkinter import filedialog
import os

def remove_specified_entities(dxf_file_path):
    doc = ezdxf.readfile(dxf_file_path)
    modelspace = doc.modelspace()

    dimensions = modelspace.query('DIMENSION')
    for dim in dimensions:
        modelspace.delete_entity(dim)

    lines_to_delete = []
    lines_to_delete.extend(modelspace.query("LINE[linetype=='DASHED']"))
    lines_to_delete.extend(modelspace.query("LINE[linetype=='DOTTED']"))
    lines_to_delete.extend(modelspace.query("LWPOLYLINE[linetype=='DASHED']"))
    lines_to_delete.extend(modelspace.query("LWPOLYLINE[linetype=='DOTTED']"))

    for line in lines_to_delete:
        modelspace.delete_entity(line)

    save_file_path = os.path.splitext(dxf_file_path)[0] + "_modified.dxf"
    doc.saveas(save_file_path)
    return save_file_path


def select_file_and_process():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select a DXF file", filetypes=[("DXF files", "*.dxf")])
    if not file_path:
        print("No file selected.")
        return

    modified_file_path = remove_specified_entities(file_path)
    print(f"File processed and saved as {modified_file_path}")

if __name__ == "__main__":
    select_file_and_process()
