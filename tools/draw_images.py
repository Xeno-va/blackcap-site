"""Draws the site's pictures as SVG: the hero scene and the cabinet. The morning list is drawn in the page itself."""
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


def cabinet():
    # writing sized to stay readable when the drawing is shown phone-width (about half size)
    W, H = 640, 600
    F = 'font-size="24" fill="#cbd5e1"'
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%" height="100%" preserveAspectRatio="xMidYMid meet" font-family="Inter, Helvetica, Arial, sans-serif">',
         '<rect x="190" y="70" width="300" height="440" rx="10" fill="#1e293b" stroke="#334155" stroke-width="4"/>',
         '<rect x="214" y="94" width="252" height="392" rx="6" fill="#0f172a"/>',
         '<rect x="226" y="140" width="228" height="10" fill="#475569"/>',   # DIN rail
         '<rect x="236" y="118" width="62" height="78" rx="6" fill="#334155"/>',  # starter
         f'<rect x="330" y="112" width="112" height="90" rx="8" fill="#0b0f14" stroke="{ORANGE}" stroke-width="3"/>',
         f'<text x="386" y="164" font-size="17" font-weight="800" fill="{ORANGE}" text-anchor="middle">BLACKCAP</text>',
         '<line x1="248" y1="196" x2="248" y2="470" stroke="#94a3b8" stroke-width="7"/>',
         '<line x1="267" y1="196" x2="267" y2="470" stroke="#94a3b8" stroke-width="7"/>',
         '<line x1="286" y1="196" x2="286" y2="470" stroke="#94a3b8" stroke-width="7"/>',
         f'<rect x="231" y="320" width="34" height="48" rx="10" fill="none" stroke="{ORANGE}" stroke-width="6"/>',
         f'<path d="M265,344 C330,344 370,290 386,202" fill="none" stroke="{ORANGE}" stroke-width="3" stroke-dasharray="6 6"/>',
         f'<line x1="180" y1="344" x2="226" y2="344" stroke="#64748b" stroke-width="2"/>',
         f'<text x="172" y="336" {F} text-anchor="end">Clamp on</text><text x="172" y="366" {F} text-anchor="end">one wire</text>',
         f'<line x1="447" y1="157" x2="504" y2="157" stroke="#64748b" stroke-width="2"/>',
         f'<text x="510" y="150" {F}>On the</text><text x="510" y="180" {F}>DIN rail</text>',
         f'<line x1="430" y1="112" x2="430" y2="30" stroke="{ORANGE}" stroke-width="3"/>',
         f'<text x="442" y="44" {F}>Antenna outside</text>',
         '<text x="340" y="560" font-size="22" fill="#94a3b8" text-anchor="middle">In the starter cabinet, away from the wellhead</text>',
         '</svg>']
    open(os.path.join(OUT, "cabinet.svg"), "w").write("\n".join(p))


if __name__ == "__main__":
    hero(); cabinet()
