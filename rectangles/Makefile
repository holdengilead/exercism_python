.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -xvv rectangles_test.py
	mypy --strict rectangles.py
	/usr/local/bin/python3 -m pylint rectangles.py