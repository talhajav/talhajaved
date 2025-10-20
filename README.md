# Personal Website

A personal website built with Flask and Frozen-Flask, optimized for Markdown-authored content and static deployment.

## Features

- **Modern Black & White Design**: Beautiful, minimalist aesthetic with smooth animations
- **Static Site Generation**: Built with Flask, exported to static HTML via Frozen-Flask
- **Markdown Content**: Write pages and blog posts in Markdown with YAML frontmatter
- **Dynamic Navigation**: Navigation automatically generated from content files
- **Simple Structure**: Easy to add new pages - just create a new `.md` file
- **Responsive Design**: Clean, mobile-friendly layout with three breakpoints
- **CI/CD Ready**: GitHub Actions workflow included for automated deployment
- **Low Maintenance**: Deploy to any static host (GitHub Pages, Netlify, Vercel, etc.)

## Project Structure

```
.
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── content/               # All content in Markdown
│   ├── pages/            # Static pages (About, Projects, etc.)
│   │   ├── home.md
│   │   ├── about.md
│   │   └── projects.md
│   └── blog/             # Blog posts
│       ├── welcome-to-my-blog.md
│       └── building-with-flask.md
├── templates/            # Jinja2 templates
│   ├── base.html        # Base template with navigation
│   ├── page.html        # Template for static pages
│   ├── blog.html        # Blog listing page
│   └── post.html        # Individual blog post template
├── build/               # Generated static site (created on build)
└── .github/
    └── workflows/
        └── deploy.yml   # GitHub Actions CI/CD workflow
```

## Quick Start

### 1. Install Dependencies

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Run Development Server

```bash
python app.py
```

Visit [http://localhost:5000](http://localhost:5000) to see your site.

### 3. Build Static Site

```bash
python app.py build
```

The static site will be generated in the `build/` directory.

## Adding Content

### Creating a New Page

1. Create a new Markdown file in `content/pages/`:

```markdown
---
title: My New Page
nav_title: New Page    # Optional - shown in navigation (defaults to title)
nav_order: 15         # Optional - controls navigation order (lower = earlier)
---

# My New Page

Your content here...
```

2. The page will **automatically** be available at `/your-filename/`
3. The page will **automatically** appear in the navigation (no manual editing needed!)
4. Use `nav_order` to control where it appears (Home is 0, About is 10, Projects is 20, Blog is 1000)

### Creating a Blog Post

1. Create a new Markdown file in `content/blog/`:

```markdown
---
title: My Blog Post Title
date: 2025-01-20
excerpt: A short description of the post.
---

# My Blog Post Title

Your post content here...
```

2. The post will automatically appear in the blog listing at `/blog/`
3. Individual posts are available at `/blog/your-filename/`

### Frontmatter Fields

**For Pages:**
- `title` (required): Page title
- `nav_title` (optional): Title shown in navigation (defaults to `title`)
- `nav_order` (optional): Number for ordering navigation items (lower = earlier)

**For Blog Posts:**
- `title` (required): Post title
- `date` (required): Publication date in YYYY-MM-DD format
- `excerpt` (optional): Short description shown in blog listing

## Deployment

### GitHub Pages

1. Push your code to GitHub
2. Go to repository Settings > Pages
3. Set source to "GitHub Actions"
4. The included workflow will automatically build and deploy on push to `main`

**Custom Domain**: Edit `.github/workflows/deploy.yml` and update the `cname` field, or remove it to use GitHub's default domain.

### Netlify

1. Connect your GitHub repository to Netlify
2. Set build command: `python app.py build`
3. Set publish directory: `build`
4. Deploy!

### Vercel

1. Connect your GitHub repository to Vercel
2. Set build command: `pip install -r requirements.txt && python app.py build`
3. Set output directory: `build`
4. Deploy!

### Other Hosts

Simply upload the contents of the `build/` directory to any static hosting service.

## Customization

### Styling

Edit the `<style>` section in [templates/base.html](templates/base.html) to customize the appearance. CSS custom properties are defined in `:root` for easy theming:

```css
:root {
    --bg-primary: #ffffff;
    --bg-secondary: #000000;
    --text-primary: #000000;
    --text-secondary: #666666;
    /* ... and more */
}
```

### Navigation

**Navigation is now fully dynamic!** It's automatically generated from your content files. No need to edit templates manually. Just add a new `.md` file with `nav_order` in the frontmatter, and it will appear in the navigation.

### Templates

- **base.html**: Main layout, navigation, and styling
- **page.html**: Template for static pages
- **blog.html**: Blog listing page
- **post.html**: Individual blog post layout

### Configuration

Edit [app.py](app.py) to:
- Change the build output directory (default: `build/`)
- Add custom Markdown extensions
- Modify URL structure
- Add new routes

## Development

### Running Tests Locally

Before building:

```bash
python app.py
```

Visit [http://localhost:5000](http://localhost:5000) and check:
- All pages load correctly
- Navigation works
- Blog posts display properly
- Styling looks good

### Building for Production

```bash
python app.py build
```

Test the built site:

```bash
cd build
python -m http.server 8000
```

Visit [http://localhost:8000](http://localhost:8000) to verify the static site works correctly.

## Markdown Features

The site supports:
- **Headings**: `# H1`, `## H2`, etc.
- **Bold**: `**bold**`
- **Italic**: `*italic*`
- **Links**: `[text](url)`
- **Images**: `![alt](url)`
- **Lists**: Unordered and ordered
- **Code blocks**: Fenced with ` ```language `
- **Inline code**: `` `code` ``
- **Tables**: Standard Markdown tables
- **Table of contents**: Automatically generated from headings

## Troubleshooting

### Pages not generating

- Ensure Markdown files have proper frontmatter with `title` field
- Check file permissions
- Verify files are in correct directories (`content/pages/` or `content/blog/`)

### Blog posts not appearing

- Ensure posts have both `title` and `date` in frontmatter
- Verify date format is `YYYY-MM-DD`
- Check that files are in `content/blog/` directory

### Build fails

- Check Python version (3.8+ required)
- Verify all dependencies are installed: `pip install -r requirements.txt`
- Look for syntax errors in Markdown files

## License

MIT License - feel free to use this for your own personal website!

## Credits

Built with:
- [Flask](https://flask.palletsprojects.com/) - Web framework
- [Frozen-Flask](https://pythonhosted.org/Frozen-Flask/) - Static site generator
- [Python-Markdown](https://python-markdown.github.io/) - Markdown processor
- [Python-Frontmatter](https://python-frontmatter.readthedocs.io/) - YAML frontmatter parser
