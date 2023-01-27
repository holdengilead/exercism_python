.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -vv pig_latin_test.py
	mypy --strict pig_latin.py
	/usr/local/bin/python3 -m pylint pig_latin.py