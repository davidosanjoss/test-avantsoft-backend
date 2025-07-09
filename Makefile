# ====================
# CONFIG DEV
# ====================
COMPOSE_DEV = docker compose -f docker-compose.dev.yml
ENV_FILE_DEV = .env

up-dev:
	$(COMPOSE_DEV) up --build

down-dev:
	$(COMPOSE_DEV) down -v

bash-dev:
	$(COMPOSE_DEV) exec web bash

migrate-dev:
	$(COMPOSE_DEV) exec web python manage.py migrate

super-user-dev:
	$(COMPOSE_DEV) exec web python manage.py createsuperuser

test-dev:
	$(COMPOSE_DEV) exec web pytest

# ====================
# CONFIG PROD
# ====================
COMPOSE_PROD = docker compose -f docker-compose.prod.yml
ENV_FILE_PROD = .env

up-prod:
	$(COMPOSE_PROD) up --build

down-prod:
	$(COMPOSE_PROD) down -v

bash-prod:
	$(COMPOSE_PROD) exec web bash

migrate-prod:
	$(COMPOSE_PROD) exec web python manage.py migrate

super-user-prod:
	$(COMPOSE_PROD) exec web python manage.py createsuperuser

test-prod:
	$(COMPOSE_PROD) exec web pytest
