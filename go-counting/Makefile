.PHONY: test

test:
	pytest -vv go_counting_test.py
	mypy --strict *.py
	pylint go_counting.py