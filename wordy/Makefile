.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -vv wordy_test.py
	mypy --strict wordy.py
	/usr/local/bin/python3 -m pylint wordy.py