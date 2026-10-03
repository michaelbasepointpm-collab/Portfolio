"""Sketches for REN fixes are in sketches.py; this module adds the Basepoint multifamily buildings."""
from sketches import G, W, f, rect, line, path, circle, text, rects_d, grid, hlines_d, vlines_d, tree, ground, svg


MF_VB = "0 104 480 216"


def shrub(cx, rx=16, ry=11):
    cy = G - ry + 1
    return (f'<ellipse class="fill-mask" cx="{f(cx)}" cy="{f(cy)}" rx="{f(rx)}" ry="{f(ry)}"/>'
            f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(rx)}" ry="{f(ry)}"/>')


def palm(x, h=96):
    top = G - h
    return (path(f"M{x} {G}C{x+2} {G-40} {x+8} {top+30} {x+6} {top}") +
            path(f"M{x+6} {top}q-20 -4 -32 10 M{x+6} {top}q-16 -14 -34 -10 M{x+6} {top}q18 -12 34 -6 "
                 f"M{x+6} {top}q20 2 30 18 M{x+6} {top}q2 -18 -4 -26", "thin"))


def wynne():
    b = [ground()]
    x0, x1, flh = 64, 416, 36
    top = G - 3 * flh - 4
    cx = (x0 + x1) / 2
    b.append(rect(x0, top, x1 - x0, G - top, "fill-mask"))
    b.append(path(f"M{x0-16} {top}L{x0+14} {top-16}H{x1-14}L{x1+16} {top}Z"))
    b.append(rect(x0, top, x1 - x0, G - top))
    strips = [x0 + 78, cx - 44, cx + 38, x1 - 84]
    b.append(path(" ".join(f"M{f(x)} {top}h6v{G-top}h-6z" for x in strips)))
    wins = []
    for r in range(3):
        y = top + 10 + r * flh
        for x in (x0 + 14, x0 + 44, x0 + 98, x0 + 128, x1 - 58, x1 - 28, x1 - 136, x1 - 106):
            wins.append((x, y, 18, 18))
    b.append(path(rects_d(wins)))
    b.append(path(" ".join(f"M{f(cx-24)} {f(top + 10 + r*flh + 22)}h48v10h-48z" for r in range(2))))
    b.append(path(" ".join(f"M{f(cx-24+i*8)} {f(top + 10 + r*flh + 22)}v10" for r in range(2) for i in range(1, 6)), "thin"))
    b.append(path(rects_d([(cx - 16, top + 10, 14, 18), (cx + 2, top + 10, 14, 18),
                           (cx - 16, top + 10 + flh, 14, 18), (cx + 2, top + 10 + flh, 14, 18)]), "thin"))
    b.append(path(f"M{f(cx-14)} {G}V{G-30}H{f(cx+14)}V{G}", "accent"))
    b.append(palm(40, 104))
    b.append(palm(438, 88))
    b.append(shrub(110, 22, 12))
    b.append(shrub(372, 22, 12))
    return svg("wynne", "WYNNE MANOR · 1309 W 14TH AVE", b,
               "Line drawing of Wynne Manor: a wide three-storey stucco rental building with dark vertical bands, stacked centre balconies and palm trees", vb=MF_VB)


def kaleden():
    b = [ground()]
    x0, x1, flh = 72, 408, 34
    top = G - 3 * flh - 2
    cx = (x0 + x1) / 2
    b.append(f'<g class="fade">{rect(x0 - 4, top - 12, x1 - x0 + 8, 12, "fill-soft")}</g>')
    b.append(path(f"M{x0-4} {top}V{top-12}H{x1+4}V{top}"))
    b.append(rect(x0, top, x1 - x0, G - top))
    b.append(path(rects_d(grid(x0 + 14, top + 9, 9, 2, 36.5, flh, 20, 18))))
    b.append(path(hlines_d(x0 + 1, x1 - 1, [G - flh + 6 + i * 6 for i in range(5)]), "thin"))
    gy = G - flh + 8
    b.append(rect(cx - 50, G - flh, 100, flh, "fill-mask"))
    b.append(path(rects_d([(x0 + 14, gy, 24, 16), (x0 + 50, gy, 24, 16), (x1 - 74, gy, 24, 16), (x1 - 38, gy, 24, 16)])))
    b.append(path(f"M{f(cx-48)} {G-flh}h96v9h-96z"))
    b.append(f'<g class="fade">{text(cx, G - flh + 7, "KALEDEN", "middle")}</g>')
    b.append(path(f"M{f(cx-14)} {G}V{G-flh+12}H{f(cx+14)}V{G}", "accent"))
    for x in (100, 156, 324, 380):
        b.append(shrub(x, 22, 14))
    b.append(tree(36, 18, trunk=24))
    return svg("kaleden", "KALEDEN · 1015 W 13TH AVE", b,
               "Line drawing of Kaleden: a three-storey stucco rental building with a dark parapet band, a named entrance canopy and rounded shrubs", vb=MF_VB)


