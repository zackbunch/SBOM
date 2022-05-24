
# define the name of the virtual environment directory
VENV := venv

# default target, when make executed without arguments
all: venv
	

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	./$(VENV)/bin/pip install -r requirements.txt --no-cache-dir

# venv is a shortcut target
venv: $(VENV)/bin/activate

run: venv
	./$(VENV)/bin/python3 sysk.py

lint:
	python3 -m pylint --version
	python3 -m pylint src


test:
	python3 -m pytest --version
	python3 -m pytest tests

black:
	python3 -m black --version
	python3 -m black src

clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete
	find . -type d -name __pycache__ -delete

.PHONY: all venv run clean lint black test