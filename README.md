# RoomMuse — Virtual Gallery Showroom

A browser-based virtual gallery that lets you upload a room photo, calibrate real-world scale, and place artworks (stock or your own) at accurate cm dimensions on the wall. Multiple pieces can be placed simultaneously and dragged into position.

## Quick Start

**Requirements:** Python 3 (any version — no packages needed).

```bash

# Launch
python serve.py
```

Your browser opens automatically to `http://localhost:8000`.

To use a different port:

```bash
python serve.py 3000
```

Press `Ctrl+C` in the terminal to stop the server.

### Alternative: no script

If you prefer a one-liner without the helper script:

```bash
cd roommuse-gallery
python -m http.server 8000
# then open http://localhost:8000 in your browser
```

Or if you only have Python 2:

```bash
python -m SimpleHTTPServer 8000
```

Or with Node.js:

```bash
npx serve .
```

## How to Use

1. **Upload a room photo** — drag-and-drop or click the upload zone.
2. **Define the wall** — drag the 4 teal corner handles to match the wall edges.
3. **Calibrate scale** — click "Calibrate scale", drag the two orange handles onto a known object (e.g. a door), enter its real height in cm, and confirm. The wall overlay disappears.
4. **Browse & filter** — use the sidebar filters (Style, Tone, Size, Price) to narrow the stock gallery.
5. **Place artwork** — click any card in the sidebar to place it on the wall at accurate real-world scale. You can place as many as you want.
6. **Drag to reposition** — grab any placed piece and drag it anywhere on the photo.
7. **View details** — click (don't drag) a placed piece to open the info panel with exact dimensions and price.
8. **Upload your own artwork** — click "+ Upload your own" at the top of the sidebar. Select one or many image files, set their real-world width/height in cm, and confirm. If "Place on wall immediately" is checked, they all appear on the wall spread out and ready to drag.
9. **Remove / Clear** — use the info panel buttons to remove a single piece or clear all.

## Project Structure

```
roommuse-gallery/
├── index.html   — Complete app (single file, no build step)
├── serve.py     — Python dev server with auto-open
└── README.md    — This file
```

## Tech

Zero dependencies. Pure HTML + CSS + vanilla JS. No build tools, no npm, no frameworks. Works in any modern browser (Chrome, Firefox, Safari, Edge).

The cm-to-pixel math follows the formula from the RoomMuse spec:

```
pxPerMetre = calibrationPixelSpan / (knownHeightCm / 100)
artWidthPx = (artWidthCm / 100) * pxPerMetre
```

Eye-level default is 57% from the top of the wall rectangle.
