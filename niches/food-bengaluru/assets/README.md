# Brand assets — Smart Pursuit logo

Put the **real Smart Pursuit logo** in this folder and every audit picks it up automatically
(cover + header of every page + the workbook README sheet). Until a file is here, the reports
render the drawn "SP" mark, so nothing ever breaks.

## Where to upload — pick any one

| Route | What to do |
|---|---|
| **1. Attach it in the Arena chat (easiest)** | Just attach the image file in the chat. It gets saved into this folder for you and the whole pack is regenerated. |
| **2. GitHub web upload** | Open this folder on the PR branch — https://github.com/vamsy16/arena-performance-marketing/tree/arena/01a0ffb0-arena-performance-marketing/niches/food-bengaluru/assets — click **Add file → Upload files**, drag the image in, name it exactly `smart-pursuit-logo.png`, commit to the same branch, then tell me and I regenerate. |
| **3. Google Drive / WhatsApp / email** | Send the file and a link or attachment; it comes back into this folder and the pack is rebuilt. |

## File requirements

- **Name:** `smart-pursuit-logo.png` (exact). `.jpg` / `.jpeg` also work with the same base name.
- **Format:** PNG preferred — with a **transparent background** if the logo sits on the navy cover.
  A JPG with a solid background will show a white or coloured box in the header, so PNG + transparency
  is the one to send if you have it.
- **Size:** at least **600 px wide** (ideally 1000–2000 px). Higher resolution just looks sharper;
  it is scaled down automatically and the aspect ratio is always preserved.
- **Lockup vs mark:** if your logo file already contains the words "SMART PURSUIT" (like the current
  circular badge), create a one-line sidecar file next to it — `assets/smart-pursuit-logo.mode.txt`
  containing `lockup` — so the reports never print the name twice. If the file is only a symbol
  (no words), use `mark` or simply leave the sidecar out for a wide file (aspect ≥ 2.0).
- **Two kinds of file both work:**
  - **Square / stacked mark** → shown at 12 mm on the cover, 6 mm in the page headers, with the
    words "SMART PURSUIT" set in type beside it (current layout).
  - **Wide lockup** (logo + wordmark in one file, aspect ≥ 2.0) → placed on its own at up to 46 mm,
    and the duplicate "SMART PURSUIT" text is dropped automatically.
- If you only have **SVG / PDF / AI**, export a PNG at 2× size and send that — the report engine
  embeds raster formats only.

## What happens after upload

1. `python3 scripts/build_evidence_audits.py` — rebuilds the 11 original audits
2. `python3 scripts/build_batch2.py` — rebuilds the 10 newer audits
3. `python3 scripts/build_master_excel.py` — rebuilds the workbook (logo on the README sheet)

All 21 PDFs are then re-checked page by page (logo present on **every** page, correct footer,
no layout overflow) before anything is called done.
