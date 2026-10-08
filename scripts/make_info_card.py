def generate_info_card():
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 490 300" width="100%" height="100%">
  <style>
    .bg { fill: #0d1117; }
    .text { font-family: monospace; font-size: 13px; fill: #c9d1d9; }
    .bold { font-weight: bold; fill: #58a6ff; }
    .green { fill: #39d353; }
    .fade { opacity: 0; animation: fadeIn 0.8s ease forwards; }
    @keyframes fadeIn { to { opacity: 1; } }
    .d1 { animation-delay: 0.2s; }
    .d2 { animation-delay: 0.4s; }
    .d3 { animation-delay: 0.6s; }
    .d4 { animation-delay: 0.8s; }
  </style>
  <rect width="100%" height="100%" class="bg" rx="6" />
  <g transform="translate(20, 30)">
    <text x="0" y="0" class="text bold fade d1">ljcqt@github-profile</text>
    <text x="0" y="20" class="text fade d1">------------------------</text>
    <text x="0" y="45" class="text fade d2"><tspan class="bold">Role:</tspan> Student / Developer</text>
    <text x="0" y="70" class="text fade d2"><tspan class="bold">Stack:</tspan> Python, C++, Linux, RAG</text>
    <text x="0" y="95" class="text fade d3"><tspan class="bold">Focus:</tspan> Applied Math &amp; CS</text>
    <text x="0" y="120" class="text fade d3"><tspan class="bold">Hobbies:</tspan> Escape Games, Running</text>
    <text x="0" y="150" class="text green fade d4">status: compiling ideas...</text>
  </g>
</svg>"""
    with open("info-card.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("Succès ! info-card.svg généré.")

if __name__ == "__main__":
    generate_info_card()