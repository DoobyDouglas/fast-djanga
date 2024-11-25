up:
	docker-compose up -d
run:
	python main.py
format:
	ruff check --fix
	ruff format
celery:
	celery -A task.app:app worker -B -l info