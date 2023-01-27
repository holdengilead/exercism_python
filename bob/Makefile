.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -xv bob_test.py
	mypy --strict bob.py
	/usr/local/bin/python3 -m pylint bob.py