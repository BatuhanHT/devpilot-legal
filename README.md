# devpilot-legal

DevPilot uygulamasının gizlilik politikası ve kullanım koşulları (GitHub Pages ile yayınlanır).

- Kaynak metinler `source/*.md`: uygulamadaki `DevPilot/Resources/Legal/*.md` dosyalarının kopyası.
- `python3 build.py` bunlardan `index.html`, `privacy*.html`, `terms*.html` üretir.
- Politikayı değiştirirsen uygulamadaki `.md` dosyalarını ve buradaki `source/` kopyalarını birlikte güncelle, "Last updated" tarihini yenile, `build.py` çalıştırıp push et.
