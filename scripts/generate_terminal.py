from datetime import datetime

USERNAME = "Yug Shrivastava"
GREEN = "#39ff14"
WHITE = "#e6e6e6"
BG = "#0b0b0b"

lines = [
    "██╗   ██╗██╗   ██╗ ██████╗ ",
    "╚██╗ ██╔╝██║   ██║██╔════╝ ",
    " ╚████╔╝ ██║   ██║██║  ███╗",
    "  ╚██╔╝  ██║   ██║██║   ██║",
    "   ██║   ╚██████╔╝╚██████╔╝",
    "   ╚═╝    ╚═════╝  ╚═════╝ ",
    "",
    "────────────────────────────────────────",
    f"USER      ▸ {USERNAME}",
    "OS        ▸ Linux | Windows",
    "EDITOR    ▸ Zed · VS Code",
    "STACK     ▸ Go · TypeScript · Python · C++",
    "LANG      ▸ English · Hindi",
    "────────────────────────────────────────",
    "",
    "$ whoami",
    "> engineer · builder · curious by default",
    "",
    "$ github --stats",
    "★ Stars ............ dynamic",
    "☉ Repositories .... dynamic",
    "↺ Commits ......... dynamic",
    "Σ Lines of Code ... dynamic",
    "",
    "$ learning",
    "> dynamic",
    "",
    "$ current-project",
    "> dynamic",
    "",
    "$ spotify --status",
    "> dynamic",
    "",
    "$ discord --presence",
    "> celestial_nomad12 · dynamic",
    "",
    "$ uptime",
    f"> online · {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}",
    "",
    "$ quote",
    '> "dynamic"',
]

y = 30
svg_lines = []

for line in lines:
    if line.startswith("$"):
        svg_lines.append(
            f'<text x="20" y="{y}" fill="{GREEN}">$</text>'
            f'<text x="35" y="{y}" fill="{WHITE}">{line[1:]}</text>'
        )
    else:
        svg_lines.append(
            f'<text x="20" y="{y}" fill="{WHITE}">{line}</text>'
        )
    y += 22

svg = f"""
<svg width="900" height="{y+20}" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="{BG}" rx="12"/>
  <style>
    text {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 16px;
      white-space: pre;
    }}
  </style>
  {''.join(svg_lines)}
</svg>
"""

with open("terminal.svg", "w") as f:
    f.write(svg.strip())
