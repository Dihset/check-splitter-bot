.PHONY: all

SHELL=/bin/bash -e
STORAGES=docker-compose/storages.yaml

lint:
	poetry run ruff check --fix .

format:
	poetry run ruff format .

up_storages:
	docker-compose --env-file .env -f ${STORAGES} up -d

down:
	docker-compose --env-file .env-f ${STORAGES} down