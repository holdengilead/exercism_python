.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -vv dnd_character_test.py
	mypy --strict dnd_character.py
	/usr/local/bin/python3 -m pylint dnd_character.py