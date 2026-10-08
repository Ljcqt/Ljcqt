import cv2
import numpy as np

def generate_ascii_svg(image_path="source-prepped.png", output_svg="avi-ascii.svg"):
    COLS = 100
    RAMP = " .`:-=+*cs#%@"

    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"Erreur : Impossible de lire {image_path}. Exécutez d'abord prep_photo.py")
        return

    h, w = img.shape
    aspect_ratio = h / w
    ROWS = int(COLS * aspect_ratio * 0.55)

    img_resized = cv2.resize(img, (COLS, ROWS))

    lines = []
    for row in img_resized:
        line_str = ""
        for pixel in row:
            idx = int(pixel / 255 * (len(RAMP) - 1))
            line_str += RAMP[idx]
        lines.append(line_str)

    svg_lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {COLS * 7.2} {ROWS * 13.5}" width="100%" height="100%">',
        '<style>',
        '  text { font-family: monospace; font-size: 11px; fill: #c9d1d9; }',
        '  .bg { fill: #0d1117; }',
        '  @keyframes typing {',
        '    from { clip-path: inset(0 100% 0 0); }',
        '    to { clip-path: inset(0 0% 0 0); }',
        '  }',
        '  .row {',
        '    animation: typing 1.2s steps(100, end) forwards;',
        '    opacity: 0;',
        '    animation-fill-mode: forwards;',
        '  }',
    ]

    for i in range(ROWS):
        delay = i * 0.03
        svg_lines.append(f'  .r{i} {{ animation-delay: {delay:.2f}s; opacity: 1; }}')

    svg_lines.extend([
        '</style>',
        f'<rect width="100%" height="100%" class="bg" rx="6" />',
        '<g transform="translate(10, 20)">'
    ])

    for i, line in enumerate(lines):
        safe_line = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace(" ", "&#160;")
        svg_lines.append(f'  <text x="0" y="{i * 13}" class="row r{i}">{safe_line}</text>')

    svg_lines.extend([
        '</g>',
        '</svg>'
    ])

    with open(output_svg, "w", encoding="utf-8") as f:
        f.write("\n".join(svg_lines))

    print(f"Succès ! Fichier ASCII SVG généré : {output_svg}")

if __name__ == "__main__":
    generate_ascii_svg()