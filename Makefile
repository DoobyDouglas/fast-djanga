up:
	docker-compose up -d
run:
	python main.py
format:
	ruff check --fix
	ruff format
check:
	mypy dependencies
	mypy fast_djanga
	mypy hash
	mypy settings
	mypy tokens
celery:
	celery -A task.app:app worker -B -l info