.PHONY: test

test:
	pytest -v generators_test.py
	mypy --strict generators.py
	pylint generators.py