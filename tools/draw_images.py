"""Draws the site's pictures as SVG: the hero scene, the morning-list example, the cabinet."""
import math
import os

OUT = os.path.join(os.path.dirname(__file__), "..", "img")
ORANGE = "#f97316"


def pumpjack(x, y, s, beam_deg, color="#05070a"):
    """A pumpjack silhouette standing at (x, y) ground, scale s, beam tilted by beam_deg."""
    a = math.radians(beam_deg)
    px, py = x, y - 120 * s                      # samson post top
    L1, L2 = 95 * s, 85 * s
    hx, hy = px - L1 * math.cos(a), py - L1 * math.sin(a)   # horsehead end
    tx, ty = px + L2 * math.cos(a), py + L2 * math.sin(a)   # tail end
    g = [f'<g fill="{color}" stroke="{color}" stroke-linecap="round" stroke-linejoin="round">']
    g.append(f'<polygon points="{x-30*s},{y} {px},{py} {x+30*s},{y}" fill="none" stroke-width="{6*s}"/>')
    g.append(f'<line x1="{hx}" y1="{hy}" x2="{tx}" y2="{ty}" stroke-width="{9*s}"/>')
    g.append(f'<path d="M{hx},{hy-18*s} q{-22*s},{18*s} 0,{40*s}" fill="none" stroke-width="{10*s}"/>')
    # bridle hangs from the outer face of the horsehead down to the wellhead
    g.append(f'<line x1="{hx-11*s}" y1="{hy+2*s}" x2="{hx-11*s}" y2="{y-14*s}" stroke-width="{2*s}"/>')
    gx, gy = x + 75 * s, y - 32 * s
    g.append(f'<line x1="{tx}" y1="{ty}" x2="{gx}" y2="{gy-20*s}" stroke-width="{4*s}"/>')
    g.append(f'<circle cx="{gx}" cy="{gy}" r="{24*s}" stroke-width="0"/>')
    g.append(f'<rect x="{gx-20*s}" y="{gy}" width="{40*s}" height="{32*s}" stroke-width="0"/>')
    g.append(f'<rect x="{x-60*s}" y="{y-6*s}" width="{195*s}" height="{6*s}" stroke-width="0"/>')
    # the electric motor behind the gearbox, belted to it: the thing Blackcap listens to
    g.append(f'<rect x="{x+105*s}" y="{y-26*s}" width="{28*s}" height="{20*s}" rx="{3*s}" stroke-width="0"/>')
    g.append(f'<line x1="{x+112*s}" y1="{y-22*s}" x2="{gx+6*s}" y2="{gy+6*s}" stroke-width="{2*s}"/>')
    g.append(f'<rect x="{hx-22*s}" y="{y-14*s}" width="{20*s}" height="{14*s}" stroke-width="0"/>')
    g.append("</g>")
    return "\n".join(g)


def hero():
    W, H = 1600, 900
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%" height="100%" preserveAspectRatio="xMidYMid slice">',
         '<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">'
         '<stop offset="0" stop-color="#0b1220"/><stop offset="0.55" stop-color="#3b2a3f"/>'
         '<stop offset="0.8" stop-color="#b4532a"/><stop offset="1" stop-color="#f59e0b"/></linearGradient>'
         '<radialGradient id="sun" cx="0.72" cy="0.86" r="0.35"><stop offset="0" stop-color="#fde68a" stop-opacity="0.9"/>'
         '<stop offset="1" stop-color="#fde68a" stop-opacity="0"/></radialGradient></defs>',
         f'<rect width="{W}" height="{H}" fill="url(#sky)"/>', f'<rect width="{W}" height="{H}" fill="url(#sun)"/>']
    # the brand's line: a power trace across the sky
    pts = []
    for k in range(0, W + 1, 8):
        ph = k / 260.0
        v = math.sin(2 * math.pi * ph) ** 2 * (1 if math.sin(2 * math.pi * ph) > 0 else 0.55)
        pts.append(f"{k},{430 - 110 * v + 20 * math.sin(k / 37)}")
    p.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{ORANGE}" stroke-opacity="0.35" stroke-width="3"/>')
    ground = 760
    p.append(f'<path d="M0,{ground} Q400,{ground-25} 800,{ground-8} T1600,{ground-18} L1600,{H} L0,{H} Z" fill="#05070a"/>')
    p.append(pumpjack(1180, ground - 12, 1.9, 9))
    p.append(pumpjack(430, ground - 18, 0.9, -6))
    p.append(pumpjack(160, ground - 22, 0.55, 4))
    p.append('</svg>')
    open(os.path.join(OUT, "hero.svg"), "w").write("\n".join(p))


