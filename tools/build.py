"""Builds index.html from content.py + sketches.py. Usage: py build2.py <project-dir>"""
import os, re, sys, importlib
sys.path.insert(0, os.path.dirname(__file__))
import sketches, content
importlib.reload(content)

project = sys.argv[1]
SK = sketches.build_all(os.path.join(project, "assets", "img", "illustrations"))

ICON = {
    "arrow-down": '<path d="M12 5v14M6 13l6 6 6-6"/>',
    "arrow-up-right": '<path d="M7 17 17 7M9 7h8v8"/>',
    "arrow-right": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "check": '<path d="m5 12 4 4 10-10"/>',
    "mail": '<path d="M3 6h18v12H3zM3 7l9 6 9-6"/>',
    "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>',
}


def icon(name, cls="icon"):
    return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true">{ICON[name]}</svg>'


def media_block(sketch_key, media, indent):
    i = " " * indent
    out = [f'{i}<div class="card__visual" data-draw data-view="sketch">',
           f'{i}  <div class="view view--sketch">{SK[sketch_key]}</div>']
    if media:
        b = media["base"]
        out += [
            f'{i}  <div class="view view--photo" aria-hidden="true">',
            f'{i}    <img src="assets/img/photos/{b}-720.webp" srcset="assets/img/photos/{b}-720.webp 720w, assets/img/photos/{b}-1200.webp 1200w" sizes="(min-width: 900px) 540px, 100vw" width="{media["w"]}" height="{media["h"]}" loading="lazy" decoding="async" alt="{media["alt"]}">',
        ]
        if media["kind"] == "Rendering":
            out.append(f'{i}    <span class="view-caption">Architectural rendering</span>')
        out += [
            f'{i}  </div>',
            f'{i}  <div class="view-toggle" role="group" aria-label="Image style">',
            f'{i}    <button type="button" data-view="sketch" aria-pressed="true">Sketch</button>',
            f'{i}    <button type="button" data-view="photo" aria-pressed="false">{media["kind"]}</button>',
            f'{i}  </div>',
        ]
    out.append(f'{i}</div>')
    return "\n".join(out)


def facts_block(facts, indent):
    i = " " * indent
    items = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in facts)
    return f'{i}<dl class="card__facts">{items}</dl>'


def roles_block(roles, indent):
    i = " " * indent
    lis = "".join(f"<li>{r}</li>" for r in roles)
    return (f'{i}<div>\n{i}  <p class="roles-label">What I handle</p>\n'
            f'{i}  <ul class="roles">{lis}</ul>\n{i}</div>')


def route_stop(s):
    sid = f"stop-{s['key']}"
    role_cls = "tag tag--solid" if s["role"].startswith("Head") else "tag tag--solid tag--alt"
    return "\n".join([
        f'          <article class="stop" aria-labelledby="{sid}">',
        f'            <div class="stop__node" aria-hidden="true">{s["n"]}</div>',
        f'            <div class="stop__card card reveal">',
        media_block(s["sketch"], s.get("media"), 14),
        f'              <div class="card__body">',
        f'                <div class="card__tags"><span class="{role_cls}">{s["role"]}</span><span class="tag">{s["kind"]}</span></div>',
        f'                <h3 class="card__title" id="{sid}">{s["title"]}</h3>',
        f'                <p class="card__address">{s["address"]}</p>',
        roles_block(s["roles"], 16),
        f'                <p class="card__desc">{s["desc"]}</p>',
        facts_block(s["facts"], 16),
        f'              </div>',
        f'            </div>',
        f'            <div class="stop__aside reveal" aria-hidden="true">',
        f'              <p class="hood">{s["hood"]}</p>',
        f'              <p class="hood-sub">{s["hood_sub"]}</p>',
        f'            </div>',
        f'          </article>',
    ])


def mf_card(m):
    sid = f"mf-{m['key']}"
    return "\n".join([
        f'          <article class="card card--compact reveal" aria-labelledby="{sid}">',
        media_block(m["sketch"], m.get("media"), 12),
        f'            <div class="card__body">',
        f'              <p class="card__address">{m["hood"]}</p>',
        f'              <h3 class="card__title" id="{sid}">{m["title"]}</h3>',
        (f'              <p class="card__subtitle">{m["subtitle"]}</p>' if m.get("subtitle") else ""),
        f'              <p class="card__desc">{m["desc"]}</p>',
        facts_block(m["facts"], 14),
        f'            </div>',
        f'          </article>',
    ]).replace("\n\n", "\n")


