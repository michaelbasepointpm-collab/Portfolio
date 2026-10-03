"""Generates the line-art building sketches used on the portfolio.
Each sketch is a 480x320 SVG drawn with plain strokes so the page can animate it.
Run: py sketches.py  -> writes assets/img/illustrations/*.svg and returns inline snippets."""

import os

W, H, G = 480, 320, 272  # width, height, ground line


def f(n):
    return f"{n:.1f}".rstrip("0").rstrip(".")


def rect(x, y, w, h, cls=None, rx=None):
    c = f' class="{cls}"' if cls else ""
    r = f' rx="{f(rx)}"' if rx else ""
    return f'<rect{c} x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}"{r}/>'


def line(x1, y1, x2, y2, cls=None):
    c = f' class="{cls}"' if cls else ""
    return f'<line{c} x1="{f(x1)}" y1="{f(y1)}" x2="{f(x2)}" y2="{f(y2)}"/>'


def path(d, cls=None):
    c = f' class="{cls}"' if cls else ""
    return f'<path{c} d="{d}"/>'


def circle(cx, cy, r, cls=None):
    c = f' class="{cls}"' if cls else ""
    return f'<circle{c} cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}"/>'


def text(x, y, s, anchor="start"):
    a = f' text-anchor="{anchor}"' if anchor != "start" else ""
    return f'<text class="label" x="{f(x)}" y="{f(y)}"{a}>{s}</text>'


def rects_d(items):
    """items: iterable of (x, y, w, h) -> one path with a subpath per rectangle."""
    return " ".join(f"M{f(x)} {f(y)}h{f(w)}v{f(h)}h{f(-w)}z" for x, y, w, h in items)


def grid(x0, y0, cols, rows, dx, dy, w, h, skip=None):
    out = []
    for r in range(rows):
        for c in range(cols):
            if skip and skip(c, r):
                continue
            out.append((x0 + c * dx, y0 + r * dy, w, h))
    return out


def hlines_d(x1, x2, ys):
    return " ".join(f"M{f(x1)} {f(y)}H{f(x2)}" for y in ys)


def vlines_d(y1, y2, xs):
    return " ".join(f"M{f(x)} {f(y1)}V{f(y2)}" for x in xs)


def tree(cx, r, ground=G, trunk=None, cls=None):
    trunk = trunk or r * 1.1
    top = ground - trunk
    cy = top - r + 4
    return circle(cx, cy, r, "fill-mask") + line(cx, ground, cx, top + 2, cls) + circle(cx, cy, r, cls)


def ground(extra=""):
    return line(16, G, W - 16, G) + line(16, G + 9, W - 16, G + 9, "thin") + extra


def svg(key, label, body, aria, vb=None):
    inner = "".join(body)
    vb = vb or f"0 0 {W} {H}"
    return (
        f'<svg class="sketch" viewBox="{vb}" role="img" aria-label="{aria}" '
        f'xmlns="http://www.w3.org/2000/svg">{inner}'
        f'<g class="fade">{text(24, 306, label)}</g></svg>'
    )


S = {}

