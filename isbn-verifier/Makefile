.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -xv isbn_verifier_test.py
	mypy isbn_verifier.py
	/usr/local/bin/python3 -m pylint isbn_verifier.py