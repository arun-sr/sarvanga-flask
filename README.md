# Sarvanga Flask website

## Free deployment using GitHub Pages

GitHub Pages cannot run a Flask server, so this repository generates the Flask
templates into static HTML before publishing them. The original Flask app is
still available for local development.

1. Push this repository to GitHub, using the `main` branch.
2. In GitHub, open **Settings > Pages**.
3. Under **Build and deployment > Source**, select **GitHub Actions**.
4. Push a change or run **Deploy static site to GitHub Pages** from the
   **Actions** tab.

The workflow in `.github/workflows/pages.yml` runs `build_static.py`, copies
the assets, and deploys the generated `site/` folder. Every push to `main`
will trigger a new deployment. The generated site has no server-side form
processing; the current contact page uses phone, WhatsApp, email, and map
links.

### Custom domain

After the first deployment, open **Settings > Pages > Custom domain** in
GitHub and follow the DNS instructions for `www.sarvanga.co.in`. For a custom
domain, add a `CNAME` file containing `www.sarvanga.co.in` to the `site/`
folder in `build_static.py` before deploying.

### Local preview

Install the dependencies and generate the static files:

```text
pip install -r requirements.txt
python build_static.py
```

Open `site/index.html` in a browser, or serve it locally with:

```text
python -m http.server 8000 --directory site
```