# ---------------------------------------------------------------- Sunrise Village (under construction)
def sunrise():
    b = [ground()]
    # tower crane between the two buildings
    mast_x = 244
    b.append(path(f"M{mast_x-5} {G}V54 M{mast_x+5} {G}V54 " +
                  " ".join(f"M{mast_x-5} {y}L{mast_x+5} {y-14}" for y in range(G, 70, -14)), "thin accent"))
    b.append(path(f"M{mast_x-70} 54H436 M{mast_x-70} 62H{mast_x-5} M{mast_x+5} 62H436 " +
                  " ".join(f"M{x} 62L{x+10} 54" for x in range(mast_x - 66, 430, 16)), "thin accent"))
    b.append(path(f"M{mast_x} 54L{mast_x} 34 L{mast_x-60} 54 M{mast_x} 34 L{mast_x+110} 54", "thin accent"))
    b.append(rect(mast_x - 66, 62, 18, 12, "thin accent"))
    b.append(path("M400 62V118 M394 118h12 M400 118v6a4 4 0 1 1 -6 2", "thin accent"))
    for x0, name in ((44, "WEST"), (276, "EAST")):
        w = 168
        top = 110
        b.append(f'<g class="fade">{rect(x0, G-28, w, 28, "fill-soft")}</g>')
        b.append(rect(x0, top, w, G - top))
        b.append(line(x0 - 5, top, x0 + w + 5, top))
        b.append(rect(x0 + 104, top - 12, 38, 12))
        b.append(path(hlines_d(x0, x0 + w, [G - 28]), "thin"))
        b.append(path(rects_d(grid(x0 + 14, top + 7, 6, 5, 25, 27, 14, 15))))
        # balcony rails on alternate columns
        b.append(path(" ".join(f"M{f(x0+10+c*25)} {f(top+25+r*27)}h22" for r in range(5) for c in (0, 2, 4)), "thin"))
        # ground floor: entry + wide windows
        b.append(path(rects_d([(x0 + 14, G - 22, 34, 16), (x0 + 120, G - 22, 34, 16)])))
        b.append(rect(x0 + 72, G - 24, 24, 24, "accent"))
        b.append(f'<g class="fade">{text(x0 + 2, top - 18, name + (" · 2926" if name == "WEST" else " · 2956"))}</g>')
    # courtyard garden + play area
    b.append(tree(228, 12, trunk=14))
    b.append(tree(260, 9, trunk=11))
    b.append(tree(30, 10, trunk=12))
    b.append(tree(456, 10, trunk=12))
    return svg("sunrise", "SUNRISE VILLAGE · 2926 &amp; 2956 VENABLES ST",
               b, "Line drawing of Sunrise Village: two six-storey buildings with a tower crane between them, under construction")

# ---------------------------------------------------------------- Timbre & Harmony
def timbre_harmony():
    b = []
    b.append(path("M16 128L58 100L84 112L122 78L150 92L176 70L214 98L250 84L282 104L318 82L352 96L392 74L430 96L464 88", "thin"))
    b.append(path("M112 86l10 -8l8 6 M168 76l8 -6l10 8", "thin"))
    b.append(ground())
    # back building
    bx, bw, btop, bbot = 236, 186, 110, 250
    b.append(rect(bx, btop, bw, bbot - btop, "fill-mask"))
    b.append(path(f"M{bx} {bbot}V{btop}H{bx+bw}V{bbot}"))
    b.append(rect(bx + 70, btop - 12, 44, 12))
    b.append(path(rects_d(grid(bx + 12, btop + 7, 8, 5, 21, 23, 9, 12))))
    b.append(path(" ".join(f"M{f(bx+9+c*21)} {f(btop+20+r*23)}h15v4h-15z" for r in range(5) for c in range(0, 8, 2)), "thin"))
    # front building
    fx, fw, ftop = 54, 210, 100
    b.append(rect(fx, ftop, fw, G - ftop, "fill-mask"))
    b.append(rect(fx, ftop, fw, G - ftop))
    b.append(line(fx - 4, ftop, fx + fw + 4, ftop))
    b.append(rect(fx + 116, ftop - 16, 60, 16))
    b.append(path(rects_d(grid(fx + 14, ftop + 9, 8, 5, 24.5, 28, 11, 15))))
    b.append(path(" ".join(f"M{f(fx+10+c*24.5)} {f(ftop+26+r*28)}h19v5h-19z" for r in range(5) for c in (1, 3, 5, 7)), "thin"))
    b.append(path(hlines_d(fx, fx + fw, [G - 32]), "thin"))
    b.append(path(rects_d([(fx + 12, G - 24, 40, 18), (fx + 142, G - 24, 52, 18)])))
    b.append(rect(fx + 88, G - 26, 30, 26, "accent"))
    # street trees
    b.append(tree(34, 14, trunk=16))
    b.append(tree(300, 18, trunk=18))
    b.append(tree(446, 12, trunk=14))
    return svg("timbre-harmony", "TIMBRE &amp; HARMONY · E 12TH AVE", b,
               "Line drawing of Timbre and Harmony: two six-storey white rental buildings with small balconies and mountains behind")

