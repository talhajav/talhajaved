# Adding New Blog Posts

## Step 1: Create the Markdown file

Create a new `.md` file in `content/blog/`. The filename becomes the URL slug — use lowercase with hyphens.

```
content/blog/my-new-post.md
```

## Step 2: Add the frontmatter

Every post requires a YAML frontmatter block at the top with three fields:

```markdown
---
title: My New Post
date: 2026-02-28
excerpt: A short one-sentence description shown on the blog listing page.
---

Your post content goes here...
```

- `title` — displayed as the page heading and in the blog list
- `date` — format must be `YYYY-MM-DD`; posts are sorted by this
- `excerpt` — shown as the preview blurb on the `/blog` page

## Step 3: Write your content

Below the frontmatter `---`, write standard Markdown. All common syntax is supported:

```markdown
## Heading

Regular paragraph text.

- bullet list
- another item

**bold**, _italic_, `inline code`

\```python
# fenced code blocks work too
def hello():
    print("hello")
\```

[link text](https://example.com)
```

## Step 4: Preview locally (optional)

```bash
python app.py
```

Open `http://localhost:7060/talhajaved/blog/my-new-post/` to check it looks right before publishing.

## Step 5: Deploy

```bash
git add content/blog/my-new-post.md
git commit -m "add post: my new post title"
git push origin main
```

Pushing to `main` automatically triggers the GitHub Actions workflow which:

1. Installs dependencies
2. Runs `python app.py build` to generate static HTML into `build/`
3. Pushes the `build/` directory to the `gh-pages` branch
4. GitHub Pages serves it from there

The live site at `https://talhajav.github.io/talhajaved/` updates within ~1-2 minutes. You can watch progress under the **Actions** tab in your GitHub repo.

---

## Frontmatter field reference

| Field | Where it appears |
|---|---|
| `title` | Page heading, blog list, browser tab |
| `date` | Shown on the post, used for sorting |
| `excerpt` | Blog listing page preview text |
