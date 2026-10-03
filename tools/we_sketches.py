"""West End rental towers (Forth Gen Holdings portfolio): small portrait sketches, viewBox 240x300."""
from sketches import f, rect, line, path, circle, rects_d, grid, hlines_d, vlines_d

WW, WH, WG = 240, 300, 282


def wground():
    return line(8, WG, WW - 8, WG) + line(8, WG + 7, WW - 8, WG + 7, "thin")


def wtree(cx, r=12, trunk=14):
    top = WG - trunk
    cy = top - r + 4
    return circle(cx, cy, r, "fill-mask") + line(cx, WG, cx, top + 2) + circle(cx, cy, r)


def wsvg(body, aria):
    return (f'<svg class="sketch" viewBox="0 0 {WW} {WH}" role="img" aria-label="{aria}" '
            f'xmlns="http://www.w3.org/2000/svg">{"".join(body)}</svg>')


def tower(x0, x1, storeys, flh):
    top = WG - storeys * flh
    return top, [rect(x0, top, x1 - x0, WG - top, "fill-mask"), rect(x0, top, x1 - x0, WG - top)]


def bayside():
    x0, x1, n, flh = 62, 178, 10, 19
    top, b = tower(x0, x1, n, flh)
    b = [wground()] + b
    b.append(path(f"M{x0-4} {top}h{x1-x0+8}v6h-{x1-x0+8}z"))
    b.append(path(hlines_d(x0 - 3, x1 + 3, [top + flh * i for i in range(1, n)])))
    b.append(path(" ".join(f"M{x0+8} {f(top+flh*i+5)}h{x1-x0-16}v8h-{x1-x0-16}z" for i in range(n - 1)), "thin"))
    b.append(path(" ".join(f"M{x0+8+k*20} {f(top+flh*i+5)}v8" for i in range(n - 1) for k in range(1, 5)), "thin"))
    cx = (x0 + x1) / 2
    b.append(path(f"M{cx-12} {WG}V{WG-14}H{cx+12}V{WG}", "accent"))
    b.append(wtree(38, 14, 18))
    b.append(wtree(204, 12, 16))
    return wsvg(b, "Line drawing of Bayside Towers: a ten-storey mid-century concrete tower with horizontal window and balcony bands")


def braeview():
    x0, x1, n, flh = 84, 156, 14, 14.5
    top, b = tower(x0, x1, n, flh)
    b = [wground()] + b
    b.append(path(f"M{x0+10} {f(top)}V{f(top-10)}H{x0+44}V{f(top)} M{x0+20} {f(top-10)}V{f(top-18)}H{x0+36}V{f(top-10)}"))
    b.append(path(rects_d(grid(x0 + 8, top + 4, 3, n - 1, 15, flh, 9, 8))))
    b.append(path(" ".join(f"M{x1} {f(top+flh*i+3)}h10v10h-10" for i in range(n - 1))))
    cx = (x0 + x1) / 2
    b.append(path(f"M{cx-10} {WG}V{WG-12}H{cx+10}V{WG}", "accent"))
    b.append(path(f"M40 {WG}h40v-8h-40z", "thin"))
    b.append(wtree(46, 14, 18))
    b.append(wtree(200, 14, 18))
    return wsvg(b, "Line drawing of Braeview Manor: a slender light concrete tower with punched windows and stacked balconies")


def elliot():
    x0, x1, n, flh = 70, 170, 12, 16.5
    top, b = tower(x0, x1, n, flh)
    b = [wground()] + b
    b.append(path(f"M{x0-3} {f(top)}h{x1-x0+6}v5h-{x1-x0+6}z"))
    b.append(path(rects_d(grid(x0 + 10, top + 6, 4, n - 1, 22, flh, 14, 9))))
    b.append(path(" ".join(f"M{x0+6} {f(top+flh*(i+1)-2)}h{x1-x0-12}" for i in range(n - 1)), "thin"))
    cx = (x0 + x1) / 2
    b.append(path(f"M{cx-12} {WG}V{WG-14}H{cx+12}V{WG}", "accent"))
    b.append(wtree(40, 14, 18))
    b.append(wtree(202, 12, 16))
    return wsvg(b, "Line drawing of Elliot Towers: a concrete residential high-rise with a flat roof and balconies")


