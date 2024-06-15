## DWG/DXF File Renamer

DWG/DXF File Renamer is a Python-based GUI application that helps you easily organize your DWG and DXF files. By specifying a prefix and selecting a directory, this tool will rename all DWG and DXF files in that directory and its subdirectories by adding the given prefix at the beginning of each file name. This is especially useful for engineers, architects, and designers who need to maintain a consistent naming convention for their project files.

### Features:
- Simple and user-friendly interface.
- Allows you to specify any prefix to be added to the DWG and DXF files.
- Select any folder from your file system.
- Renames all DWG and DXF files in the selected folder and its subdirectories with the specified prefix.

### Requirements:
- Python 3.x
- Tkinter (usually comes pre-installed with Python)

### How to Use:
1. Run the `DWGFileRenamer.py` script.
2. Enter the desired prefix in the provided field.
3. Click on the "Browse" button to select the folder containing your DWG and DXF files.
4. Click on the "Rename" button to apply the prefix to all DWG and DXF files in the selected folder and its subdirectories.

### Example:
If you have a DWG file named `48019-0000-00.dwg` and a DXF file named `example.dxf` in different subdirectories and you specify the prefix `PNZC`, the files will be renamed to `PNZC-48019-0000-00.dwg` and `PNZC-example.dxf`.
