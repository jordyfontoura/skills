"""Gera os gráficos do retrato de uso publicado no README.

Uso: python scripts/render_skill_usage.py
Fonte: docs/data/skill-usage.json. Usa apenas a biblioteca padrão.
"""

from datetime import datetime
from html import escape
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs/data/skill-usage.json"
FONT = 'ui-sans-serif, system-ui, -apple-system, "Segoe UI", Arial, sans-serif'


def text(x, y, value, size=20, color="#fafafa", anchor="start", weight=400):
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" '
            f'text-anchor="{anchor}" font-weight="{weight}">{escape(str(value))}</text>')


def panel(rows, x, y, title, label, maximum):
    active = [row for row in rows if row["occurrences"]]
    parts = [text(x, y, title, 28, weight=500),
             text(x, y + 34, label, 18, "#a1a1aa")]
    for index, row in enumerate(active):
        baseline = y + 83 + index * 34
        width = row["occurrences"] / maximum * 266
        parts.extend([
            text(x, baseline, row["skill"], 20, "#d4d4d8"),
            f'<rect x="{x + 248}" y="{baseline - 13}" width="266" height="10" rx="3" fill="#18181b"/>',
            f'<rect x="{x + 248}" y="{baseline - 13}" width="{width:.3f}" height="10" rx="3" fill="url(#bar)"/>',
        ])
    return "\n".join(parts), y + 83 + (len(active) - 1) * 34


def svg(data, mobile=False):
    maximum = max(row["occurrences"] for key in ("user", "agent") for row in data[key])
    width = 600 if mobile else 1200
    left, left_end = panel(data["user"], 40, 184, "Pedidos do usuário", "chamadas diretas", maximum)
    right_y = left_end + 100 if mobile else 184
    right, right_end = panel(data["agent"], 40 if mobile else 648, right_y,
                             "Uso declarado pelo agente", "declarações de uso", maximum)
    height = int(max(left_end, right_end) + 126)
    divider = (f'<path d="M40 {left_end + 47} H560" stroke="#27272a"/>' if mobile else
               f'<path d="M604 164 V{height - 112}" stroke="#27272a"/>')
    date = datetime.fromisoformat(data["snapshot_date"]).strftime("%d/%m/%Y")
    subtitle = f'Conversas do autor · {date}'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
  <title id="title">Frequência das skills nas conversas do autor</title>
  <desc id="desc">{escape(subtitle)}. Pedidos diretos do usuário e declarações do agente, ordenados por frequência de uso, sem contagens visíveis. Repetições em mensagens diferentes contam. Mesma escala nos dois rankings.</desc>
  <defs>
    <linearGradient id="bar"><stop stop-color="#71717a"/><stop offset="1" stop-color="#e4e4e7"/></linearGradient>
    <pattern id="dots" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1" fill="#fafafa" fill-opacity="0.035"/></pattern>
  </defs>
  <style>text {{ font-family: {FONT}; font-variant-numeric: tabular-nums; }}</style>
  <rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="24" fill="#09090b" stroke="#27272a"/>
  <rect x="24" y="16" width="{width - 48}" height="106" fill="url(#dots)"/>
  {text(40, 64, "Skills em uso", 36, weight=500)}
  {text(40, 103, subtitle, 20, "#a1a1aa")}
  <path d="M40 132 H{width - 40}" stroke="#27272a"/>
  {divider}
  {left}
  {right}
  <path d="M40 {height - 82} H{width - 40}" stroke="#27272a"/>
  {text(40, height - 48, "Frequência relativa. Não é telemetria de execução.", 18, "#a1a1aa")}
  {text(40, height - 21, "Mesmo pedido pode aparecer nos dois grupos. Mesma escala.", 18, "#a1a1aa")}
</svg>
'''


def main():
    data = json.loads(SOURCE.read_text(encoding="utf-8"))
    for key in ("user", "agent"):
        data[key].sort(key=lambda row: (-row["occurrences"], row["skill"]))
    for name, content in (("docs/assets/skill-usage.svg", svg(data)),
                          ("docs/assets/skill-usage-mobile.svg", svg(data, mobile=True))):
        (ROOT / name).write_text(content, encoding="utf-8", newline="\n")
        print(f"Gerado: {name}")


if __name__ == "__main__":
    main()
