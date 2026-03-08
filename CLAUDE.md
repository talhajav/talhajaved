# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A personal website (talhajav.github.io/talhajaved) built with Flask + Frozen-Flask. During development it runs as a live Flask server; for deployment it freezes to static HTML in `build/` and is served via GitHub Pages.

## Commands

```bash
# Development server (port 7060)
python app.py

# Build static site to build/
python app.py build

# Preview built site
cd build && python -m http.server 8000
```

The `run.sh` script wraps these as `./run.sh dev`, `./run.sh build`, `./run.sh test`.

## Architecture

**`app.py`** is the entire backend. It:
- Defines Flask routes for `/`, `/<page_name>/`, `/projects/`, `/projects/<slug>/`, `/blog/`, `/blog/<slug>/`
- Reads content from `content/` using `python-frontmatter` to parse YAML frontmatter + Markdown body
- Converts Markdown to HTML with `python-markdown` (extensions: fenced_code, codehilite, tables, toc)
- Registers Frozen-Flask URL generators so all content pages are included in the static build
- Overrides Jinja2's `url_for` to prepend `/talhajaved` (the GitHub Pages subpath) to all URLs

**Content** lives in `content/` as Markdown files with YAML frontmatter:
- `content/pages/*.md` — static pages; `home.md` → `/`, others → `/<stem>/`
- `content/blog/*.md` — blog posts → `/blog/<stem>/`; sorted by `date` field
- `content/projects/*.md` — projects → `/projects/<stem>/`; sorted by `order` then `date` field

**Navigation** is dynamically generated at request time from `content/pages/*.md` frontmatter (`nav_order`, `nav_title`) plus hardcoded entries for Projects (order 30) and Blog (order 1000).

**Templates** (`templates/`) are Jinja2 HTML. `base.html` is the shared layout; `page.html`, `blog.html`, `post.html`, `projects.html`, `project.html` extend it. All CSS is in `static/style.css` — theme colors are CSS custom properties in `:root` at the top of that file.

**Deployment**: Push to `main` triggers `.github/workflows/deploy.yml` which runs `python app.py build` and pushes `build/` to the `gh-pages` branch.

## Content frontmatter

Pages (`content/pages/`):
- `title` (required), `nav_title` (optional), `nav_order` (optional, integer)

Blog posts (`content/blog/`):
- `title` (required), `date` (required, `YYYY-MM-DD`), `excerpt` (optional)

Projects (`content/projects/`):
- `title`, `date`, `technologies`, `excerpt`, `order` (integer, lower = shown first)
