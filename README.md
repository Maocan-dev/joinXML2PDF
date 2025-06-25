# XML to PDF Merger — GUI Tool

## 📄 Description

This tool lets you convert XML files into formatted PDFs and automatically merge them with base PDFs that share the same filename. It features a graphical interface—no command line needed.

## ✨ Features

- Converts XML files into readable PDFs
- Finds a matching base PDF by name (e.g., `data.xml` + `data.pdf`)
- Merges both into a new `data(merged).pdf`
- Friendly GUI to select folders
- Real-time processing log

## 🖥️ Requirements

- Windows 10 or newer
- Python 3.8+ (only if running the `.py` script instead of `.exe`)
- Installed `wkhtmltopdf` tool (see below)
- Python libraries (only for `.py` script):
  ```bash
  pip install pdfkit PyPDF2
  ```

## 🛠️ wkhtmltopdf Installation

### Before running this tool, install wkhtmltopdf:

### Go to: https://wkhtmltopdf.org/downloads.html

### Download the Windows Installer (.msi version)

### Install it to the default location: C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe

## 🚀 Usage

Run the app (double-click the .exe or run the .py script)

Use the buttons to select three folders:

Folder containing XML files

Folder containing base PDFs (with matching names)

Output folder where merged PDFs will be saved

Click "Iniciar conversión" to start processing

Wait for the log to confirm successful merges

## 📝 Notes

The base PDF name must match the XML filename (ignoring extensions) Example:

FACTURA_123.xml + FACTURA_123.pdf ➝ FACTURA_123(merged).pdf
If no matching base PDF is found, a warning will be shown, and that XML will be skipped

All temporary files are cleaned automatically

## 🛟 Support

This tool was built for fast offline PDF merging with a clean interface. Feel free to extend it further — you have the code!

## 📥 Download

## To download the .exe file, go to:

### https://github.com/Maocan-dev/joinXML2PDF/tree/main/dist
