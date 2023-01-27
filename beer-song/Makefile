.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -xvv beer_song_test.py
	mypy --strict beer_song.py
	mypy --strict beer_song_test.py
	/usr/local/bin/python3 -m pylint beer_song.py