def strata_card(s):
    sid = f"strata-{s['key']}"
    return "\n".join([
        f'            <article class="card card--compact reveal" aria-labelledby="{sid}">',
        media_block(s["sketch"], s.get("media"), 14),
        f'              <div class="card__body">',
        f'                <div class="card__tags"><span class="tag">Strata suite</span></div>',
        f'                <h3 class="card__title" id="{sid}">{s["title"]}</h3>',
        f'                <p class="card__address">{s["address"]}</p>',
        f'                <p class="card__desc">{s["desc"]}</p>',
        facts_block(s["facts"], 16),
        f'              </div>',
        f'            </article>',
    ])


route = list(content.ROUTE)
if content.REN_DATA:
    route.append(content.REN_DATA)

tpl = open(os.path.join(os.path.dirname(__file__), "page.template.html"), encoding="utf-8").read()
html = tpl
html = html.replace("{{route}}", "\n\n".join(route_stop(s) for s in route))
html = html.replace("{{multifamily}}", "\n".join(mf_card(m) for m in content.MULTIFAMILY))
html = html.replace("{{strata}}", "\n".join(strata_card(s) for s in content.STRATA))
html = html.replace("{{route_count}}", {4: "Four", 5: "Five", 6: "Six"}[len(route)])
html = html.replace("{{mf_count}}", {0: "Six", 5: "Five", 6: "Six", 7: "Seven"}[len(content.MULTIFAMILY)])
logo_rel = "assets/img/brokerage/basepoint-logo.svg"
if os.path.exists(os.path.join(project, logo_rel)):
    logo = f'<img src="{logo_rel}" alt="Basepoint Real Estate Group" width="180" height="42">'
else:
    logo = '<span class="wordmark">BASEPOINT<small>Real Estate Group</small></span>'


def job_item(j):
    return "\n".join([
        '            <li class="job reveal">',
        f'              <p class="job__when">{j["when"]}</p>',
        '              <div>',
        f'                <h3 class="job__role">{j["role"]}</h3>',
        f'                <p class="job__org">{j["org"]}</p>',
        f'                <p class="job__text">{j["text"]}</p>',
        '              </div>',
        '            </li>',
    ])


def group_block(g):
    items = "".join(f"<li>{b}</li>" for b in g["buildings"])
    return (f'            <div class="bl-group"><p class="bl-label">{g["label"]}</p>'
            f'<ul class="bl-items">{items}</ul></div>')


groups = getattr(content, "BUILDING_GROUPS", [])
n_props = sum(len(g["buildings"]) for g in groups)
def we_card(w):
    sid = f"we-{w['key']}"
    return "\n".join([
        f'          <article class="we-card reveal" aria-labelledby="{sid}">',
        f'            <div class="we-card__visual" data-draw>{SK[w["sketch"]]}</div>',
        f'            <h3 class="we-card__title" id="{sid}">{w["title"]}</h3>',
        f'            <p class="we-card__address">{w["address"]}</p>',
        f'            <p class="we-card__facts">{w["facts"]}</p>',
        '          </article>',
    ])


html = html.replace("{{westend}}", "\n".join(we_card(w) for w in getattr(content, "WEST_END", [])))
html = html.replace("{{jobs}}", "\n".join(job_item(j) for j in getattr(content, "JOBS", [])))
html = html.replace("{{building_groups}}", "\n".join(group_block(g) for g in groups))
html = html.replace("{{fact4_value}}", str(n_props))
html = html.replace("{{fact4_label}}", "Properties across Metro Vancouver I've leased, managed or worked in")
lic = getattr(content, "LICENSED", False)
html = html.replace("{{brokerage_logo}}", logo)
html = html.replace("{{brokerage_text}}", content.BROKERAGE_TEXT_LICENSED if lic else content.BROKERAGE_TEXT)
html = html.replace("{{current_title}}", content.CURRENT_TITLE_LICENSED if lic else content.CURRENT_TITLE)
html = re.sub(r"\{\{icon:([a-z-]+)\}\}", lambda m: icon(m.group(1)), html)
html = re.sub(r"\{\{sketch:([a-z-]+)\}\}", lambda m: SK[m.group(1)], html)
left = re.findall(r"\{\{[^}]+\}\}", html)
assert not left, left
assert "—" not in html, "em dash found"
open(os.path.join(project, "index.html"), "w", encoding="utf-8", newline="\n").write(html)
print("index.html", len(html) // 1024, "KB;", len(route), "route stops;", len(content.MULTIFAMILY), "multifamily")
