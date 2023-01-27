.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -xv allergies_test.py
	mypy --strict allergies.py
	/usr/local/bin/python3 -m pylint allergies.py