# ---------------------------------------------------------------- The Hawthorn
def hawthorn():
    b = [ground()]
    x0, x1, top = 64, 404, 100
    fl = (G - top) / 6
    b.append(f'<g class="fade">{rect(x0 - 8, top - 8, x1 - x0 + 16, 7, "fill-soft")}</g>')
    b.append(path(f"M{x0-12} {top-8}H{x1+12}V{top-1}H{x0-12}Z"))
    b.append(rect(x0, top, x1 - x0, G - top))
    # dark siding on the upper floors
    b.append(path(vlines_d(top + 1, top + fl * 2, [x0 + 6 + i * 7 for i in range(int((x1 - x0 - 8) / 7))]), "thin"))
    b.append(path(hlines_d(x0, x1, [top + fl * 2, G - fl]), "thin"))
    b.append(path(rects_d(grid(x0 + 16, top + 8, 9, 5, 36, fl, 14, 17))))
    # projecting box balconies
    for r in range(1, 5):
        y = top + fl * r + fl - 9
        b.append(path(f"M{x1-44} {f(y)}h52v9h-52 M{x0-8} {f(y)}h40v9h-40"))
    b.append(path(" ".join(f"M{x1-40+i*12} {f(top + fl*r + fl - 9)}v9" for r in range(1, 5) for i in range(4)), "thin"))
    # ground floor: storefront glazing, entry and building sign
    b.append(path(rects_d([(x0 + 14, G - 24, 66, 18), (x0 + 96, G - 24, 66, 18)])))
    b.append(rect(x0 + 176, G - 26, 26, 26, "accent"))
    b.append(f'<g class="fade">{text(x0 + 252, G - 11, "THE HAWTHORN", "middle")}</g>')
    b.append(path(f"M{x0+212} {G-24}h80", "thin"))
    # bike rack + trees
    b.append(path("M352 272v-10a6 6 0 0 1 12 0v10 M368 272v-10a6 6 0 0 1 12 0v10 M384 272v-10a6 6 0 0 1 12 0v10", "thin"))
    b.append(tree(36, 16, trunk=22))
    b.append(tree(448, 14, trunk=18))
    return svg("the-hawthorn", "THE HAWTHORN · 8705 FRENCH ST", b,
               "Line drawing of The Hawthorn: a six-storey rental building with a wood soffit roof, box balconies and street trees")

# ---------------------------------------------------------------- The Independent
def independent():
    b = [ground()]
    tx, tw, ttop = 248, 84, 26
    b.append(rect(tx, ttop, tw, G - ttop))
    b.append(rect(tx + 18, ttop - 10, 48, 10))
    floors = 21
    fh = (G - 92 - ttop) / (floors - 4)
    b.append(path(hlines_d(tx, tx + tw, [ttop + fh * i for i in range(1, floors - 4)]), "thin"))
    b.append(path(vlines_d(ttop, G - 92, [tx + 21, tx + 42, tx + 63]), "thin"))
    # mid-rise podium with townhomes
    px, pw, ptop = 54, 194, 172
    b.append(rect(px, ptop, pw, G - ptop))
    b.append(line(px - 4, ptop, px + pw, ptop))
    b.append(path(rects_d(grid(px + 12, ptop + 10, 7, 3, 26, 24, 14, 14))))
    b.append(path(" ".join(f"M{px+20+i*44} {G}v-20h16v20" for i in range(4)), "accent"))
    # retail / office wing
    rx, rw, rtop = 332, 104, 186
    b.append(rect(rx, rtop, rw, G - rtop))
    b.append(path(rects_d(grid(rx + 10, rtop + 10, 4, 2, 23, 22, 15, 13))))
    b.append(path(rects_d([(rx + 8, G - 34, 88, 28)])))
    b.append(path(vlines_d(G - 34, G - 6, [rx + 30, rx + 52, rx + 74]), "thin"))
    b.append(tree(30, 12, trunk=14))
    b.append(tree(196, 10, trunk=12))
    b.append(tree(456, 10, trunk=12))
    return svg("the-independent", "THE INDEPENDENT · 2508 WATSON ST", b,
               "Line drawing of The Independent: a 21-storey residential tower with a mid-rise podium of townhomes and a retail wing")

