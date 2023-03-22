.PHONY: test

test:
	pytest -vv grep_test.py
	mypy --strict grep.py
	pylint grep.py