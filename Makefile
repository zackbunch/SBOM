
# SHELL := /usr/bin/env bash
VENV := venv
VENV_ACTIVATE := $(VENV)/bin/activate
ACTIVATE_ENV = source $(VENV)/bin/activate
PYTHON := $(VENV)/bin/python3
PIP := $(VENV)/bin/pip

all: venv

# venv is a shortcut target
venv:$(VENV)/bin/activate
	
$(VENV_ACTIVATE): requirements.txt
	python3 -m venv $(VENV)
	./$(PIP) install -r requirements.txt --no-cache-dir

run:
	$(ACTIVATE_ENV) && ./$(PYTHON) sysk.py

lint:
	$(PYTHON) -m pylint src

format:
	$(PYTHON) -m black src
	$(PYTHON) -m isort src 

test: $(ACTIVATE_ENV)
	$(PYTHON) -m pytest src/tests

build:
	python3 -m pip install --upgrade build
	python3 -m build


clean:
	rm -rf $(VENV)
	find . -type f -name '*.json' -delete
	find . -type f -name '*.pyc' -delete
	find . -type d -name __pycache__ -delete

.PHONY: all venv run clean lint format test build