# ---------------------------------------------------------------- The Hudson
def hudson():
    b = [ground()]
    tx, tw, ttop = 168, 150, 22
    b.append(rect(tx, ttop, tw, 160 - ttop))
    b.append(path(f"M{tx+10} {ttop}V{ttop-8}H{tx+tw-10}V{ttop}"))
    b.append(path(hlines_d(tx, tx + tw, [ttop + 9 + i * 9 for i in range(15)]), "thin"))
    b.append(path(vlines_d(ttop, 160, [tx + 30, tx + 60, tx + 90, tx + 120]), "thin"))
    # heritage facade in front
    hx, hw, htop = 62, 268, 160
    b.append(rect(hx, htop, hw, G - htop, "fill-mask"))
    b.append(rect(hx, htop, hw, G - htop))
    b.append(path(f"M{hx-6} {htop}H{hx+hw+6} M{hx-6} {htop+8}H{hx+hw+6}"))
    b.append(path(" ".join(f"M{hx+6+i*8} {htop+8}v4" for i in range(33)), "thin"))
    # arched windows
    arches = []
    for i in range(7):
        x = hx + 16 + i * 36
        arches.append(f"M{x} {htop+56}V{htop+34}a8 8 0 0 1 16 0V{htop+56}Z")
    b.append(path(" ".join(arches)))
    b.append(path(hlines_d(hx, hx + hw, [htop + 64]), "thin"))
    b.append(path(rects_d([(hx + 10 + i * 64, G - 40, 52, 34) for i in range(4)])))
    b.append(rect(hx + hw - 26, htop + 18, 12, 60, "accent"))
    b.append(path(" ".join(f"M{hx+hw-20} {htop+28+i*12}h0.1" for i in range(4)), "accent"))
    # neighbour
    b.append(path("M330 272V196H440V272 M342 210h22v16h-22z M376 210h22v16h-22z M410 210h22v16h-22z", "thin"))
    b.append(tree(34, 12, trunk=16))
    b.append(tree(452, 10, trunk=12))
    return svg("the-hudson", "THE HUDSON · 610 GRANVILLE ST", b,
               "Line drawing of The Hudson: a downtown condo tower rising behind a restored heritage facade on Granville Street")

