.PHONY: test

test:
	pytest -vv connect_test.py
	mypy --strict *.py
	pylint connect.py