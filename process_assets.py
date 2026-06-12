import os
import zipfile
import subprocess
import sys

# Auto-install dependencies if missing
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import fitz  # PyMuPDF
except ImportError:
    print("Installing PyMuPDF...")
    install('pymupdf')
    import fitz

try:
    from PIL import Image
except ImportError:
    print("Installing Pillow...")
    install('Pillow')
    from PIL import Image

zip_path = r"C:\Users\sarju\Desktop\RIVER WALK EVENTS-LEO GROUP-pages.zip"
extract_dir = r"d:\internship work\LEO CONV CENTRE\assets\raw_pdfs"
output_dir = r"d:\internship work\LEO CONV CENTRE\assets"

os.makedirs(extract_dir, exist_ok=True)

print("Extracting ZIP file...")
try:
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
except Exception as e:
    print(f"Failed to extract ZIP: {e}")
    sys.exit(1)

print("Converting PDFs to high-quality WebP...")
count = 0
for root, _, files in os.walk(extract_dir):
    for file in files:
        if file.lower().endswith(".pdf"):
            pdf_path = os.path.join(root, file)
            print(f"\nProcessing {file}...")
            
            try:
                doc = fitz.open(pdf_path)
                for page_num in range(len(doc)):
                    page = doc.load_page(page_num)
                    
                    # Render at 3x scale for massive high-res quality
                    mat = fitz.Matrix(3.0, 3.0)
                    pix = page.get_pixmap(matrix=mat)
                    
                    # Convert to Pillow Image
                    mode = "RGBA" if pix.alpha else "RGB"
                    img = Image.frombytes(mode, [pix.width, pix.height], pix.samples)
                    
                    # Cap width at 1920px to prevent bloated file sizes
                    if img.width > 1920:
                        ratio = 1920 / img.width
                        new_h = int(img.height * ratio)
                        img = img.resize((1920, new_h), Image.Resampling.LANCZOS)

                    # Generate clean filename
                    base_name = os.path.splitext(file)[0].replace(" ", "_").lower()
                    out_name = f"{base_name}_p{page_num+1}.webp"
                    out_path = os.path.join(output_dir, out_name)
                    
                    # Save as compressed WebP
                    img.save(out_path, "WEBP", quality=85)
                    size_kb = os.path.getsize(out_path) // 1024
                    print(f"  -> Saved {out_name} ({size_kb} KB)")
                    count += 1
                doc.close()
            except Exception as e:
                print(f"  -> Error processing {file}: {e}")

print("\nCleaning up temporary PDF files...")
import shutil
shutil.rmtree(extract_dir)

print(f"\nSUCCESS: Converted {count} images and saved to the assets folder.")
