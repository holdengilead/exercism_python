.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -vv affine_cipher_test.py
	mypy --strict affine_cipher.py
	/usr/local/bin/python3 -m pylint affine_cipher.py