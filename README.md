# Ministry of Education × Flam — pitch deck

An interactive, 14-slide presentation for the Ministry of Education, Government of India.

## Present it

Open `index.html` in Chrome on the presenting laptop.

- **← / →** (or Space) move between slides, **F** toggles full screen, **Esc** closes a live demo.
- Tabbed slides advance on their own; a tap holds the chosen tab for 12 seconds.
- The kiosk journey, voice helpline and Flicks demo open inside the deck. They need an internet connection, and each has an "open in a new tab" fallback.

`index.html` is self-contained: every image, video and logo is embedded. Fonts load from Google Fonts.

## Edit it

| Path | What it holds |
| --- | --- |
| `src/template.html` | Slide markup, styles and behaviour, with `{{IMG_…}}`, `{{VID_…}}` and `{{URL_…}}` placeholders |
| `src/build.py` | Inlines the assets and writes `index.html` |
| `assets/images/` | Slide visuals (generated in Flowy, watermark strip cropped) |
| `assets/video/` | Flicks clips for the city, small-town and village settings |
| `assets/logos/` | Flam and Ministry of Education logos |

After editing, rebuild:

```bash
python3 src/build.py
```

### Airboards recording and QR

The Airboards slide has a phone placeholder for the experience recording and a card for the experience QR. To fill them, set `airboardVideo` and `airboardQR` in the `CONFIG` object near the top of the script in `src/template.html`, then rebuild.

## Slides

1. Cover
2. The Ministry's priorities
3. The scale
4. Where Flam fits
5. Voice Agent
6. Visual Agent
7. Kiosk journey (live)
8. Airboards
9. Flicks for government
10. Flicks (live)
11. On the Ministry's schemes
12. The first step: Kashi Tamil Sangamam 5.0
13. The path
14. Thank you