def heather():
    x0, x1, n, flh = 84, 164, 13, 15.5
    top, b = tower(x0, x1, n, flh)
    b = [wground()] + b
    b.append(path(f"M{x0-6} {f(top)}l14 -12l14 12l14 -12l14 12l14 -12l14 12l14 -12l2 12"))
    b.append(path(" ".join(f"M{x0-12} {f(top+flh*i+4)}h18v{f(flh-6)}h-18" for i in range(n - 1))))
    b.append(path(f"M{x0+40} {f(top+4)}h12v{f(WG-top-24)}h-12z", "accent"))
    b.append(path(rects_d(grid(x0 + 14, top + 5, 1, n - 1, 0, flh, 18, 8)) + " " +
                  rects_d(grid(x0 + 58, top + 5, 1, n - 1, 0, flh, 14, 8))))
    cx = (x0 + x1) / 2
    b.append(path(f"M{cx-10} {WG}V{WG-12}H{cx+10}V{WG}", "accent"))
    b.append(wtree(40, 14, 18))
    b.append(wtree(200, 14, 18))
    return wsvg(b, "Line drawing of Heather House: a tall narrow white tower with stacked balconies, a vertical window strip and angular roof canopies")


def kevin():
    x0, x1, n, flh = 30, 210, 9, 20
    top, b = tower(x0, x1, n, flh)
    b = [wground()] + b
    b.append(path(f"M{x0-3} {f(top)}h{x1-x0+6}v5h-{x1-x0+6}z"))
    b.append(path(" ".join(f"M{x0+12} {f(top+flh*i+14)}h{x1-x0-24}v6h-{x1-x0-24}z" for i in range(n - 1))))
    b.append(path(" ".join(f"M{x0+12+k*13} {f(top+flh*i+14)}v6" for i in range(n - 1) for k in range(1, 12)), "thin"))
    b.append(path(rects_d([(x0 + 18 + k * 30, top + flh * i + 4, 16, 9) for i in range(n - 1) for k in range(6)]), "thin"))
    cx = (x0 + x1) / 2
    b.append(path(f"M{cx-16} {WG}V{WG-14}H{cx+16}V{WG}", "accent"))
    b.append(path(f"M{cx-24} {WG-16}h48", ""))
    return wsvg(b, "Line drawing of Kevin Manor: a wide nine-storey mid-century slab with continuous horizontal balcony bands")


def rosewoods():
    x0, x1, n, flh = 16, 224, 4, 24
    top, b = tower(x0, x1, n, flh)
    b = [wground()] + b
    b.append(path(f"M{x0-4} {f(top)}h{x1-x0+8}v5h-{x1-x0+8}z"))
    b.append(path(hlines_d(x0, x1, [top + flh * i for i in range(1, n)]), "thin"))
    b.append(path(rects_d([(x0 + 10 + k * 52, top + flh * i + 5, 32, flh - 9) for i in range(n) for k in range(4) if not (i == n - 1 and k == 2)])))
    b.append(path(" ".join(f"M{x0+10+k*52} {f(top+flh*i+flh-9)}h32" for i in range(n) for k in range(4)), "thin"))
    b.append(path(f"M{x0+114} {WG}V{WG-18}H{x0+134}V{WG}", "accent"))
    b.append(wtree(52, 18, 22))
    b.append(wtree(190, 20, 22))
    return wsvg(b, "Line drawing of Rosewoods: a long, low four-storey building with large recessed balconies and mature trees")


WE_BUILDERS = {
    "we-bayside": bayside,
    "we-braeview": braeview,
    "we-elliot": elliot,
    "we-heather": heather,
    "we-kevin": kevin,
    "we-rosewoods": rosewoods,
}
