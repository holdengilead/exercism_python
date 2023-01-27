.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -xvv secret_handshake_test.py
	mypy --strict secret_handshake.py
	/usr/local/bin/python3 -m pylint secret_handshake.py