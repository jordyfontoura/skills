"""Gera os gráficos e a tabela do retrato de uso publicado no README.

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
    total = sum(row["occurrences"] for row in rows)
    parts = [text(x, y, title, 28, weight=500),
             text(x, y + 58, total, 44, weight=500),
             text(x + 99, y + 57, label, 18, "#a1a1aa"),
             text(x, y + 106, "Skill", 16, "#a1a1aa"),
             text(x + 450, y + 106, "Vezes", 16, "#a1a1aa", "end"),
             text(x + 514, y + 106, "Threads", 16, "#a1a1aa", "end")]
    for index, row in enumerate(active):
        baseline = y + 145 + index * 34
        width = row["occurrences"] / maximum * 158
        parts.extend([
            text(x, baseline, row["skill"], 20, "#d4d4d8"),
            f'<rect x="{x + 248}" y="{baseline - 13}" width="158" height="10" rx="3" fill="#18181b"/>',
            f'<rect x="{x + 248}" y="{baseline - 13}" width="{width:.3f}" height="10" rx="3" fill="url(#bar)"/>',
            text(x + 450, baseline, row["occurrences"], 20, anchor="end", weight=500),
            text(x + 514, baseline, row["threads"], 20, "#a1a1aa", "end"),
        ])
    return "\n".join(parts), y + 145 + (len(active) - 1) * 34


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
    subtitle = f'{data["thread_count"]} conversas do autor · {date}'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
  <title id="title">Frequência das skills nas conversas do autor</title>
  <desc id="desc">{escape(subtitle)}. Pedidos diretos do usuário e declarações do agente, ordenados por quantidade de ocorrências. Repetições em mensagens diferentes contam. A coluna Threads mostra conversas distintas. Mesma escala nos dois rankings. Tabela e método em docs/SKILL-USAGE.md.</desc>
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
  {text(40, height - 48, "Ocorrências por mensagem. Não é telemetria de execução.", 18, "#a1a1aa")}
  {text(40, height - 21, "Mesmo pedido pode aparecer nos dois grupos. Mesma escala.", 18, "#a1a1aa")}
</svg>
'''


def report(data):
    date = datetime.fromisoformat(data["snapshot_date"]).strftime("%d/%m/%Y")
    cutoff = datetime.fromisoformat(data["cutoff"]).strftime("%Hh%M")
    lines = ["# Uso observado das skills", "",
             f'Retrato de **{data["thread_count"]} conversas pessoais do autor**, consultadas no T3 Code',
             f"em {date}, com corte às {cutoff} (Brasília). Inclui histórico anterior a essa data.", "",
             "## Como foi contado", "",
             "- **Pedidos do usuário:** chamadas diretas pelo nome da skill, como `$progress`,",
             "  `/write-goal` ou uma frase explícita pedindo seu uso. São pedidos, sem comprovação de execução.",
             "- **Uso declarado pelo agente:** mensagens em que o agente anuncia ou relata usar uma skill.",
             "  Inclui o atendimento a pedidos do usuário; não mede apenas iniciativa própria.",
             "- Cada skill conta uma vez por mensagem. Repetições em mensagens diferentes contam novamente.",
             "- A coluna **Threads** conta conversas distintas e não determina a ordem do ranking.",
             "- Os grupos podem se sobrepor. Seus totais não devem ser somados como execuções distintas.", "",
             "Foram excluídos catálogos, citações, sugestões de uso futuro e pedidos para editar a própria",
             "skill. No ranking humano, também ficaram de fora regras embutidas em goals e automações.",
             "Usos silenciosos e atividades internas de subagentes não foram contados. Nomes antigos",
             "diferentes não foram agregados aos atuais. Zero significa ausência de registro neste critério.", "",
             "A amostra depende das conversas disponíveis e da identificação das declarações. Não é",
             "telemetria de execução nem uma medida da utilidade ou da qualidade de cada skill.", ""]
    for key, title in (("user", "Pedidos do usuário"), ("agent", "Uso declarado pelo agente")):
        lines += [f"## {title}", "", "| Skill | Ocorrências | Threads |", "| --- | ---: | ---: |"]
        lines += [f'| `{r["skill"]}` | {r["occurrences"]} | {r["threads"]} |' for r in data[key]]
        lines += [""]
    lines += ["## Atualizar o retrato", "",
              "Os números agregados estão em [data/skill-usage.json](data/skill-usage.json).",
              "Para publicar uma nova análise, atualize os dados e a data de corte e gere os gráficos",
              "e esta tabela a partir da raiz do repositório:", "", "```bash",
              "python scripts/render_skill_usage.py", "```", "",
              "O comando só gera os arquivos locais; não consulta conversas nem atualiza as contagens.", ""]
    return "\n".join(lines)


def main():
    data = json.loads(SOURCE.read_text(encoding="utf-8"))
    for key in ("user", "agent"):
        data[key].sort(key=lambda row: (-row["occurrences"], row["skill"]))
    for name, content in (("docs/assets/skill-usage.svg", svg(data)),
                          ("docs/assets/skill-usage-mobile.svg", svg(data, mobile=True)),
                          ("docs/SKILL-USAGE.md", report(data))):
        (ROOT / name).write_text(content, encoding="utf-8", newline="\n")
        print(f"Gerado: {name}")


if __name__ == "__main__":
    main()
