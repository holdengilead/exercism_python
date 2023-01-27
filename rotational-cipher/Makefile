.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -vv rotational_cipher_test.py
	mypy --strict rotational_cipher.py
	/usr/local/bin/python3 -m pylint rotational_cipher.py