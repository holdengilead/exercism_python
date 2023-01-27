.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -xvv ocr_numbers_test.py
	mypy --strict ocr_numbers.py
	/usr/local/bin/python3 -m pylint ocr_numbers.py