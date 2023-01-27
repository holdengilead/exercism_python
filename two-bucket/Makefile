.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -vv two_bucket_test.py
	mypy --strict two_bucket.py
	/usr/local/bin/python3 -m pylint two_bucket.py