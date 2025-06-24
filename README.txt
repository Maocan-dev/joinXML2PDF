==============================
XML to PDF Merger — GUI Tool
==============================

DESCRIPTION:
------------
This tool lets you convert XML files into formatted PDFs and automatically merge them with base PDFs
that share the same filename. It features a graphical interface (no command line needed).

FEATURES:
---------
- Converts XML files into readable PDFs.
- Finds a matching base PDF by name (e.g., data.xml + data.pdf).
- Merges both into a new "data(merged).pdf".
- Friendly GUI to select folders.
- Real-time processing log.

REQUIREMENTS:
-------------
- Windows 10 or newer.
- Python 3.8+ (only if running the .py script instead of .exe).
- Installed wkhtmltopdf tool (see below).
- Python libraries (only for .py script):
    pip install pdfkit PyPDF2

WKHMTLTOPDF INSTALLATION:
-------------------------
Before running this tool, install wkhtmltopdf:
1. Go to: https://wkhtmltopdf.org/downloads.html
2. Download the Windows Installer (.msi version).
3. Install it to the default location:
   C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe

USAGE:
------
1. Run the app (double-click the .exe or run the .py script).
2. Use the buttons to select three folders:
   - Folder containing XML files.
   - Folder containing base PDFs (with matching names).
   - Output folder where merged PDFs will be saved.
3. Click "Iniciar conversión" to start processing.
4. Wait for the log to confirm successful merges.

NOTES:
------
- The base PDF name must match the XML filename (ignoring extensions).
  For example:
    FACTURA_123.xml + FACTURA_123.pdf ➝ FACTURA_123(merged).pdf
- If no matching base PDF is found, a warning will be shown, and that XML will be skipped.
- All temporary files are cleaned automatically.

SUPPORT:
--------
This tool was built for fast offline PDF merging with a clean interface.
Feel free to extend it further — you have the code!

DOWNLOAD:
---------
to download the .exe file, go to:
https://github.com/Maocan-dev/joinXML2PDF/tree/main/dist


________________________________________________________________________________________________