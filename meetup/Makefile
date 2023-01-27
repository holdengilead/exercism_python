.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -xvv meetup_test.py
	mypy --strict meetup.py
	/usr/local/bin/python3 -m pylint meetup.py