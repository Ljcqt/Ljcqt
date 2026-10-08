import json
import os

def render_heatmap():
    if not os.path.exists("data/contributions.json"):
        print("Erreur : data/contributions.json introuvable.")
        return

    with open("data/contributions.json", "r", encoding="utf-8") as f:
        days = json.load(f)

    PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353", "#69f0a0"]
    WIDTH = 860
    HEIGHT = 160
    
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="100%" height="100%">',
        '<style>',
        '  .bg { fill: #0d1117; }',
        '  .text { font-family: monospace; font-size: 12px; fill: #8b949e; }',
        '  .box { rx: 3px; ry: 3px; transition: fill 0.3s ease; }',
        '</style>',
        f'<rect width="100%" height="100%" class="bg" rx="6" />',
        '<g transform="translate(20, 30)">'
    ]

    box_size = 11
    gap = 4
    x_offset = 0
    y_offset = 0
    
    for i, day in enumerate(days):
        day_of_week = i % 7
        if day_of_week == 0 and i > 0:
            x_offset += box_size + gap
        
        y_offset = day_of_week * (box_size + gap)
        color = PALETTE[min(day['level'], len(PALETTE)-1)]
        
        svg.append(f'  <rect x="{x_offset}" y="{y_offset}" width="{box_size}" height="{box_size}" fill="{color}" class="box"><title>{day["date"]}: {day["count"]} contributions</title></rect>')

    svg.extend([
        '</g>',
        '</svg>'
    ])

    with open("contrib-heatmap.svg", "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print("Succès ! contrib-heatmap.svg généré.")

if __name__ == "__main__":
    render_heatmap()