# ---------------------------------------------------------------- ALMA Gastown
def alma():
    b = []
    # Woodward's W tower in the background
    b.append(path("M406 40l8 22l8 -16l8 16l8 -22", "accent"))
    b.append(path("M414 70L410 180 M430 70L434 180 " + " ".join(f"M{412 - i*0.4} {74+i*18}L{432 + i*0.4} {92+i*18} M{432 + i*0.4} {74+i*18}L{412 - i*0.4} {92+i*18}" for i in range(6)), "thin"))
    b.append(path("M396 272V180H462V272", "thin"))
    b.append(ground())
    # left neighbour
    b.append(path("M28 272V150H108", "thin"))
    b.append(path(rects_d(grid(40, 164, 3, 4, 22, 24, 10, 14)), "thin"))
    # main building
    x0, w, top = 108, 280, 92
    fl = (G - 46 - (top + 14)) / 5
    b.append(rect(x0, top, w, G - top, "fill-mask"))
    b.append(f'<g class="fade">{rect(x0, top, w, 14, "fill-soft")}</g>')
    b.append(rect(x0, top, w, G - top))
    b.append(line(x0, top + 14, x0 + w, top + 14))
    b.append(line(x0, G - 46, x0 + w, G - 46))
    pairs = []
    for r in range(5):
        y = top + 19 + r * fl
        for bay in range(1, 8):
            bx = x0 + 12 + bay * 34
            pairs += [(bx, y, 9, 14), (bx + 13, y, 9, 14)]
    b.append(path(rects_d(pairs)))
    # fire escape on the corner bays
    fe = []
    for r in range(5):
        y = top + 14 + (r + 1) * fl - 3
        fe.append(f"M{x0+6} {f(y)}h40v3h-40z")
        if r < 4:
            fe.append(f"M{x0+40} {f(y+3)}L{x0+12} {f(y+fl)}")
    b.append(path(" ".join(fe), "thin"))
    # storefronts with awnings
    b.append(path(rects_d([(x0 + 10 + i * 68, G - 34, 54, 34) for i in range(4)])))
    b.append(path(" ".join(f"M{x0+6+i*68} {G-36}l6 -8h50l6 8z" for i in range(4)), "accent"))
    # street lamp + trees
    b.append(tree(372, 18, trunk=22))
    return svg("alma-gastown", "ALMA · 455 ABBOTT ST, GASTOWN", b,
               "Line drawing of ALMA: a six-storey historic brick building in Gastown with a fire escape, storefronts and the Woodward's W sign behind")

# ---------------------------------------------------------------- Hillcrest Manor (3850 Cambie)
def hillcrest():
    b = [ground()]
    x0, w, top = 86, 308, 150
    b.append(rect(x0, top, w, G - top))
    b.append(path(f"M{x0-8} {top}H{x0+w+8}V{top+8}H{x0-8}Z"))
    fl = (G - top - 8) / 3
    wins = []
    for r in range(3):
        y = top + 8 + r * fl + 10
        for c in range(3):
            wins.append((x0 + 18 + c * 36, y, 20, 22))
            wins.append((x0 + w - 38 - c * 36, y, 20, 22))
    b.append(path(rects_d(wins)))
    b.append(path(" ".join(f"M{x-2} {f(y+22)}h24" for x, y, *_ in wins), "thin"))
    cx = x0 + w / 2
    b.append(path(f"M{cx-22} {G}V{G-38}H{cx+22}V{G}", "accent"))
    b.append(path(f"M{cx-30} {G-40}H{cx+30}L{cx+24} {G-48}H{cx-24}Z"))
    b.append(path(f"M{cx-12} {top+18}h24v{f(fl*2-10)}h-24z", "thin"))
    b.append(path(f"M{cx-30} {G+4}h60 M{cx-26} {G}v4 M{cx+26} {G}v4", "thin"))
    b.append(tree(46, 24, trunk=26))
    b.append(tree(430, 26, trunk=26))
    return svg("hillcrest-manor", "HILLCREST MANOR · 3850 CAMBIE ST", b,
               "Line drawing of Hillcrest Manor: a three-storey walk-up rental building with a central entry, flanked by large street trees")

