import tkinter as tk
from ezdxf import readfile
from os.path import basename
from tkinter import filedialog


def number_incrementer(number_str):
    incremented_number = int(number_str) + 1
    
    return str(incremented_number)

def add_codes_to_dxf(file_path, search_text, title_prefix, start_code_str):
    try:
        doc = readfile(file_path)
    except Exception as e:
        print(f"Error: {e}")
        return

    msp = doc.modelspace()
    code_number_str = start_code_str

    for mtext in msp.query('MTEXT'):
        if search_text.lower() in mtext.text.lower():
            new_code = f"{title_prefix}{code_number_str}"
            mtext.text = f"{mtext.text}\n{new_code}"
            code_number_str = number_incrementer(code_number_str)

    file_name = basename(file_path)
    new_file_name = file_name.replace('.dxf', '_modified.dxf')
    doc.saveas(new_file_name)
    print(f"Changes saved: {new_file_name}")
    return new_file_name


def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("DXF Files", "*.dxf")])
    if file_path:
        file_path_label.config(text=file_path)
        return file_path
    else:
        file_path_label.config(text="No file selected.")
        return None

def process_file():
    file_path = file_path_label.cget("text")
    if file_path == "No file selected." or not file_path:
        print("No file selected.")
        return
    search_text = search_entry.get()
    title_prefix = title_prefix_entry.get()
    start_code_str = start_code_entry.get()
    new_file_path = add_codes_to_dxf(file_path, search_text, title_prefix, start_code_str)
    if new_file_path:
        result_label.config(text=f"Operation completed: {new_file_path}")
    else:
        result_label.config(text="An error occurred during the process.")

def show_examples():
    example_message = (
        "Search Text Example: 'MATERIAL'\n"
        "Title Prefix Example: 'CODE: HNS-01-'\n"
        "Start Number Example: '1'"
    )
    tk.messagebox.showinfo("Examples", example_message)

    
app = tk.Tk()
app.title("mTextManipulator")

frame = tk.Frame(app)
frame.pack(padx=10, pady=10)

help_button = tk.Button(frame, text="?", command=show_examples, width=3)
help_button.pack(pady=10)

file_path_label = tk.Label(frame, text="No file selected.")
file_path_label.pack()

open_button = tk.Button(frame, text="Select DXF File", command=open_file)
open_button.pack()


search_label = tk.Label(frame, text="Search Text")
search_label.pack()

search_entry = tk.Entry(frame)
search_entry.pack()

title_prefix_label = tk.Label(frame, text="Title Prefix")
title_prefix_label.pack()

title_prefix_entry = tk.Entry(frame)
title_prefix_entry.pack()

start_code_label = tk.Label(frame, text="Start Number")
start_code_label.pack()

start_code_entry = tk.Entry(frame)
start_code_entry.pack()

process_button = tk.Button(frame, text="EDIT", command=process_file)
process_button.pack()

result_label = tk.Label(frame, text="")
result_label.pack()

app.mainloop()