def hillcrest_mf():
    b = [ground()]
    x0, x1, flh = 84, 396, 34
    top = G - 3 * flh
    cx = (x0 + x1) / 2
    gables = (x0 + 52, cx, x1 - 52)
    b.append(rect(x0, top - 20, x1 - x0, G - top + 20, "fill-mask"))
    roof = f"M{x0-6} {top}"
    for gx in gables:
        roof += f"H{f(gx-22)}L{f(gx)} {f(top-20)}L{f(gx+22)} {top}"
    roof += f"H{x1+6}"
    b.append(path(roof))
    b.append(rect(x0, top, x1 - x0, G - top))
    panels = []
    for gx in gables:
        panels.append(f"M{f(gx-14)} {top+4}L{f(gx+14)} {top+flh-4}M{f(gx+14)} {top+4}L{f(gx-14)} {top+flh-4}")
    b.append(path(" ".join(panels), "thin"))
    b.append(path(vlines_d(top, top + flh, [x0 + 30, x0 + 74, cx - 26, cx + 26, x1 - 74, x1 - 30]), "thin"))
    wins = []
    for r in range(3):
        y = top + 8 + r * flh
        xs = (x0 + 96, x0 + 124, x1 - 142, x1 - 114) if r == 0 else \
             (x0 + 14, x0 + 44, x0 + 96, x0 + 124, x1 - 142, x1 - 114, x1 - 62, x1 - 32)
        for x in xs:
            wins.append((x, y, 18, 18))
    b.append(path(rects_d(wins)))
    b.append(path(hlines_d(x0 + 1, x1 - 1, [G - flh + 4 + i * 5 for i in range(6)]), "thin"))
    b.append(rect(cx - 24, G - flh - 6, 48, flh + 6, "fill-mask"))
    b.append(path(f"M{f(cx-24)} {G}V{G-flh-6}H{f(cx+24)}V{G}"))
    b.append(path(hlines_d(cx - 23, cx - 13, [G - flh + i * 5 for i in range(7)]) + " " +
                  hlines_d(cx + 13, cx + 23, [G - flh + i * 5 for i in range(7)]), "thin"))
    b.append(path(f"M{f(cx-12)} {G}V{G-28}H{f(cx+12)}V{G}", "accent"))
    b.append(path(f"M{f(cx-32)} {G-flh-6}h64v6h-64z"))
    b.append(f'<g class="fade">{text(cx, G - flh - 10, "3850", "middle")}</g>')
    b.append(tree(46, 26, trunk=26))
    b.append(tree(432, 24, trunk=26))
    b.append(shrub(140, 22, 12))
    b.append(shrub(340, 22, 12))
    return svg("hillcrest-manor", "HILLCREST MANOR · 3850 CAMBIE ST", b,
               "Line drawing of Hillcrest Manor: a low stucco building with small gables, half-timber trim and a brick entrance marked 3850", vb=MF_VB)


def selkirk():
    b = [ground()]
    x0, x1, flh = 120, 330, 34
    top = G - 3 * flh - 2
    b.append(rect(x0, top, x1 - x0, G - top, "fill-mask"))
    b.append(rect(x0, top, x1 - x0, G - top))
    b.append(path(f"M{x0-3} {top}h{x1-x0+6}v6h-{x1-x0+6}z"))
    b.append(path(vlines_d(top + 7, G, [x0 + 4 + i * 5 for i in range(int((x1 - x0 - 6) / 5))]), "thin"))
    wins = [(x0 + 14 + c * 50, top + 16 + r * flh, 34, 14) for r in range(3) for c in range(4)]
    b.append("".join(rect(*w, "fill-mask") for w in wins))
    b.append(path(rects_d(wins)))
    b.append(path(" ".join(f"M{f(x+17)} {f(y)}v14" for x, y, *_ in wins), "thin"))
    px = x1
    b.append(path(f"M{px+6} {G}V{G-58}M{px+86} {G}V{G-58}M{px} {G-58}H{px+96}M{px} {G-64}H{px+96}"))
    b.append(path(" ".join(f"M{px+6+i*10} {G-64}v6" for i in range(10)), "thin"))
    b.append(path(" ".join(f"M{px+10+i*6} {G}v-34" for i in range(13)) + f" M{px+8} {G-34}H{px+88}", "thin"))
    b.append(path(f"M{x0-34} {G}V{G-32}M{x0-4} {G}V{G-32}M{x0-40} {G-34}h42", "accent"))
    b.append(tree(56, 18, trunk=22))
    return svg("selkirk", "SELKIRK · 8687 SELKIRK ST", b,
               "Line drawing of Selkirk: a compact dark stucco building with a white roof edge, white-framed windows and a corner patio with a pergola", vb=MF_VB)


