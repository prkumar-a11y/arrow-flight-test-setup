.PHONY: install setup run-server run-client test benchmark docker-build docker-up docker-down clean help

install:
	pip install -r requirements.txt

setup: install
	@echo "Setup complete!"

run-server:
	python server/flight_server.py

run-client:
	python client/flight_client.py

test:
	pytest tests/ -v --tb=short

docker-build:
	docker-compose build

docker-up:
	docker-compose up -d

docker-down:
	docker-compose down

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

help:
	@echo "Arrow Flight Setup - Commands: install, setup, run-server, run-client, test, docker-build, docker-up, docker-down, clean"