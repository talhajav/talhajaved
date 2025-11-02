from flask import Flask, render_template, abort
from flask_frozen import Freezer
import markdown
import frontmatter
from pathlib import Path
from datetime import datetime

app = Flask(__name__)
app.config['FREEZER_DESTINATION'] = 'build'
app.config['FREEZER_RELATIVE_URLS'] = False
app.config['FREEZER_BASE_URL'] = 'https://talhajav.github.io/talhajaved/'

freezer = Freezer(app)

# GitHub Pages base path (configured for talhajav.github.io/talhajaved)
BASE_PATH = '/talhajaved'


def url_for_with_base(endpoint, **values):
    """Generate URL with base path prepended."""
    from flask import url_for as flask_url_for
    url = flask_url_for(endpoint, **values)
    # Prepend base path if not already present
    if not url.startswith(BASE_PATH) and not url.startswith('http'):
        url = BASE_PATH + url
    return url


# Override url_for in Jinja2 environment
app.jinja_env.globals['url_for'] = url_for_with_base

# Markdown extensions for better rendering
MD = markdown.Markdown(extensions=['fenced_code', 'codehilite', 'tables', 'toc'])


@app.context_processor
def inject_current_year():
    """Make current year available in templates."""
    return {'current_year': lambda: datetime.now().year}


@app.context_processor
def inject_navigation():
    """Dynamically generate navigation from available pages."""
    nav_items = [{'route': 'index', 'title': 'Home', 'order': 10}]  # Home gets order 10

    pages_dir = Path('content') / 'pages'
    if pages_dir.exists():
        for page_file in sorted(pages_dir.glob('*.md')):
            if page_file.stem != 'home':
                post = frontmatter.load(page_file)
                nav_order = post.get('nav_order', 999)
                nav_items.append({
                    'route': 'page',
                    'params': {'page_name': page_file.stem},
                    'title': post.get('nav_title', post.get('title', page_file.stem.title())),
                    'order': nav_order
                })

    # Add projects and blog to navigation
    nav_items.append({'route': 'projects', 'title': 'Projects', 'order': 30})
    nav_items.append({'route': 'blog', 'title': 'Blog', 'order': 1000})

    # Sort by order
    nav_items.sort(key=lambda x: x.get('order', 999))

    return {'navigation': nav_items}


def load_page(page_name):
    """Load a page from content directory."""
    page_path = Path('content') / 'pages' / f'{page_name}.md'
    if not page_path.exists():
        return None

    post = frontmatter.load(page_path)
    content_html = MD.convert(post.content)
    MD.reset()  # Reset for next conversion

    return {
        'title': post.get('title', page_name.title()),
        'content': content_html,
        'metadata': post.metadata
    }


def load_blog_posts():
    """Load all blog posts sorted by date."""
    posts = []
    blog_dir = Path('content') / 'blog'

    if not blog_dir.exists():
        return posts

    for post_file in blog_dir.glob('*.md'):
        post = frontmatter.load(post_file)

        # Parse date
        date = post.get('date')
        if isinstance(date, str):
            date = datetime.strptime(date, '%Y-%m-%d')

        posts.append({
            'slug': post_file.stem,
            'title': post.get('title', post_file.stem.replace('-', ' ').title()),
            'date': date,
            'excerpt': post.get('excerpt', ''),
            'content': MD.convert(post.content),
            'metadata': post.metadata
        })
        MD.reset()

    # Sort by date, newest first
    posts.sort(key=lambda x: x['date'], reverse=True)
    return posts


def load_projects():
    """Load all projects sorted by order."""
    projects = []
    projects_dir = Path('content') / 'projects'

    if not projects_dir.exists():
        return projects

    for project_file in projects_dir.glob('*.md'):
        project = frontmatter.load(project_file)

        # Parse date
        date = project.get('date')
        if isinstance(date, str):
            date = datetime.strptime(date, '%Y-%m-%d')

        projects.append({
            'slug': project_file.stem,
            'title': project.get('title', project_file.stem.replace('-', ' ').title()),
            'date': date,
            'technologies': project.get('technologies', ''),
            'excerpt': project.get('excerpt', ''),
            'content': MD.convert(project.content),
            'metadata': project.metadata,
            'order': project.get('order', 999)
        })
        MD.reset()

    # Sort by order, then by date
    projects.sort(key=lambda x: (x['order'], x['date']), reverse=False)
    return projects


@app.route('/')
def index():
    """Homepage."""
    page = load_page('home')
    if not page:
        page = {
            'title': 'Welcome',
            'content': '<p>Welcome to my personal website.</p>',
            'metadata': {}
        }
    return render_template('page.html', page=page)


@app.route('/<page_name>/')
def page(page_name):
    """Generic page route."""
    page = load_page(page_name)
    if not page:
        abort(404)
    return render_template('page.html', page=page)


@app.route('/projects/')
def projects():
    """Projects listing page."""
    project_list = load_projects()
    return render_template('projects.html', projects=project_list)


@app.route('/projects/<slug>/')
def project(slug):
    """Individual project page."""
    project_path = Path('content') / 'projects' / f'{slug}.md'
    if not project_path.exists():
        abort(404)

    proj = frontmatter.load(project_path)
    date = proj.get('date')
    if isinstance(date, str):
        date = datetime.strptime(date, '%Y-%m-%d')

    content_html = MD.convert(proj.content)
    MD.reset()

    project_data = {
        'slug': slug,
        'title': proj.get('title', slug.replace('-', ' ').title()),
        'date': date,
        'technologies': proj.get('technologies', ''),
        'content': content_html,
        'metadata': proj.metadata
    }

    return render_template('project.html', project=project_data)


@app.route('/blog/')
def blog():
    """Blog listing page."""
    posts = load_blog_posts()
    return render_template('blog.html', posts=posts)


@app.route('/blog/<slug>/')
def blog_post(slug):
    """Individual blog post."""
    post_path = Path('content') / 'blog' / f'{slug}.md'
    if not post_path.exists():
        abort(404)

    post = frontmatter.load(post_path)
    date = post.get('date')
    if isinstance(date, str):
        date = datetime.strptime(date, '%Y-%m-%d')

    content_html = MD.convert(post.content)
    MD.reset()

    post_data = {
        'slug': slug,
        'title': post.get('title', slug.replace('-', ' ').title()),
        'date': date,
        'content': content_html,
        'metadata': post.metadata
    }

    return render_template('post.html', post=post_data)


@freezer.register_generator
def page_generator():
    """Generate URLs for all pages."""
    pages_dir = Path('content') / 'pages'
    if pages_dir.exists():
        for page_file in pages_dir.glob('*.md'):
            if page_file.stem not in ['home', 'projects']:  # Home is handled by index route, projects by projects route
                yield 'page', {'page_name': page_file.stem}


@freezer.register_generator
def project_generator():
    """Generate URLs for all projects."""
    projects_dir = Path('content') / 'projects'
    if projects_dir.exists():
        for project_file in projects_dir.glob('*.md'):
            yield 'project', {'slug': project_file.stem}


@freezer.register_generator
def blog_post_generator():
    """Generate URLs for all blog posts."""
    blog_dir = Path('content') / 'blog'
    if blog_dir.exists():
        for post_file in blog_dir.glob('*.md'):
            yield 'blog_post', {'slug': post_file.stem}


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == 'build':
        # Build static site
        freezer.freeze()
        print(f"Site built successfully in {app.config['FREEZER_DESTINATION']}/")
    else:
        # Run development server
        app.run(debug=True, port=7060)
