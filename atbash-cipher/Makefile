.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -vv atbash_cipher_test.py
	mypy --strict atbash_cipher.py
	/usr/local/bin/python3 -m pylint atbash_cipher.py