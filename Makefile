up:
	docker compose -f docker-compose.dev.yml up --build

down:
	docker compose -f docker-compose.dev.yml down -v

bash:
	docker compose -f docker-compose.dev.yml exec web bash

migrate:
	docker compose -f docker-compose.dev.yml exec web python manage.py migrate

createsuperuser:
	docker compose -f docker-compose.dev.yml exec web python manage.py createsuperuser
