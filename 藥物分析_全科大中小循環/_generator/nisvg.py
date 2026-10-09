# -*- coding: utf-8 -*-
"""Tiny SVG layout helper for the 藥物分析 Ni figures.

Hand-wrapped CJK text (SVG has no auto wrap), panels, arrows.
Every <text> carries data-b="<container rect id>" so the browser checker
can verify that real glyph boxes stay inside their panel.
"""
import re
from xml.sax.saxutils import escape

FONT = ("Noto Sans CJK TC, Noto Sans TC, PingFang TC, Microsoft JhengHei, "
        "WenQuanYi Zen Hei, Droid Sans Fallback, sans-serif")

INK = "#24343f"
MUTED = "#61717a"
RED = "#b72d4a"
BG = "#f8f6ee"

PANEL = {
    "A": ("#fff1c8", "#9e771c"),
    "B": ("#d9eeea", "#286c68"),
    "C": ("#dcecdc", "#356844"),
    "D": ("#e8e1f2", "#685185"),
    "E": ("#dceaf7", "#326991"),
    "F": ("#f5dfe2", "#b72d4a"),
    "W": ("#ffffff", "#61717a"),
    "G": ("#eef0ec", "#61717a"),
}

CLOSE_P = set("，。、；：！？）」』】〉》％,.;:!?)]}…")
OPEN_P = set("（「『【〈《([{")


def cw(ch):
    """Conservative advance width of one char, in em."""
    o = ord(ch)
    if ch == " ":
        return 0.32
    if ch in " ":
        return 0.2
    if (0x2E80 <= o <= 0x9FFF) or (0xF900 <= o <= 0xFAFF) or (0xFF00 <= o <= 0xFFEF) \
            or (0x3000 <= o <= 0x303F):
        return 1.0
    if ch in "→←↑↓↔⇄⇒⇢×÷±≈≠≤≥∝√∑∫∞≡⟶·•○●◆◇■□★☆①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳…—":
        return 1.0
    if ch in "₀₁₂₃₄₅₆₇₈₉₊₋⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻ₐₑₒₓₙ":
        return 0.5
    if 0x0370 <= o <= 0x03FF:
        return 0.68
    if ch.isdigit():
        return 0.58
    if ch.isupper():
        return 0.7
    if ch.islower():
        return 0.58
    if ch in "′″'`":
        return 0.3
    if ch in ".,:;!|":
        return 0.32
    if ch in "()[]{}/\\-":
        return 0.4
    return 0.62


def tw(s, size):
    return sum(cw(c) for c in s) * size


def parse_runs(s):
    """'**bold**' and '{{#hex|colored}}' markup -> [(text, bold, color)]."""
    runs = []
    pat = re.compile(r"\*\*(.+?)\*\*|\{\{(#[0-9a-fA-F]{6})\|(.+?)\}\}")
    pos = 0
    for m in pat.finditer(s):
        if m.start() > pos:
            runs.append((s[pos:m.start()], False, None))
        if m.group(1) is not None:
            runs.append((m.group(1), True, None))
        else:
            runs.append((m.group(3), True, m.group(2)))
        pos = m.end()
    if pos < len(s):
        runs.append((s[pos:], False, None))
    return runs


WORD = re.compile(r"[A-Za-z0-9_·\(\)\[\]\.\+\-/=′'%°\^₀-₉⁰-⁹¹²³⁺⁻αβγδεζημνλπσρτφχψωΦΔΣΩ]+(?:–[A-Za-z0-9]+)*")


def tokens(runs):
    out = []
    for text, bold, color in runs:
        i = 0
        while i < len(text):
            m = WORD.match(text, i)
            if m and m.end() > i:
                out.append((m.group(0), bold, color))
                i = m.end()
            else:
                out.append((text[i], bold, color))
                i += 1
    return out


