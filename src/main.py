import threading
import subprocess
import tkinter as tk
from tkinter import ttk
import os

def run_script_in_thread(script_path):
    def run_script():
        try:
            if not os.path.exists(script_path):
                print(f"File not found: {script_path}")
                return

            script_dir = os.path.dirname(script_path)
            os.chdir(script_dir)

            subprocess.run(["python", os.path.basename(script_path)], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Script execution error: {e}")
    thread = threading.Thread(target=run_script)
    thread.start()

def run_mTextManipulator():
    run_script_in_thread("dependencies\\mTextManipulator\\mTextManipulator.py")

def run_dxf2exec():
    run_script_in_thread("dependencies\\dxf2exec\\dfxexec.py")

def run_dfxconverter():
    run_script_in_thread("src\\dxfconverter.py")

def run_dfxclear():
    run_script_in_thread("src\\dxfclear.py")

def run_dxfMerger():
    run_script_in_thread("src\\dxfMerger.py")

def run_dxfFileRenamer():
    run_script_in_thread("dependencies\\DXF-DWGFileRenamer\\main.py")

def run_dxfComparator():
    run_script_in_thread("src\\dxfComparator.py")

def run_clipboard2PDF():
    run_script_in_thread("dependencies\\Clipboard2PDF\\main.py")

root = tk.Tk()
root.title("DXF Script Runner")

window_width = 300
window_height = 470
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int((screen_width/2) - (window_width/2))
y_coordinate = int((screen_height/2) - (window_height/2))
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

info_text = tk.Label(root, text="Select the scripts you wish to run", font=("Arial", 14), pady=10)
info_text.pack()

info_text = tk.Label(root, text="Only for DXF files", font=("Arial", 14))
info_text.pack()

button1 = ttk.Button(root, text="mText editor", command=run_mTextManipulator)
button1.pack(pady=10)

button2 = ttk.Button(root, text="Extract texts to Excel", command=run_dxf2exec)
button2.pack(pady=10)

button3 = ttk.Button(root, text="Convert files", command=run_dfxconverter)
button3.pack(pady=10)

button4 = ttk.Button(root, text="Clear files", command=run_dfxclear)
button4.pack(pady=10)

button5 = ttk.Button(root, text="Merge files", command=run_dxfMerger)
button5.pack(pady=10)

button6 = ttk.Button(root, text="Rename DXF-DWG Files", command=run_dxfFileRenamer)
button6.pack(pady=10)

button7 = ttk.Button(root, text="Compare DXF Files", command=run_dxfComparator)
button7.pack(pady=10)

button8 = ttk.Button(root, text="Clipboard to PDF", command=run_clipboard2PDF)
button8.pack(pady=10)

root.mainloop()
