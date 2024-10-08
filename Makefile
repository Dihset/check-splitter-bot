.PHONY: all

SHELL=/bin/bash -e
STORAGES=docker-compose/storages.yaml
MONITORING=docker-compose/monitoring.yaml

format:
	poetry run ruff format .
	poetry run ruff check --fix .

up_storages:
	docker-compose --env-file .env -f ${STORAGES} up -d

up_monitoring:
	docker-compose --env-file .env -f ${MONITORING} up -d

down:
	docker-compose --env-file .env-f ${STORAGES} down

migrate: ## migrate dev
	alembic upgrade head

makemigrations: ## makemigrations dev
	alembic revision --autogenerate -m="$(m)"

downgrade:
	alembic downgrade -1