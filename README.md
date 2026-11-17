# Visit Armenia

A static travel site about Armenia: an About Armenia guide (culture, religion, cuisine, money, transport, places, tips), FAQ, and tour pages.

**Live site:** https://khanumyan.github.io/armenian-landing-avangarde-6days/

## Pages
The site is in two languages: **Russian (default)** at the root and **English** in `en/`.
Every page exists in both versions with the same file name; the RU / EN switch in the header links them.
When you change a page, update both versions.

- `index.html` — splash screen, “Barev dzez”, About Armenia, FAQ
- `tours.html` — the tour card, what’s included, tour FAQ
- `tour-yerevan-garni-sevan-myler.html` — the single 6-day / 4-night tour with the day-by-day itinerary
- `en/…` — the same pages in English (images and styles are referenced as `../img/`, `../style.css`)
- `style.css` — shared styles, `img/` — photos

## Run locally
```
python3 serve.py
```
Then open http://127.0.0.1:8767/

Photos: mostly from Wikimedia Commons; authors and licenses are listed in `img/credits.json`.
