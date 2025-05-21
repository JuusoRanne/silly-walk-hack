#!/bin/bash
# Setup and run script for the Silly Walk Grant Application Orchestrator

# Function to install dependencies
install_dependencies() {
    echo "Installing dependencies..."
    pip install -r requirements.txt
    echo "Dependencies installed successfully!"
}

# Function to run tests
run_tests() {
    echo "Running tests..."
    python -m pytest
    echo "Tests completed!"
}

# Function to run the application
run_app() {
    echo "Starting the Silly Walk Grant Application Orchestrator..."
    python run.py
}

# Main script
case "$1" in
    setup)
        install_dependencies
        ;;
    test)
        run_tests
        ;;
    run)
        run_app
        ;;
    all)
        install_dependencies
        run_tests
        run_app
        ;;
    *)
        echo "Usage: $0 {setup|test|run|all}"
        echo "  setup: Install dependencies"
        echo "  test: Run tests"
        echo "  run: Start the application"
        echo "  all: Setup, test, and run"
        exit 1
        ;;
esac

exit 0
