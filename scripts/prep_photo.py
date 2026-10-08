import cv2
import numpy as np
from PIL import Image
from rembg import remove
import sys
import os

def prep_photo(input_path, output_path="source-prepped.png"):
    if not os.path.exists(input_path):
        print(f"Erreur : L'image '{input_path}' est introuvable.")
        sys.exit(1)

    print("1. Suppression de l'arrière-plan (rembg)...")
    with open(input_path, 'rb') as i:
        input_image = i.read()
        output_image = remove(input_image)

    temp_no_bg = "temp_no_bg.png"
    with open(temp_no_bg, 'wb') as o:
        o.write(output_image)

    print("2. Traitement des contrastes et composition sur fond blanc...")
    fg = Image.open(temp_no_bg).convert("RGBA")
    bg = Image.new("RGBA", fg.size, (255, 255, 255, 255))
    combined = Image.alpha_composite(bg, fg).convert("L")

    img_cv = np.array(combined)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(img_cv)

    cv2.imwrite(output_path, enhanced)
    if os.path.exists(temp_no_bg):
        os.remove(temp_no_bg)

    print(f"Succès ! Image préparée enregistrée sous : {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/prep_photo.py <votre_photo.jpg>")
        sys.exit(1)
    prep_photo(sys.argv[1])