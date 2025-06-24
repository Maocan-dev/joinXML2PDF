import os
from PyPDF2 import PdfMerger

def merge_pdfs(xml_pdf_folder, base_pdf_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(xml_pdf_folder):
        if filename.endswith('(xml).pdf'):
            base_name = filename.replace('(xml).pdf', '')
            xml_pdf_path = os.path.join(xml_pdf_folder, filename)
            base_pdf_path = os.path.join(base_pdf_folder, f"{base_name}.pdf")

            if os.path.exists(base_pdf_path):
                merger = PdfMerger()
                merger.append(base_pdf_path)
                merger.append(xml_pdf_path)

                merged_output_path = os.path.join(output_folder, f"{base_name}.pdf")
                merger.write(merged_output_path)
                merger.close()

                print(f"✅ {base_name}.pdf creado.")
            else:
                print(f"⚠️  No se encontró el PDF base para: {base_name}")

if __name__ == "__main__":
    print("== Fusionador de PDFs ==")
    xml_pdf_folder = input("📁 Carpeta con PDFs tipo '(xml).pdf': ").strip('"')
    base_pdf_folder = input("📁 Carpeta con los PDFs base: ").strip('"')
    output_folder = input("📁 Carpeta de salida para PDFs fusionados: ").strip('"')

    merge_pdfs(xml_pdf_folder, base_pdf_folder, output_folder)
    print("\n🚀 Listo.")
