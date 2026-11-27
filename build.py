#!/usr/bin/env python3
"""source/*.md dosyalarından düz HTML sayfaları üretir (Jekyll gerekmez).

Kullanım: uygulamadaki DevPilot/Resources/Legal/*.md dosyalarını source/ içine kopyala,
sonra `python3 build.py` çalıştır ve değişiklikleri push et.
"""
import html
import pathlib

ROOT = pathlib.Path(__file__).parent
SOURCE = ROOT / "source"

# kaynak dosya -> (çıktı dosyası, dil, diğer dildeki karşılığı, bağlantı etiketleri)
PAGES = {
    "privacy.en.md": ("privacy.html", "en", "privacy.tr.html", "Türkçe"),
    "privacy.tr.md": ("privacy.tr.html", "tr", "privacy.html", "English"),
    "terms.en.md": ("terms.html", "en", "terms.tr.html", "Türkçe"),
    "terms.tr.md": ("terms.tr.html", "tr", "terms.html", "English"),
    "support.en.md": ("support.html", "en", "support.tr.html", "Türkçe"),
    "support.tr.md": ("support.tr.html", "tr", "support.html", "English"),
}

# Destek sayfalarının altına eklenen iletişim bölümü.
# Destek e-postası; boş bırakılırsa yalnızca GitHub Issues gösterilir.
SUPPORT_EMAIL = "btemelbusiness@outlook.com"
ISSUES_URL = "https://github.com/BatuhanHT/devpilot-legal/issues"
CONTACT = {
    "en": ("Contact", "Email", "Open an issue on GitHub", "Issues are public. Do not post passwords, tokens or private data."),
    "tr": ("İletişim", "E-posta", "GitHub'da bir konu açın", "Konular herkese açıktır. Parola, token veya özel veri paylaşmayın."),
}


def contact_block(lang: str) -> str:
    heading, email_label, issues_label, warning = CONTACT[lang]
    lines = []
    if SUPPORT_EMAIL:
        mail = html.escape(SUPPORT_EMAIL)
        lines.append(f'<li>{email_label}: <a href="mailto:{mail}">{mail}</a></li>')
    lines.append(f'<li><a href="{ISSUES_URL}">{issues_label}</a></li>')
    return f"<h2>{heading}</h2>\n<ul>{''.join(lines)}</ul>\n<p>{html.escape(warning)}</p>"
HOME_LABEL = {"en": "Home", "tr": "Ana sayfa"}

CSS = """
:root{color-scheme:light dark;--bg:#fff;--fg:#0f172a;--muted:#475569;--accent:#0369a1;--border:#e2e8f0}
@media(prefers-color-scheme:dark){:root{--bg:#080b10;--fg:#f8fafc;--muted:#94a3b8;--accent:#38bdf8;--border:#334155}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:17px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}
main{max-width:720px;margin:0 auto;padding:32px 20px 64px}
nav{display:flex;justify-content:space-between;gap:12px;font-size:15px;margin-bottom:28px;padding-bottom:14px;border-bottom:1px solid var(--border)}
a{color:var(--accent)}
h1{font-size:2rem;line-height:1.2;margin:0 0 .5rem}
h2{font-size:1.2rem;margin:2rem 0 .4rem}
p,li{color:var(--muted)}
li{margin:.35rem 0}
ul{padding-left:1.2rem}
.cards{display:grid;gap:12px;margin-top:24px}
.card{display:block;padding:16px 18px;border:1px solid var(--border);border-radius:12px;text-decoration:none;color:var(--fg)}
.card span{display:block;color:var(--muted);font-size:15px}
"""


def page(lang: str, title: str, nav: str, body: str) -> str:
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<style>{CSS}</style>
</head>
<body>
<main>
{nav}
{body}
</main>
</body>
</html>
"""


def render(markdown: str) -> tuple[str, str]:
    """(ilk başlık, gövde HTML). Uygulamadaki LegalDocumentView ile aynı alt küme: #, ##, '- ' maddeleri, paragraf."""
    title, out = "", []
    for chunk in markdown.strip().split("\n\n"):
        text = chunk.strip()
        if not text:
            continue
        if text.startswith("# "):
            title = text[2:]
            out.append(f"<h1>{html.escape(title)}</h1>")
        elif text.startswith("## "):
            out.append(f"<h2>{html.escape(text[3:])}</h2>")
        elif text.startswith("- "):
            items = "".join(f"<li>{html.escape(line[2:].strip())}</li>" for line in text.splitlines())
            out.append(f"<ul>{items}</ul>")
        else:
            out.append(f"<p>{html.escape(text)}</p>")
    return title, "\n".join(out)


def main() -> None:
    for source, (target, lang, other, other_label) in PAGES.items():
        title, body = render((SOURCE / source).read_text(encoding="utf-8"))
        if source.startswith("support."):
            body += "\n" + contact_block(lang)
        nav = f'<nav><a href="./">{HOME_LABEL[lang]}</a><a href="{other}" hreflang="{"tr" if lang == "en" else "en"}">{other_label}</a></nav>'
        (ROOT / target).write_text(page(lang, title, nav, body), encoding="utf-8")

    index = """<h1>DevPilot</h1>
<p>AI-native engineering cockpit for iOS.</p>
<div class="cards">
<a class="card" href="https://apps.apple.com/app/id6837625215">Download on the App Store<span>iPhone, free</span></a>
<a class="card" href="indir.html">DevPilot’u indir<span>Türkçe</span></a>
<a class="card" href="privacy.html">Privacy Policy<span>English</span></a>
<a class="card" href="terms.html">Terms of Use<span>English</span></a>
<a class="card" href="support.html">Support<span>English</span></a>
<a class="card" href="privacy.tr.html">Gizlilik Politikası<span>Türkçe</span></a>
<a class="card" href="terms.tr.html">Kullanım Koşulları<span>Türkçe</span></a>
<a class="card" href="support.tr.html">Destek<span>Türkçe</span></a>
</div>"""
    (ROOT / "index.html").write_text(page("en", "DevPilot", "", index), encoding="utf-8")
    print("Üretildi:", ", ".join(sorted(p.name for p in ROOT.glob("*.html"))))


if __name__ == "__main__":
    main()