def report():
    W, H = 760, 620
    # sorted the way the copy promises: wells that need you first
    rows = [("Smith 4", "Down since 4:12 am", "#ef4444", "Motor stopped; no restart since"),
            ("Ridge 1", "Running, no load", "#ef4444", "Motor turning with almost no load: check belts and rods"),
            ("Ridge 3", "Timer running long", "#f59e0b", "Pumps off after 3 h; timer set to 6 h"),
            ("Creek 7", "Something changed", "#f59e0b", "Different from this well's normal since yesterday"),
            ("Smith 2", "Running normally", "#22c55e", "Ran 7 h 40 min in 2 starts"),
            ("Creek 8", "Running normally", "#22c55e", "Used 41 kWh yesterday, about $4.90")]
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%" height="100%" preserveAspectRatio="xMidYMid meet" font-family="Inter, Helvetica, Arial, sans-serif">',
         f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="18" fill="#0f172a" stroke="#1e293b" stroke-width="2"/>',
         '<text x="32" y="56" font-size="24" font-weight="700" fill="#f8fafc">Tuesday morning</text>',
         '<text x="32" y="84" font-size="15" fill="#94a3b8">6 wells · 2 need you today · 2 to check · 2 fine</text>',
         f'<text x="{W-32}" y="56" font-size="13" fill="#64748b" text-anchor="end">Sample report</text>']
    y = 120
    for name, status, col, detail in rows:
        p.append(f'<rect x="24" y="{y}" width="{W-48}" height="72" rx="12" fill="#111c33"/>')
        p.append(f'<circle cx="52" cy="{y+36}" r="8" fill="{col}"/>')
        p.append(f'<text x="74" y="{y+31}" font-size="18" font-weight="600" fill="#f1f5f9">{name}</text>')
        p.append(f'<text x="74" y="{y+54}" font-size="14" fill="#94a3b8">{detail}</text>')
        p.append(f'<text x="{W-48}" y="{y+42}" font-size="15" font-weight="600" fill="{col}" text-anchor="end">{status}</text>')
        y += 82
    p.append('</svg>')
    open(os.path.join(OUT, "report.svg"), "w").write("\n".join(p))


def cabinet():
    W, H = 640, 520
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%" height="100%" preserveAspectRatio="xMidYMid meet" font-family="Inter, Helvetica, Arial, sans-serif">',
         '<rect x="120" y="40" width="400" height="440" rx="10" fill="#1e293b" stroke="#334155" stroke-width="4"/>',
         '<rect x="150" y="70" width="340" height="380" rx="6" fill="#0f172a"/>',
         '<rect x="165" y="110" width="310" height="10" fill="#475569"/>',   # DIN rail
         '<rect x="185" y="90" width="70" height="80" rx="6" fill="#334155"/>',  # starter
         '<rect x="270" y="90" width="70" height="80" rx="6" fill="#334155"/>',
         f'<rect x="360" y="84" width="96" height="92" rx="8" fill="#0b0f14" stroke="{ORANGE}" stroke-width="3"/>',
         f'<text x="408" y="136" font-size="15" font-weight="800" fill="{ORANGE}" text-anchor="middle">BLACKCAP</text>',
         '<line x1="200" y1="170" x2="200" y2="430" stroke="#94a3b8" stroke-width="7"/>',
         '<line x1="225" y1="170" x2="225" y2="430" stroke="#94a3b8" stroke-width="7"/>',
         '<line x1="250" y1="170" x2="250" y2="430" stroke="#94a3b8" stroke-width="7"/>',
         f'<rect x="183" y="290" width="34" height="46" rx="10" fill="none" stroke="{ORANGE}" stroke-width="6"/>',
         f'<path d="M217,312 C300,312 360,260 400,180" fill="none" stroke="{ORANGE}" stroke-width="3" stroke-dasharray="6 6"/>',
         '<text x="108" y="310" font-size="15" fill="#cbd5e1" text-anchor="end">Clamp on one</text><text x="108" y="330" font-size="15" fill="#cbd5e1" text-anchor="end">motor wire</text>',
         '<text x="530" y="125" font-size="15" fill="#cbd5e1">On the</text><text x="530" y="145" font-size="15" fill="#cbd5e1">DIN rail</text>',
         f'<line x1="456" y1="96" x2="456" y2="20" stroke="{ORANGE}" stroke-width="3"/>',
         '<text x="466" y="28" font-size="14" fill="#cbd5e1">Antenna outside</text>',
         '<text x="320" y="505" font-size="14" fill="#64748b" text-anchor="middle">In the starter cabinet, away from the wellhead</text>',
         '</svg>']
    open(os.path.join(OUT, "cabinet.svg"), "w").write("\n".join(p))


if __name__ == "__main__":
    hero(); report(); cabinet()