def w71():
    b = [ground()]
    x0, x1, flh = 92, 388, 36
    top = G - 3 * flh - 2
    cx = (x0 + x1) / 2
    b.append(rect(x0, top, x1 - x0, G - top, "fill-mask"))
    b.append(path(f"M{x0-5} {top}h{x1-x0+10}v5h-{x1-x0+10}z"))
    b.append(rect(x0, top, x1 - x0, G - top))
    wins = []
    for r in range(3):
        y = top + 12 + r * flh
        for i, x in enumerate((x0 + 16, x0 + 58, x0 + 100, x1 - 126, x1 - 76, x1 - 40)):
            w = 26 if i % 2 == 0 else 18
            if r == 2 and abs(x + w / 2 - cx) < 40:
                continue
            wins.append((x, y, w, 18))
    b.append(path(rects_d(wins)))
    b.append(path(f"M{f(cx-18)} {G}V{G-30}H{f(cx+18)}V{G}M{f(cx-10)} {G}V{G-24}H{f(cx+10)}V{G}", "accent"))
    b.append(path(f"M{f(cx-26)} {G-31}h52v5h-52z"))
    b.append(tree(184, 34, trunk=30))
    b.append(shrub(330, 26, 10))
    b.append(shrub(116, 20, 10))
    return svg("w71", "911 W 71ST AVE · MARPOLE", b,
               "Line drawing of 911 West 71st Avenue: a simple three-storey stucco rental block with a flat roof, a central entrance and a large front tree", vb=MF_VB)


def seaview():
    b = [ground()]
    x0, x1, flh = 70, 400, 34
    top = G - 3 * flh
    b.append(rect(x0, top - 30, x1 - x0, G - top + 30, "fill-mask"))
    b.append(rect(x1 - 70, top - 44, 22, 30))
    b.append(path(f"M{x0-24} {top}L{(x0+x1)/2} {top-26}L{x1+24} {top}Z"))
    b.append(rect(x0, top, x1 - x0, G - top))
    b.append(f'<g class="fade">{"".join(rect(x0 + 1, top + 30 + r * flh, 150, 8, "fill-soft") for r in range(2))}</g>')
    b.append(path(" ".join(f"M{x0+1} {top+30+r*flh}h150v8h-150z" for r in range(2)), "thin"))
    wins = [(x0 + 16 + c * 34, top + 8 + r * flh, 20, 18) for r in range(3) for c in range(4)]
    wins += [(x0 + 176 + c * 40, top + 8 + r * flh, 22, 20) for r in range(3) for c in range(4)]
    b.append(path(rects_d(wins)))
    b.append(path(" ".join(f"M{x0+168+c*80} {top+30+r*flh}h56v10h-56z" for r in range(2) for c in range(2))))
    b.append(path(" ".join(f"M{x0+168+c*80+i*8} {top+30+r*flh}v10" for r in range(2) for c in range(2) for i in range(1, 7)), "thin"))
    b.append(path(f"M{x0+150} {G}V{G-28}H{x0+172}V{G}", "accent"))
    b.append(tree(36, 18, trunk=22))
    b.append(tree(442, 16, trunk=20))
    return svg("seaview", "SEA VIEW APARTMENTS · 2236 TRINITY ST", b,
               "Line drawing of Sea View Apartments: a low stucco rental building with a shallow pitched roof, a chimney, horizontal panels and balconies", vb=MF_VB)


MF_BUILDERS = {
    "wynne": wynne,
    "kaleden": kaleden,
    "hillcrest-mf": hillcrest_mf,
    "selkirk": selkirk,
    "w71": w71,
    "seaview": seaview,
}