def wrap(s, width, size):
    """Return list of lines; each line is a list of (text, bold, color)."""
    lines = []
    for para in s.split("\n"):
        toks = tokens(parse_runs(para))
        cur, curw = [], 0.0
        for t in toks:
            w = tw(t[0], size) * (1.04 if t[1] else 1.0)
            if cur and curw + w > width:
                if t[0] in CLOSE_P:
                    if curw + w <= width + size * 0.3:
                        cur.append(t)
                        curw += w
                        continue
                    carry = [t]
                    while cur and carry[0][0] in CLOSE_P and len(cur) > 1:
                        carry.insert(0, cur.pop())
                    while len(cur) > 1 and cur[-1][0] in OPEN_P:
                        carry.insert(0, cur.pop())
                    if cur:
                        lines.append(cur)
                        cur = carry
                        curw = sum(tw(x[0], size) for x in cur)
                        continue
                if t[0] == " ":
                    lines.append(cur)
                    cur, curw = [], 0.0
                    continue
                carry = []
                if cur and cur[-1][0] in OPEN_P:
                    carry = [cur.pop()]
                lines.append(cur)
                cur = carry + [t]
                curw = sum(tw(x[0], size) for x in cur)
            else:
                if not cur and t[0] == " ":
                    continue
                cur.append(t)
                curw += w
        lines.append(cur)
    return lines


def merge(line):
    out = []
    for t, b, c in line:
        if out and out[-1][1] == b and out[-1][2] == c:
            out[-1] = (out[-1][0] + t, b, c)
        else:
            out.append((t, b, c))
    return out


