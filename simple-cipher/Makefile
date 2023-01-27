.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -xv simple_cipher_test.py
	mypy --strict simple_cipher.py
	/usr/local/bin/python3 -m pylint simple_cipher.py