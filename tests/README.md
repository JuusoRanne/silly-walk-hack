# Running Tests for the Silly Walk Grant Application Orchestrator

This document provides instructions for running the test suite for the Silly Walk Grant Application Orchestrator.

## Prerequisites

Make sure you have installed all the dependencies:

```bash
pip install -r requirements.txt
pip install pytest  # For running tests
```

## Running the Tests

### Using pytest

To run all the tests with pytest:

```bash
pytest
```

For a more detailed output:

```bash
pytest -v
```

To run a specific test file:

```bash
pytest tests/test_scoring_service.py
```

### Using unittest

To run all the tests with unittest:

```bash
python -m unittest discover tests
```

To run a specific test file:

```bash
python -m unittest tests/test_scoring_service.py
```

## Test Coverage

To check test coverage:

```bash
pip install pytest-cov
pytest --cov=app tests/
```

## Running the Application

To start the application:

```bash
python run.py
```

The API will be available at http://localhost:8000/api/v1

You can access the automatically generated API documentation at http://localhost:8000/docs
