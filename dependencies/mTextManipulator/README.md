# mTextManipulator

A Tool for Automating DXF Annotations

**Introduction**

The mTextManipulator is a Python application aimed at automating the process of annotating DXF files. Built using the Tkinter library for its graphical user interface (GUI) and relying on the `ezdxf` module to interact with DXF files, this tool provides a user-friendly way to add sequential codes to MTEXT entities based on specific search criteria.

**Features**

- **DXF File Selection**: Users can select the DXF file they wish to modify directly from their filesystem.
- **Case-Insensitive Search**: Implements a case-insensitive search functionality to find MTEXT entities containing a specified keyword or phrase, ensuring that all relevant entities are targeted regardless of their case.
- **Sequential Code Addition**: Allows users to specify a title prefix and a starting number, adding these as sequential codes to the identified MTEXT entities, which aids in categorizing and referencing within the DXF file.
- **User Guidance**: Includes a "?" help button that, when clicked, displays examples of valid inputs for search text, title prefix, and starting number, guiding users on how to effectively use the tool.

**How It Works**

Upon launching the mTextManipulator, users are greeted with a simple and intuitive interface. The process begins with selecting a DXF file, followed by entering the desired search text, title prefix, and starting number for the codes. The application then scans the selected DXF file for MTEXT entities that contain the specified search text, adding a new line with the title prefix and a sequentially incremented number to each matching entity.

**Examples**

- **Search Text Example**: 'MATERIAL'
- **Title Prefix Example**: 'CODE: HNS-01-'
- **Start Number Example**: '1'

These examples are provided to assist users in understanding the format and types of inputs expected by the application, ensuring a smooth and efficient user experience.

**Conclusion**

mTextManipulator streamlines the task of editing and annotating DXF files, making it an invaluable tool for engineers, architects, and designers who frequently work with CAD drawings. By automating what would otherwise be a manual and time-consuming process, it allows professionals to focus more on their design work and less on file management tasks.
