#!/bin/bash

# Helper script for common tasks

case "$1" in
    dev|serve)
        echo "Starting development server..."
        uv run python app.py
        ;;
    build)
        echo "Building static site..."
        uv run python app.py build
        echo "Build complete! Files are in build/"
        ;;
    test)
        echo "Running test suite..."
        uv run pytest
        ;;
    preview)
        echo "Serving built site locally..."
        cd build && uv run python -m http.server 8000
        ;;
    install|sync)
        echo "Syncing environment with uv..."
        uv sync
        echo "Installation complete!"
        ;;
    *)
        echo "Usage: ./run.sh [command]"
        echo ""
        echo "Commands:"
        echo "  install    - Create .venv and install dependencies (uv sync)"
        echo "  dev        - Run development server (port 7060)"
        echo "  build      - Build static site to build/"
        echo "  test       - Run the pytest suite"
        echo "  preview    - Serve the built site locally (port 8000)"
        echo ""
        echo "Examples:"
        echo "  ./run.sh install"
        echo "  ./run.sh dev"
        echo "  ./run.sh test"
        ;;
esac
