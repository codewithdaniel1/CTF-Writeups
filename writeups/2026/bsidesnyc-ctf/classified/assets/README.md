# Classified challenge assets

CipherWiki was captured from https://ctf313.com/cipher-wiki/index.html on October 18, 2026. The exact UTC capture time, source URLs, file sizes, and hashes are recorded in `original/cipher-wiki-manifest.json`.

## Local archive

Open `original/cipher-wiki/index.html` to browse the saved challenge website. It contains 53 HTML pages, including the article and talk-page navigation, the OC-7 memo, both wiki stylesheets, images, audio, and local font files. The archive is approximately 255 MiB, mostly original audio. Binary assets are unchanged.

The solve path is:

1. `original/cipher-wiki/index.html`
2. `original/cipher-wiki/films/f02.html`
3. `original/cipher-wiki/talk/f02.html`
4. `original/cipher-wiki/classified/oc7.html`

The `.docref` hex clue remains unchanged. Its decoded `/classified/oc7.html` path is relative to the challenge website's root; the actual source document was served at `https://ctf313.com/cipher-wiki/classified/oc7.html`.

## Source preservation

`original/cipher-wiki-source.zip` contains the byte-for-byte HTML and CSS responses captured from the original website and its font provider before localizing links. Unmodified media and fonts are stored alongside the browsable pages; their source hashes appear in the manifest. The original site's attribution and license notices remain in the saved pages. Font licenses and their source URLs are in `original/cipher-wiki/_fonts/licenses/`.

Only navigation and dependency URLs were changed in the browsable archive. Google Fonts CSS and font files are local. Links to five Wikipedia reference articles remain external. No page text, hidden flags, encoded clues, or inline presentation styles were changed. The original search, account, edit, and history controls remain placeholders, as on the source site.

The original `talk/index.html` had 24 article links that returned 404 because they omitted `../`. Those links, its three misdirected homepage links, and two broken production-page links on `talk/talk_production.html` now point to the matching archived articles. Each URL change is recorded in the manifest. The archive does not invent content for missing pages.

The earlier standalone talk page, memo, and stylesheet have been consolidated into this site-shaped archive. The recovered flag remains in `recovered/flag.txt`.