# ---------------------------------------------------------------- Front desk / building operations
def front_desk():
    b = []
    b.append(line(16, G, W - 16, G))
    b.append(path("M16 40H464", "thin"))
    # mailboxes
    b.append(rect(34, 96, 96, 116))
    b.append(path(rects_d(grid(40, 102, 4, 6, 23, 18, 19, 14)), "thin"))
    # key cabinet behind the desk
    b.append(rect(196, 92, 88, 64))
    b.append(path(" ".join(f"M{206+c*14} {104+r*16}a3 3 0 1 0 0.1 0" for r in range(3) for c in range(6)), "thin"))
    # desk
    b.append(path("M150 196H330V272H150Z M142 188H338V196H142Z"))
    b.append(path("M170 214h140 M170 232h140", "thin"))
    b.append(path("M300 188v-26h28v26 M314 162v-4", "thin"))
    b.append(path("M176 188a10 10 0 0 1 20 0 M186 178v-3", "accent"))
    # elevator
    b.append(path("M370 272V112H446V272 M408 112V272", ""))
    b.append(path("M392 96h32v10h-32z M402 101h0.1 M414 101h0.1", "thin"))
    # plant
    b.append(path("M66 272l-6 -26h32l-6 26z M76 246c-14 -20 -10 -38 0 -46c10 8 14 26 0 46 M76 246c-20 -8 -26 -22 -22 -30 M76 246c20 -8 26 -22 22 -30", "thin"))
    return svg("front-desk", "FRONT DESK · BUILDING OPERATIONS", b,
               "Line drawing of a residential lobby with a front desk, key cabinet, mailboxes and an elevator")


# ---------------------------------------------------------------- REN (new rental, curved brick corner)
def ren(label="REN · 5510 JOYCE ST"):
    b = [ground()]
    x0, x1, top, wing_top, gf = 64, 424, 78, 96, 236
    b.append(rect(x0, top, x1 - x0, G - top, "fill-mask"))
    b.append(path(f"M{x0} {G}V{top+40}Q{x0} {top} {x0+40} {top}H{x0+226}Q{x0+252} {top} {x0+258} {wing_top}H{x1}V{G}"))
    b.append(line(x0, gf, x1, gf))
    fl = (gf - top - 8) / 5
    # windows on the curved brick block
    b.append(path(rects_d(grid(x0 + 16, top + 10, 7, 5, 31, fl, 13, 20))))
    b.append(path(" ".join(f"M{x0+14} {f(top+10+r*fl+20)}h17" for r in range(5)), "thin"))
    # projecting balconies on the wing
    wx = x0 + 262
    for r in range(4):
        y = wing_top + 12 + r * ((gf - wing_top - 10) / 4)
        for c in range(3):
            bx = wx + 8 + c * 32
            b.append(path(f"M{f(bx)} {f(y)}h12v18h-12z", "thin"))
            b.append(path(f"M{f(bx-4)} {f(y+12)}h22v10h-22z"))
    # brick coursing hint
    b.append(path(hlines_d(x0 + 2, x0 + 230, [top + 40 + i * 32 for i in range(5)]), "thin"))
    # retail ground floor with canopy
    b.append(path(f"M{x0-6} {gf+6}H{x0+240}", "accent"))
    b.append(path(rects_d([(x0 + 10 + i * 56, gf + 10, 46, 26) for i in range(4)])))
    b.append(rect(x0 + 246, gf + 6, 22, 30, "accent"))
    b.append(path(rects_d([(x0 + 280, gf + 10, 34, 26), (x0 + 320, gf + 10, 34, 26)])))
    b.append(tree(40, 14, trunk=20))
    b.append(tree(206, 16, trunk=22))
    b.append(tree(446, 14, trunk=20))
    return svg("ren", label, b,
               "Line drawing of REN: a seven-storey brick rental building with a curved corner, projecting balconies and ground-floor shops")


