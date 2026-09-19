# unilogistix.com

Customer site for Unilogistix — a humanless company, makers of CorporateOS.

Built from the 2026-09 brand kit (Ink / Paper / Signal, Archivo + IBM Plex, the U mark). Copy follows the customer presentation in `../CORPORATE_OS.md`.

## Local

```bash
python3 -m http.server 4173 --directory /home/ike/Unilogistix/website
```

Open http://127.0.0.1:4173/

## Ship

Upload the contents of this folder to the existing Vercel project for `unilogistix.com` (apex and www already CNAME there). `index.html` is the site.
