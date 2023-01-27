.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -vv run_length_encoding_test.py
	mypy --strict run_length_encoding.py
	/usr/local/bin/python3 -m pylint run_length_encoding.py