class SVG:
    def __init__(self, width, prefix, title, desc):
        self.w = width
        self.prefix = prefix
        self.title = title
        self.desc = desc
        self.items = []
        self.maxy = 0
        self.nid = 0
        self.markers = set()

    def _id(self, tag="b"):
        self.nid += 1
        return f"{self.prefix}-{tag}{self.nid}"

    def _y(self, y):
        self.maxy = max(self.maxy, y)

    # ---------- primitives ----------
    def new_id(self):
        return self._id()

    def mark(self):
        return len(self.items)

    def rect(self, x, y, w, h, style="W", rx=18, sw=2, dash=None, fill=None, stroke=None,
             rid=None, at=None):
        rid = rid or self._id()
        f, s = PANEL[style]
        f = fill or f
        s = stroke or s
        d = f' stroke-dasharray="{dash}"' if dash else ""
        el = (f'<rect id="{rid}" x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" '
              f'rx="{rx}" fill="{f}" stroke="{s}" stroke-width="{sw}"{d}/>')
        if at is None:
            self.items.append(el)
        else:
            self.items.insert(at, el)
        self._y(y + h)
        return rid

    def text(self, x, y, s, size=23, color=INK, weight=400, anchor="start", box=None):
        runs = merge([t for t in tokens(parse_runs(s))])
        self._emit_line(x, y, runs, size, color, weight, anchor, box)
        self._y(y + size * 0.3)

    def _emit_line(self, x, y, runs, size, color, weight, anchor, box):
        b = f' data-b="{box}"' if box else ""
        parts = []
        for t, bold, c in runs:
            attrs = []
            if bold:
                attrs.append('font-weight="700"')
            if c:
                attrs.append(f'fill="{c}"')
            if attrs:
                parts.append(f'<tspan {" ".join(attrs)}>{escape(t)}</tspan>')
            else:
                parts.append(escape(t))
        a = f' text-anchor="{anchor}"' if anchor != "start" else ""
        self.items.append(
            f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" font-weight="{weight}" '
            f'fill="{color}"{a}{b} xml:space="preserve">{"".join(parts)}</text>')

    def para(self, x, y, w, s, size=23, color=INK, lh=1.45, weight=400, box=None, measure=False):
        """Draw wrapped paragraph; y is top of the block. Returns bottom y."""
        lines = wrap(s, w, size)
        base = y + size * 0.95
        for ln in lines:
            if not measure:
                self._emit_line(x, base, merge(ln), size, color, weight, "start", box)
            base += size * lh
        bottom = y + len(lines) * size * lh
        if not measure:
            self._y(bottom)
        return bottom

    def para_h(self, w, s, size=23, lh=1.45):
        return len(wrap(s, w, size)) * size * lh

    def card(self, x, y, w, title=None, body=(), style="W", tsize=27, bsize=23, pad=22,
             gap=8, min_h=0, title_color=None, lh=1.45, rx=18, sw=2, body_color=INK, dash=None):
        """Auto-height panel. body: list of strings (each a paragraph)."""
        inner = w - 2 * pad
        h = pad
        if title:
            h += self.para_h(inner, title, tsize, 1.3) + gap
        for i, p in enumerate(body):
            h += self.para_h(inner, p, bsize, lh)
            if i < len(body) - 1:
                h += gap
        h += pad
        h = max(h, min_h)
        rid = self.rect(x, y, w, h, style, rx=rx, sw=sw, dash=dash)
        cy = y + pad
        if title:
            tc = title_color or PANEL[style][1]
            if style == "W" and not title_color:
                tc = INK
            cy = self.para(x + pad, cy, inner, title, tsize, tc, 1.3, 700, box=rid) + gap
        for i, p in enumerate(body):
            cy = self.para(x + pad, cy, inner, p, bsize, body_color, lh, box=rid)
            if i < len(body) - 1:
                cy += gap
        return y + h, rid

    def card_h(self, w, title=None, body=(), tsize=27, bsize=23, pad=22, gap=8, lh=1.45):
        inner = w - 2 * pad
        h = pad
        if title:
            h += self.para_h(inner, title, tsize, 1.3) + gap
        for i, p in enumerate(body):
            h += self.para_h(inner, p, bsize, lh)
            if i < len(body) - 1:
                h += gap
        return h + pad

    def arrow(self, pts, color=MUTED, width=3, dash=None, head=True, head_size=12):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        p = " ".join(f"{a:.1f},{b:.1f}" for a, b in pts)
        self.items.append(
            f'<polyline class="arrow" points="{p}" fill="none" stroke="{color}" stroke-width="{width}" '
            f'stroke-linecap="round" stroke-linejoin="round"{d}/>')
        if head:
            (x1, y1), (x2, y2) = pts[-2], pts[-1]
            import math
            ang = math.atan2(y2 - y1, x2 - x1)
            hs = head_size
            a1 = ang + math.pi * 0.83
            a2 = ang - math.pi * 0.83
            p1 = (x2 + hs * math.cos(a1), y2 + hs * math.sin(a1))
            p2 = (x2 + hs * math.cos(a2), y2 + hs * math.sin(a2))
            self.items.append(
                f'<polygon class="arrowhead" points="{x2:.1f},{y2:.1f} {p1[0]:.1f},{p1[1]:.1f} '
                f'{p2[0]:.1f},{p2[1]:.1f}" fill="{color}"/>')
        for a, b in pts:
            self._y(b)

    def line(self, x1, y1, x2, y2, color=MUTED, width=2, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.items.append(
            f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" '
            f'stroke-width="{width}"{d}/>')

    def raw(self, s):
        self.items.append(s)

    def save(self, path, height=None, margin=56):
        h = height or int(self.maxy + margin)
        tid, did = f"{self.prefix}-title", f"{self.prefix}-desc"
        head = (
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{h}" '
            f'viewBox="0 0 {self.w} {h}" role="img" aria-labelledby="{tid} {did}" '
            f'font-family="{FONT}">\n'
            f'<title id="{tid}">{escape(self.title)}</title>\n'
            f'<desc id="{did}">{escape(self.desc)}</desc>\n'
            f'<rect x="0" y="0" width="{self.w}" height="{h}" fill="{BG}"/>\n')
        body = "\n".join(self.items)
        with open(path, "w", encoding="utf-8") as f:
            f.write(head + body + "\n</svg>\n")
        return h
