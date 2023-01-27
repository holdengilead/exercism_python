.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -vv queen_attack_test.py
	mypy --strict queen_attack.py
	/usr/local/bin/python3 -m pylint queen_attack.py