install:
	poetry install

import: install
	poetry add prompt

build:
	poetry build

pub:
	poetry publish -r ppt
lint:
	poetry run flake8 brain_games
