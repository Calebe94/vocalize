############
# vocalize #
############

upload:
	@. venv/bin/activate; pip install --upgrade twine; twine upload dist/*

test:
	@python -m unittest tests.test

build:
	@virtualenv venv
	@. venv/bin/activate; pip install --upgrade build; python -m build

install:
	@pip install .

clean:
	@rm -fr build dist venv src/lotodice.egg-info src/lotodice/__pycache__

.PHONY: build test install clean
