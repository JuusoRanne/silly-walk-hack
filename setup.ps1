# Setup and run script for the Silly Walk Grant Application Orchestrator

# Function to install dependencies
function Install-Dependencies {
    Write-Host "Installing dependencies..." -ForegroundColor Green
    pip install -r requirements.txt
    Write-Host "Dependencies installed successfully!" -ForegroundColor Green
}

# Function to run tests
function Run-Tests {
    Write-Host "Running tests..." -ForegroundColor Green
    python -m pytest
    Write-Host "Tests completed!" -ForegroundColor Green
}

# Function to run the application
function Start-Application {
    Write-Host "Starting the Silly Walk Grant Application Orchestrator..." -ForegroundColor Green
    python run.py
}

# Process command-line arguments
param(
    [Parameter(Position=0)]
    [ValidateSet("setup", "test", "run", "all")]
    [string]$Command = "help"
)

switch ($Command) {
    "setup" {
        Install-Dependencies
    }
    "test" {
        Run-Tests
    }
    "run" {
        Start-Application
    }
    "all" {
        Install-Dependencies
        Run-Tests
        Start-Application
    }
    default {
        Write-Host "Usage: .\setup.ps1 {setup|test|run|all}" -ForegroundColor Yellow
        Write-Host "  setup: Install dependencies" -ForegroundColor White
        Write-Host "  test: Run tests" -ForegroundColor White
        Write-Host "  run: Start the application" -ForegroundColor White
        Write-Host "  all: Setup, test, and run" -ForegroundColor White
    }
}
