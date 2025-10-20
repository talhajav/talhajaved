---
title: Personal Website
date: 2025-01-15
technologies: Python, Flask, Frozen-Flask
excerpt: A static website generator built with Flask and exported to static HTML for fast, low-maintenance hosting.
order: 1
---

The site you're currently viewing! A static website generator built with Flask and exported to static HTML for fast, low-maintenance hosting.

## Technologies

- **Python** - Core programming language
- **Flask** - Web framework for development
- **Frozen-Flask** - Static site generation
- **Markdown** - Content authoring
- **GitHub Actions** - CI/CD pipeline

## Features

- **Markdown-based content authoring** - Write content in simple Markdown files
- **Static site generation** - Fast, secure, and easy to host
- **Clean, responsive design** - Beautiful black and white aesthetic
- **CI/CD deployment** - Automatic deployment with GitHub Actions
- **Dynamic navigation** - Automatically generated from content files

## Architecture

The site uses Flask during development for easy testing and preview, then Frozen-Flask crawls all routes and generates static HTML files. This gives you the best of both worlds: a pleasant development experience and a lightning-fast production site.

## Deployment

The site is deployed automatically via GitHub Actions whenever changes are pushed to the main branch. The static files can be hosted on any platform - GitHub Pages, Netlify, Vercel, or any web server.

## Future Enhancements

- Dark mode toggle
- Search functionality
- RSS feed for blog posts
- Project tagging and filtering