# ---------------------------------------------------------------- Low-rise rental (parametric)
def walkup(label, aria, storeys=3, bays=6, roof="flat", balconies=False, brick=False, entry="center", width=300):
    b = [ground()]
    flh = 34 if storeys <= 3 else 30
    x0 = (W - width) / 2
    x1 = x0 + width
    top = G - storeys * flh - 6
    b.append(rect(x0, top, width, G - top, "fill-mask"))
    if roof == "hip":
        b.append(path(f"M{f(x0-10)} {f(top)}L{f(x0+34)} {f(top-30)}H{f(x1-34)}L{f(x1+10)} {f(top)}Z"))
    elif roof == "gable":
        b.append(path(f"M{f(x0-10)} {f(top)}L{f((x0+x1)/2)} {f(top-44)}L{f(x1+10)} {f(top)}Z"))
    else:
        b.append(path(f"M{f(x0-6)} {f(top)}H{f(x1+6)}V{f(top+7)}H{f(x0-6)}Z"))
    b.append(rect(x0, top, width, G - top))
    if brick:
        b.append(path(hlines_d(x0 + 2, x1 - 2, [top + 14 + i * 12 for i in range(int((G - top - 18) / 12))]), "thin"))
    bay_w = width / bays
    wins = []
    rails = []
    cx = (x0 + x1) / 2
    for r in range(storeys):
        y = top + 12 + r * flh
        for c in range(bays):
            bx = x0 + c * bay_w + bay_w / 2 - 9
            if entry == "center" and abs((bx + 9) - cx) < bay_w * 0.6 and r == storeys - 1:
                continue
            wins.append((bx, y, 18, 20))
            if balconies and c % 2 == 1 and r < storeys - 1:
                rails.append(f"M{f(bx-6)} {f(y+22)}h30v8h-30z")
    b.append(path(rects_d(wins)))
    if rails:
        b.append(path(" ".join(rails)))
    b.append(path(" ".join(f"M{f(x-2)} {f(y+20)}h22" for x, y, *_ in wins), "thin"))
    ex = cx if entry == "center" else x0 + bay_w * 0.5
    b.append(path(f"M{f(ex-13)} {G}V{G-30}H{f(ex+13)}V{G}", "accent"))
    b.append(path(f"M{f(ex-22)} {G-32}H{f(ex+22)}L{f(ex+18)} {G-38}H{f(ex-18)}Z"))
    b.append(tree(x0 - 26 if x0 > 50 else 34, 18, trunk=22))
    b.append(tree(x1 + 26 if x1 < W - 50 else W - 34, 20, trunk=22))
    return svg("walkup", label, b, aria)

