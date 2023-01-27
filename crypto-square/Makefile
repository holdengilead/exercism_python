.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -vv crypto_square_test.py
	mypy --strict crypto_square.py
	/usr/local/bin/python3 -m pylint crypto_square.py