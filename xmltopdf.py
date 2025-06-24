import os
import pdfkit
import html

# Ruta al ejecutable de wkhtmltopdf
config = pdfkit.configuration(
    wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    
)

def convert_xml_to_pdf(xml_path, pdf_path):
    with open(xml_path, 'r', encoding='utf-8') as file:
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

    pdfkit.from_string(html_content, pdf_path, configuration=config)

def convert_all_xmls_in_folder(folder_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.xml'):
            xml_path = os.path.join(folder_path, filename)
            pdf_filename = os.path.splitext(filename)[0] + '(xml).pdf'
            pdf_path = os.path.join(output_folder, pdf_filename)

            print(f"Convirtiendo: {filename} → {pdf_filename}")
            convert_xml_to_pdf(xml_path, pdf_path)

if __name__ == "__main__":
    print("== Conversor de XML a PDF ==")
    input_folder = input("Ingresa la ruta de la carpeta con archivos XML: ").strip('"')
    output_folder = input("Ingresa la ruta de la carpeta de salida para los PDFs: ").strip('"')

    if not os.path.isdir(input_folder):
        print("❌ La carpeta de entrada no existe.")
    else:
        convert_all_xmls_in_folder(input_folder, output_folder)
        print("\n✅ Conversión completada.")