def skyline():
    Wd, Hd = 1200, 230
    wl = 196
    b = []
    b.append(path("M0 128L50 110L96 118L150 92L196 104L244 80L292 98L340 84L372 96L398 70L412 58L424 70L434 54L446 66L470 82L520 92L560 78L612 98L660 76L708 92L760 68L812 88L860 72L910 92L962 78L1010 96L1062 84L1120 102L1200 94", "mtn"))
    # Lions Gate Bridge
    b.append(path(f"M24 166H312 M100 {wl}V112 M236 {wl}V112 M24 158Q64 150 100 112Q168 176 236 112Q272 150 312 158", ""))
    def cable_y(x):
        def q(p0, c, p1, t):
            return (1 - t) ** 2 * p0 + 2 * (1 - t) * t * c + t * t * p1
        if x < 100:
            return q(158, 150, 112, (x - 24) / 76)
        if x < 236:
            return q(112, 176, 112, (x - 100) / 136)
        return q(112, 150, 158, (x - 236) / 76)
    b.append(path(" ".join(f"M{x} 166V{f(cable_y(x))}" for x in range(38, 312, 14) if abs(x - 100) > 4 and abs(x - 236) > 4), "thin"))
    # Stanley Park canopy
    b.append(path(f"M312 {wl}c4 -22 16 -24 22 -12c6 -20 20 -20 24 -6c6 -14 18 -12 20 2c6 -10 16 -6 16 8", "thin"))
    # downtown towers
    towers = [(398, 128, 30), (432, 106, 26), (462, 140, 36), (502, 84, 28), (534, 112, 34), (572, 130, 26)]
    towers += [(660, 92, 32), (698, 58, 22), (724, 120, 38), (766, 100, 28), (798, 138, 44), (846, 122, 30)]
    tw = []
    for x, y, w in towers:
        tw.append(f"M{x} {wl}V{y}H{x+w}V{wl}")
    b.append(path(" ".join(tw)))
    b.append(path("M502 84l14 -12l14 12 M698 58l11 -16l11 16 M709 42v-10", ""))
    b.append(path(" ".join(f"M{x + w/2} {y + 10}V{wl}" for x, y, w in towers[::2]), "thin"))
    # Harbour Centre
    b.append(path(f"M610 {wl}V92H626V{wl} M618 84V58", ""))
    b.append(path("M596 92a22 7 0 1 0 44 0a22 7 0 1 0 -44 0", ""))
    # Science World
    b.append(path(f"M960 {wl}a34 34 0 0 1 68 0", ""))
    b.append(path(f"M966 180L994 {wl} M976 168L1022 186 M994 162V{wl} M1012 166L966 192 M1022 180L994 {wl}", "thin"))
    b.append(path(f"M1000 162v-14", "thin"))
    # East Van houses
    houses = []
    for i, x in enumerate(range(1060, 1190, 32)):
        h = 18 + (i % 2) * 6
        houses.append(f"M{x} {wl}V{wl-h}L{x+13} {wl-h-12}L{x+26} {wl-h}V{wl}")
    b.append(path(" ".join(houses), "thin"))
    # water + sailboat
    b.append(path(f"M0 {wl}H1200", "water"))
    b.append(path(" ".join(f"M{x} {wl+12}q8 -5 16 0t16 0" for x in (60, 220, 470, 760, 900, 1120)), "thin"))
    b.append(path(f"M880 {wl-4}h34l-6 6h-24z M896 {wl-6}V{wl-40}L914 {wl-8}Z", "accent"))
    inner = "".join(b)
    return (
        f'<svg class="sketch" viewBox="0 0 {Wd} {Hd}" role="img" '
        f'aria-label="Line drawing of the Vancouver skyline: North Shore mountains and the Lions, Lions Gate Bridge, downtown towers including Harbour Centre, and Science World" '
        f'xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMax meet">{inner}'
        f'<g class="fade"><text class="label" x="{Wd-8}" y="{Hd-4}" text-anchor="end">VANCOUVER, B.C.</text></g></svg>'
    )


BUILDERS = {
    "ren": ren,
    "sunrise": sunrise,
    "timbre-harmony": timbre_harmony,
    "hawthorn": hawthorn,
    "independent": independent,
    "hudson": hudson,
    "alma": alma,
    "skyline": skyline,
}

STANDALONE_CSS = (
    "<style>.sketch path,.sketch rect,.sketch line,.sketch circle{fill:none;stroke:#1b1e22;stroke-width:1.4;"
    "stroke-linecap:round;stroke-linejoin:round}.thin{stroke:#6b717a!important;stroke-width:.9!important}"
    ".accent{stroke:#1f3a5f!important}.mtn{stroke:#6b717a!important}.water{stroke:#1f3a5f!important}"
    ".fill-soft{fill:#ece7de!important;stroke:none!important}.fill-mask{fill:#f1ede5!important;stroke:none!important}"
    ".label{fill:#6b717a;font:9px 'IBM Plex Mono',monospace;letter-spacing:.14em}</style>"
)


def build_all(out_dir):
    os.makedirs(out_dir, exist_ok=True)
    snippets = {}
    from mf_sketches import MF_BUILDERS
    from we_sketches import WE_BUILDERS
    for key, fn in {**BUILDERS, **MF_BUILDERS, **WE_BUILDERS}.items():
        s = fn()
        snippets[key] = s
        standalone = s.replace('class="sketch"', 'class="sketch"', 1).replace(">", ">" + STANDALONE_CSS, 1)
        with open(os.path.join(out_dir, f"{key}.svg"), "w", encoding="utf-8") as fh:
            fh.write(standalone)
    return snippets


if __name__ == "__main__":
    import sys
    snippets = build_all(sys.argv[1] if len(sys.argv) > 1 else "out")
    for k, v in snippets.items():
        print(k, len(v))
