.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -vv simple_linked_list_test.py
	mypy --strict simple_linked_list.py
	/usr/local/bin/python3 -m pylint simple_linked_list.py