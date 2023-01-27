.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -xvv minesweeper_test.py
	mypy --strict minesweeper.py
	/usr/local/bin/python3 -m pylint minesweeper.py