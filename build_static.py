"""Render the Flask templates into a site that GitHub Pages can host."""

from pathlib import Path
import posixpath
import shutil

from app import app
from consts import treatments_catalog


ROOT = Path(__file__).parent
OUTPUT = ROOT / "site"

PAGES = {
    "/": "index.html",
    "/about": "about/index.html",
    "/services": "services/index.html",
    "/treatments": "treatments/index.html",
    "/packages": "packages/index.html",
    "/courses": "courses/index.html",
    "/blogs": "blogs/index.html",
    "/review": "review/index.html",
    "/gallery": "gallery/index.html",
    "/contact": "contact/index.html",
    "/thank-you": "thank-you/index.html",
}


def relative_url(page_path: str, target: str) -> str:
    """Return a URL to target relative to the generated page."""
    page_parent = posixpath.dirname(page_path)
    return posixpath.relpath(target, page_parent or ".")


def rewrite_urls(html: str, page_path: str) -> str:
    """Turn Flask's root-relative URLs into GitHub Pages-compatible URLs."""
    static_url = relative_url(page_path, "static/")
    html = html.replace('"/static/', f'"{static_url}').replace(
        "'/static/", f"'{static_url}"
    )

    urls = {}
    for route, output_path in PAGES.items():
        urls[route] = output_path
    for name in treatments_catalog:
        urls[f"/treatments/{name}"] = f"treatments/{name}/index.html"

    for source, target in sorted(urls.items(), key=lambda item: len(item[0]), reverse=True):
        html = html.replace(
            f'"{source}"', f'"{relative_url(page_path, target)}"'
        ).replace(
            f"'{source}'", f"'{relative_url(page_path, target)}'"
        )
    return html


def render_page(client, route: str, output_path: str) -> None:
    response = client.get(route)
    if response.status_code != 200:
        raise RuntimeError(
            f"Could not render {route}: HTTP {response.status_code}"
        )
    html = response.get_data(as_text=True)
    output_path = output_path.replace("\\", "/")
    output_file = OUTPUT / output_path
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(rewrite_urls(html, output_path), encoding="utf-8")


def main() -> None:
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    (OUTPUT / "static").parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(ROOT / "static", OUTPUT / "static")

    with app.test_client() as client:
        for route, output_path in PAGES.items():
            render_page(client, route, output_path)
        for name in treatments_catalog:
            render_page(
                client,
                f"/treatments/{name}",
                f"treatments/{name}/index.html",
            )

    (OUTPUT / ".nojekyll").touch()
    print(f"Generated {sum(1 for _ in OUTPUT.rglob('*.html'))} HTML pages in {OUTPUT}")


if __name__ == "__main__":
    main()
