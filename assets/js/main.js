/* Michael Tapia: portfolio interactions
   - Scroll-drawn leasing route
   - Building sketches that draw themselves into view
   - Sketch / photo toggle on property cards
   Everything degrades to a static, fully readable page without JS. */

(() => {
  "use strict";

  const doc = document.documentElement;
  doc.classList.add("js");

  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

  /* ---------- Header state ---------- */

  const header = document.querySelector(".site-header");
  const onScrollHeader = () => header && header.classList.toggle("is-scrolled", window.scrollY > 8);

  /* ---------- Sketch preparation ---------- */

  const DRAWABLE = "path, rect, line, polyline, polygon, circle, ellipse";

  document.querySelectorAll(".sketch").forEach((svg) => {
    svg.querySelectorAll(DRAWABLE).forEach((el) => {
      if (el.closest(".fade, .label") || /\bfill-/.test(el.getAttribute("class") || "")) return;
      el.setAttribute("pathLength", "1");
      el.classList.add("ln");
    });
  });

  /* ---------- Reveal + draw on enter ---------- */

  const revealTargets = document.querySelectorAll(".reveal, [data-draw]");

  if ("IntersectionObserver" in window && !reduceMotion.matches) {
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          entry.target.classList.add("is-visible", "is-drawn");
          io.unobserve(entry.target);
        });
      },
      { threshold: 0.18, rootMargin: "0px 0px -8% 0px" }
    );
    revealTargets.forEach((el) => io.observe(el));
  } else {
    revealTargets.forEach((el) => el.classList.add("is-visible", "is-drawn"));
  }

  /* ---------- Sketch / photo toggle ---------- */

  document.querySelectorAll(".view-toggle").forEach((group) => {
    const visual = group.closest(".card__visual");
    group.addEventListener("click", (event) => {
      const button = event.target.closest("button[data-view]");
      if (!button || !visual) return;
      const view = button.dataset.view;
      visual.dataset.view = view;
      group.querySelectorAll("button[data-view]").forEach((b) => {
        b.setAttribute("aria-pressed", String(b === button));
      });
      visual.querySelectorAll(".view").forEach((v) => {
        v.setAttribute("aria-hidden", String(!v.classList.contains(`view--${view}`)));
      });
    });
  });

  /* ---------- Leasing route ---------- */

  const SVG_NS = "http://www.w3.org/2000/svg";

  class Route {
    constructor(el) {
      this.el = el;
      this.stops = [...el.querySelectorAll(".stop")];
      this.end = el.querySelector(".route-end__pin");
      this.svg = document.createElementNS(SVG_NS, "svg");
      this.svg.setAttribute("class", "route__svg");
      this.svg.setAttribute("aria-hidden", "true");
      this.svg.setAttribute("focusable", "false");
      this.base = document.createElementNS(SVG_NS, "path");
      this.base.setAttribute("class", "route__base");
      this.progress = document.createElementNS(SVG_NS, "path");
      this.progress.setAttribute("class", "route__progress");
      this.svg.append(this.base, this.progress);
      el.prepend(this.svg);
      this.samples = [];
      this.length = 0;
      this.nodeY = [];
      this.frame = 0;
    }

    centerOf(node, origin) {
      const r = node.getBoundingClientRect();
      return { x: r.left + r.width / 2 - origin.left, y: r.top + r.height / 2 - origin.top };
    }

    build() {
      const origin = this.el.getBoundingClientRect();
      const w = origin.width;
      const h = this.el.scrollHeight;
      this.svg.setAttribute("viewBox", `0 0 ${w} ${h}`);

      const nodes = this.stops.map((s) => this.centerOf(s.querySelector(".stop__node"), origin));
      if (!nodes.length) return;
      this.nodeY = nodes.map((p) => p.y);

      const wide = window.matchMedia("(min-width: 900px)").matches;
      const swing = wide ? Math.min(420, w * 0.32) : 0;

      // Side where each stop's empty space is (opposite the card): odd stops -> left, even -> right.
      const side = (i) => (i % 2 === 0 ? -1 : 1);

      const points = [{ x: nodes[0].x, y: 0 }, ...nodes];
      if (this.end) points.push(this.centerOf(this.end, origin));

      let d = `M ${points[0].x.toFixed(1)} ${points[0].y.toFixed(1)}`;
      for (let i = 1; i < points.length; i++) {
        const a = points[i - 1];
        const b = points[i];
        const dy = b.y - a.y;
        // Leave each stop toward its empty side and arrive at the next from its empty side,
        // which makes an S-curve that weaves around the cards. First and last segments stay gentle.
        const toEnd = this.end && i === points.length - 1;
        const sa = i === 1 ? 0 : side(i - 2) * swing * (toEnd ? 0.5 : 1);
        const sb = toEnd ? 0 : side(i - 1) * swing * (i === 1 ? 0.5 : 1);
        const c1 = { x: a.x + sa, y: a.y + dy * 0.5 };
        const c2 = { x: b.x + sb, y: b.y - dy * 0.5 };
        d += ` C ${c1.x.toFixed(1)} ${c1.y.toFixed(1)}, ${c2.x.toFixed(1)} ${c2.y.toFixed(1)}, ${b.x.toFixed(1)} ${b.y.toFixed(1)}`;
      }

      this.base.setAttribute("d", d);
      this.progress.setAttribute("d", d);
      this.length = this.progress.getTotalLength();
      this.progress.style.strokeDasharray = `${this.length}`;

      // Sample y along the path so scroll position maps to drawn length.
      const steps = Math.max(80, Math.round(this.length / 10));
      this.samples = [];
      let maxY = -Infinity;
      for (let i = 0; i <= steps; i++) {
        const len = (this.length * i) / steps;
        maxY = Math.max(maxY, this.progress.getPointAtLength(len).y);
        this.samples.push({ len, y: maxY });
      }
      this.update();
    }

    lengthAtY(y) {
      const s = this.samples;
      if (!s.length) return 0;
      if (y <= s[0].y) return 0;
      if (y >= s[s.length - 1].y) return this.length;
      let lo = 0;
      let hi = s.length - 1;
      while (hi - lo > 1) {
        const mid = (lo + hi) >> 1;
        if (s[mid].y < y) lo = mid; else hi = mid;
      }
      const a = s[lo];
      const b = s[hi];
      const t = b.y === a.y ? 0 : (y - a.y) / (b.y - a.y);
      return a.len + (b.len - a.len) * t;
    }

    update() {
      const top = this.el.getBoundingClientRect().top;
      const pen = reduceMotion.matches ? Infinity : window.innerHeight * 0.62 - top;
      const drawn = this.lengthAtY(pen);
      this.progress.style.strokeDashoffset = `${Math.max(0, this.length - drawn)}`;
      this.stops.forEach((stop, i) => stop.classList.toggle("is-reached", this.nodeY[i] <= pen));
    }

    schedule() {
      if (this.frame) return;
      this.frame = requestAnimationFrame(() => {
        this.frame = 0;
        this.update();
      });
    }
  }

  const routes = [...document.querySelectorAll(".route")].map((el) => new Route(el));

  const rebuild = () => routes.forEach((r) => r.build());
  let resizeTimer = 0;
  const onResize = () => {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(rebuild, 120);
  };

  rebuild();
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(rebuild);
  window.addEventListener("load", rebuild);
  window.addEventListener("resize", onResize);
  if ("ResizeObserver" in window) {
    const ro = new ResizeObserver(onResize);
    routes.forEach((r) => ro.observe(r.el));
  }

  window.addEventListener(
    "scroll",
    () => {
      onScrollHeader();
      routes.forEach((r) => r.schedule());
    },
    { passive: true }
  );
  onScrollHeader();

  /* ---------- Current section in nav ---------- */

  const navLinks = [...document.querySelectorAll(".site-nav a[href^='#']")];
  const sections = navLinks
    .map((a) => document.querySelector(a.getAttribute("href")))
    .filter(Boolean);

  if ("IntersectionObserver" in window && sections.length) {
    const navIO = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          navLinks.forEach((a) => {
            if (a.getAttribute("href") === `#${entry.target.id}`) a.setAttribute("aria-current", "true");
            else a.removeAttribute("aria-current");
          });
        });
      },
      { rootMargin: "-45% 0px -50% 0px" }
    );
    sections.forEach((s) => navIO.observe(s));
  }
})();
