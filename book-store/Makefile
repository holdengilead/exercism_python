.PHONY: test

test:
	pytest -vv book_store_test.py
	mypy --strict *.py
	pylint book_store.py