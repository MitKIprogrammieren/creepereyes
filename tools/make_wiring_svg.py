"""Erzeugt docs/verdrahtung.svg – Verdrahtungsplan für die Webflash-Seite (dunkler Hintergrund)."""
from pathlib import Path

EDGE, INK, QUIET = "#8c8c8c", "#ececec", "#a3a3a3"
RED, BLACK, BLUE, YELLOW = "#e04545", "#1a1a1a", "#3a7be0", "#f2c919"
ORANGE, GREEN, WHITE, PCB = "#f08a24", "#2e9e48", "#ffffff", "#3a86c0"

out = []
a = out.append


def text(x, y, s, size=13, weight=400, fill=INK, anchor="start"):
    a(f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{s}</text>')


def wire(d, c):
    a(f'<path d="{d}" fill="none" stroke="{EDGE}" stroke-width="5" stroke-linejoin="round"/>')
    a(f'<path d="{d}" fill="none" stroke="{c}" stroke-width="3" stroke-linejoin="round"/>')


def dot(x, y):
    a(f'<circle cx="{x}" cy="{y}" r="3.5" fill="{INK}"/>')


def used(x, y, c):
    a(f'<circle cx="{x}" cy="{y}" r="6.5" fill="{c}" stroke="{EDGE}" stroke-width="1.25"/>')


def pad(x, c):
    a(f'<circle cx="{x}" cy="790" r="8" fill="{c}" stroke="{EDGE}" stroke-width="1.25"/>')


ys = [106 + 24 * i for i in range(15)]
left = ["GND", "TXD", "RXD", "IO10", "IO11", "IO25", "IO12", "IO8", "IO22", "GND", "IO9", "GND", "IO27", "IO26", "GND"]
right = ["3V3", "RST", "IO0", "IO1", "IO2", "IO3", "IO13/N", "IO14/N", "IO4", "IO5", "NC", "VBAT", "GND", "5V", "GND"]
left_used = {0, 3, 4}
right_used = {0, 2, 3, 8, 9, 12, 13}

text(380, 30, "Verdrahtung: ESP32-H2 zu beiden OLED-Modulen", 16, 600, anchor="middle")
text(380, 50, "Board von der Stiftseite, USB-C unten · Module von hinten · Kabelfarben wie beim Waveshare-Kabel", 11.5, fill=QUIET, anchor="middle")

# ESP32-H2
a(f'<rect x="270" y="70" width="220" height="402" rx="8" fill="none" stroke="{EDGE}" stroke-width="1.5"/>')
a(f'<rect x="350" y="452" width="60" height="22" rx="6" fill="none" stroke="{EDGE}" stroke-width="1.25"/>')
text(380, 492, "USB-C", 11.5, fill=QUIET, anchor="middle")
text(380, 262, "ESP32-H2", 15, 600, anchor="middle")
text(380, 282, "Stiftseite", 11.5, fill=QUIET, anchor="middle")
for i, y in enumerate(ys):
    a(f'<circle cx="286" cy="{y}" r="3" fill="{QUIET}" fill-opacity="0.45"/>')
    a(f'<circle cx="474" cy="{y}" r="3" fill="{QUIET}" fill-opacity="0.45"/>')
    text(298, y + 4, left[i], 13, 600 if i in left_used else 400, INK if i in left_used else QUIET)
    text(462, y + 4, right[i], 13, 600 if i in right_used else 400, INK if i in right_used else QUIET, "end")

# Kabel
wire("M474 106H640V520M60 520H640M60 520V782M430 520V782", RED)
wire("M286 106H190V550M106 550H476M106 550V782M476 550V782", BLACK)
wire("M474 322H560V580M152 580H560M152 580V782M522 580V782", BLUE)
wire("M474 298H580V610M198 610H580M198 610V782M568 610V782", YELLOW)
wire("M474 178H600V640H244V782", ORANGE)
wire("M474 154H614V782", ORANGE)
wire("M286 178H210V700M210 700H660M290 700V782M660 700V782", GREEN)
wire("M286 202H230V730M230 730H706M336 730V782M706 730V782", WHITE)
for x, y in [(430, 520), (190, 550), (522, 580), (568, 610), (290, 700), (336, 730)]:
    dot(x, y)
for x, y, c in [(286, 106, BLACK), (286, 178, GREEN), (286, 202, WHITE), (474, 106, RED), (474, 154, ORANGE),
                (474, 178, ORANGE), (474, 298, YELLOW), (474, 322, BLUE), (474, 394, BLACK), (474, 418, RED)]:
    used(x, y, c)

# Akku
wire("M474 394H660", BLACK)
wire("M474 418H660", RED)
wire("M690 450V476", RED)
wire("M726 450V476", BLACK)
a(f'<rect x="690" y="346" width="32" height="14" rx="4" fill="none" stroke="{EDGE}" stroke-width="1.25"/>')
text(706, 338, "USB-C laden", 11.5, fill=QUIET, anchor="middle")
a('<rect x="660" y="360" width="92" height="90" rx="6" fill="#c0392b" fill-opacity="0.18" stroke="#d0503f" stroke-width="1.5"/>')
text(706, 378, "TP4056", 13, 600, anchor="middle")
text(668, 398, "OUT−", 11.5)
text(668, 422, "OUT+", 11.5)
text(690, 442, "B+", 11.5, anchor="middle")
text(726, 442, "B−", 11.5, anchor="middle")
a('<rect x="660" y="476" width="92" height="44" rx="8" fill="#2e9e48" fill-opacity="0.18" stroke="#3fb35c" stroke-width="1.5"/>')
text(706, 494, "LiPo 1S", 13, 600, anchor="middle")
text(706, 510, "3,7 V", 11.5, fill=QUIET, anchor="middle")

# OLED-Module
names = ["VCC", "GND", "DIN", "CLK", "CS", "DC", "RST"]
cols = [RED, BLACK, BLUE, YELLOW, ORANGE, GREEN, WHITE]
for x0, title, cs in [(30, "Linkes Auge", "IO1"), (400, "Rechtes Auge", "IO0")]:
    a(f'<rect x="{x0}" y="766" width="330" height="170" rx="10" fill="{PCB}" fill-opacity="0.16" stroke="{PCB}" stroke-width="1.5"/>')
    a(f'<rect x="{x0 + 250}" y="830" width="56" height="80" rx="3" fill="none" stroke="{EDGE}" stroke-width="1" stroke-dasharray="4 3"/>')
    for k in range(7):
        x = x0 + 30 + 46 * k
        pad(x, cols[k])
        text(x, 816, names[k], 11.5, 600, anchor="middle")
    text(x0 + 20, 890, title, 13, 600)
    text(x0 + 20, 910, f"Waveshare 1.5inch OLED, CS an {cs}", 11.5, fill=QUIET)

text(380, 964, "Gemeinsam: VCC, GND, DIN, CLK, DC, RST · getrennt: CS links IO1, CS rechts IO0", 13, 600, anchor="middle")
text(380, 986, "Statt Kabelstecker geht auch die Stiftleiste: VCC, GND, NC, DIN, CLK, CS, DC, RST – NC bleibt frei", 11.5, fill=QUIET, anchor="middle")
text(380, 1004, "BS1 und BS2 auf 0 lassen (Werkseinstellung = 4-Draht-SPI). Akku per JST-Stecker, zum Ausschalten abziehen", 11.5, fill=QUIET, anchor="middle")

svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 1030" role="img" '
       'aria-label="Verdrahtung ESP32-H2 zu zwei OLED-Modulen mit TP4056 und LiPo" '
       'font-family="system-ui, -apple-system, Segoe UI, sans-serif">' + "".join(out) + "</svg>")
Path(__file__).resolve().parent.parent.joinpath("docs", "verdrahtung.svg").write_text(svg, encoding="utf-8")
print("docs/verdrahtung.svg geschrieben")
