import os
import html
import pdfkit
import tempfile
from PyPDF2 import PdfMerger
import tkinter as tk
from tkinter import filedialog, messagebox

config = pdfkit.configuration(
    wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
)

def convert_xml_to_temp_pdf(xml_path):
    with open(xml_path, "r", encoding="utf-8") as file:
        raw_xml = file.read()

    escaped_xml = html.escape(raw_xml)
    html_content = f"""
    <html><head><meta charset="UTF-8"><style>
    body {{ font-family: Consolas, monospace; padding: 20px; }}
    pre {{
        white-space: pre-wrap;
        word-wrap: break-word;
        background-color: #f4f4f4;
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #ccc;
    }}</style></head>
    <body><h2>{os.path.basename(xml_path)}</h2><pre>{escaped_xml}</pre></body></html>
    """

    temp_pdf = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    pdfkit.from_string(html_content, temp_pdf.name, configuration=config)
    return temp_pdf.name

def merge_pdfs(base_pdf_path, xml_pdf_path, output_path):
    merger = PdfMerger()
    merger.append(base_pdf_path)
    merger.append(xml_pdf_path)
    merger.write(output_path)
    merger.close()

def process(xml_folder, base_pdf_folder, output_folder, status_box):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(xml_folder):
        if filename.lower().endswith(".xml"):
            base_name = os.path.splitext(filename)[0]
            xml_path = os.path.join(xml_folder, filename)
            base_pdf = os.path.join(base_pdf_folder, f"{base_name}.pdf")
            merged_pdf = os.path.join(output_folder, f"{base_name}(ok).pdf")

            status_box.insert(tk.END, f"📄 Procesando {filename}...\n")
            try:
                temp_xml_pdf = convert_xml_to_temp_pdf(xml_path)
                if os.path.exists(base_pdf):
                    merge_pdfs(base_pdf, temp_xml_pdf, merged_pdf)
                    status_box.insert(tk.END, f"✅ Fusionado: {base_name}(merged).pdf\n\n")
                else:
                    status_box.insert(tk.END, f"⚠️  No se encontró base PDF: {base_name}.pdf\n\n")
                os.unlink(temp_xml_pdf)  # Limpia el archivo temporal
            except Exception as e:
                status_box.insert(tk.END, f"❌ Error en {filename}: {e}\n\n")
            status_box.update_idletasks()

def select_folder(entry):
    path = filedialog.askdirectory()
    if path:
        entry.delete(0, tk.END)
        entry.insert(0, path)

def start_gui():
    root = tk.Tk()
    root.title("Conversor y Fusionador XML + PDF")

    tk.Label(root, text="📁 Carpeta XMLs:").grid(row=0, column=0, sticky='w')
    tk.Label(root, text="📁 Carpeta PDFs base:").grid(row=1, column=0, sticky='w')
    tk.Label(root, text="📁 Carpeta salida:").grid(row=2, column=0, sticky='w')

    entry_xml = tk.Entry(root, width=50)
    entry_base = tk.Entry(root, width=50)
    entry_out = tk.Entry(root, width=50)
    entry_xml.grid(row=0, column=1)
    entry_base.grid(row=1, column=1)
    entry_out.grid(row=2, column=1)

    tk.Button(root, text="Seleccionar", command=lambda: select_folder(entry_xml)).grid(row=0, column=2)
    tk.Button(root, text="Seleccionar", command=lambda: select_folder(entry_base)).grid(row=1, column=2)
    tk.Button(root, text="Seleccionar", command=lambda: select_folder(entry_out)).grid(row=2, column=2)

    status_box = tk.Text(root, height=20, width=80)
    status_box.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

    def run():
        xml_dir = entry_xml.get()
        base_dir = entry_base.get()
        out_dir = entry_out.get()
        if not os.path.isdir(xml_dir) or not os.path.isdir(base_dir):
            messagebox.showerror("Error", "📌 Verifica que las carpetas de entrada existan.")
            return
        status_box.delete("1.0", tk.END)
        process(xml_dir, base_dir, out_dir, status_box)
        status_box.insert(tk.END, "🎉 Proceso completado.\n")

    tk.Button(root, text="Iniciar conversión", command=run).grid(row=3, column=1, pady=10)

    tk.Label(root, text="⚠️  Asegúrate de tener wkhtmltopdf instalado en:\n    C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe", fg='gray').grid(row=5, column=0, columnspan=3, pady=(0, 10))

    root.mainloop()

if __name__ == "__main__":
    start_gui()
