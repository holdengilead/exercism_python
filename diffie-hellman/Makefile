.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -vv diffie_hellman_test.py
	mypy --strict diffie_hellman.py
	/usr/local/bin/python3 -m pylint diffie_hellman.py