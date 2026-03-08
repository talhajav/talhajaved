#!/bin/bash

# Helper script for common tasks

case "$1" in
    dev|serve)
        echo "Starting development server..."
        source venv/bin/activate && python app.py
        ;;
    build)
        echo "Building static site..."
        source venv/bin/activate && python app.py build
        echo "Build complete! Files are in build/"
        ;;
    test)
        echo "Testing built site locally..."
        cd build && python -m http.server 8000
        ;;
    install)
        echo "Creating virtual environment and installing dependencies..."
        python3 -m venv venv
        source venv/bin/activate && pip install -r requirements.txt
        echo "Installation complete!"
        ;;
    *)
        echo "Usage: ./run.sh [command]"
        echo ""
        echo "Commands:"
        echo "  install    - Set up virtual environment and install dependencies"
        echo "  dev        - Run development server"
        echo "  build      - Build static site"
        echo "  test       - Test built site locally (port 8000)"
        echo ""
        echo "Examples:"
        echo "  ./run.sh install"
        echo "  ./run.sh dev"
        echo "  ./run.sh build"
        ;;
esac
