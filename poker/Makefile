.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -xvv poker_test.py
	mypy --strict poker.py
	/usr/local/bin/python3 -m pylint poker.py