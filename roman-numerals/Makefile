.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -vv roman_numerals_test.py
	mypy --strict roman_numerals.py
	/usr/local/bin/python3 -m pylint roman_numerals.py