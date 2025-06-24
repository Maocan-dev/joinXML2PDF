import os
import html
import pdfkit
from PyPDF2 import PdfMerger

# ⚙️ Configura la ruta a wkhtmltopdf
config = pdfkit.configuration(
    wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
)

def convert_xml_to_pdf(xml_path, output_pdf_path):
    with open(xml_path, "r", encoding="utf-8") as file:
        raw_xml = file.read()

    escaped_xml = html.escape(raw_xml)

    html_content = f"""
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            body {{ font-family: Consolas, monospace; padding: 20px; }}
            pre {{
                white-space: pre-wrap;
                word-wrap: break-word;
                background-color: #f4f4f4;
                padding: 10px;
                border-radius: 5px;
                border: 1px solid #ccc;
            }}
        </style>
    </head>
    <body>
        <h2>{os.path.basename(xml_path)}</h2>
        <pre>{escaped_xml}</pre>
    </body>
    </html>
    """

    pdfkit.from_string(html_content, output_pdf_path, configuration=config)

def merge_with_base_pdf(base_pdf_path, xml_pdf_path, output_path):
    merger = PdfMerger()
    merger.append(base_pdf_path)
    merger.append(xml_pdf_path)
    merger.write(output_path)
    merger.close()

def process_folder(xml_folder, base_pdf_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(xml_folder):
        if filename.lower().endswith(".xml"):
            base_name = os.path.splitext(filename)[0]
            xml_path = os.path.join(xml_folder, filename)

            xml_pdf_path = os.path.join(output_folder, f"{base_name}(xml).pdf")
            base_pdf_path = os.path.join(base_pdf_folder, f"{base_name}.pdf")
            merged_pdf_path = os.path.join(output_folder, f"{base_name}(merged).pdf")

            print(f"\n📄 Procesando: {filename}")
            convert_xml_to_pdf(xml_path, xml_pdf_path)

            if os.path.exists(base_pdf_path):
                merge_with_base_pdf(base_pdf_path, xml_pdf_path, merged_pdf_path)
                print(f"✅ Fusionado: {base_name}(merged).pdf")
            else:
                print(f"⚠️  No se encontró el PDF base para: {base_name}.pdf")

if __name__ == "__main__":
    print("🔧 Conversor y Fusionador XML+PDF")
    print("\n⚠️  IMPORTANTE:")
    print("   - Instalar wkhtmltopdf desde: https://wkhtmltopdf.org/downloads.html")
    print('   - Asegurarse de tenerlo instalado en:')
    print('     "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"\n')

    xml_folder = input("📁 Ruta de carpeta con archivos XML: ").strip('"')
    base_pdf_folder = input("📁 Ruta de carpeta con PDFs base: ").strip('"')
    output_folder = input("📁 Carpeta de salida para PDFs finales: ").strip('"')

    if not os.path.isdir(xml_folder):
        print("❌ Carpeta XML no válida.")
    elif not os.path.isdir(base_pdf_folder):
        print("❌ Carpeta de PDFs base no válida.")
    else:
        process_folder(xml_folder, base_pdf_folder, output_folder)
        print("\n🚀 Proceso terminado.")
