.PHONY: build up demo clean

IMAGE_NAME = password-cracker
ARTIFACTS_DIR = $(PWD)/artifacts/release

init:
	mkdir -p "$(ARTIFACTS_DIR)"
	mkdir -p data

build: init
	docker build -t $(IMAGE_NAME) .

up: build
	@echo "System is up. Docker image built and ready."

demo: up
	@echo "--- 1. Running Unit Tests ---"
	docker run --rm $(IMAGE_NAME) pytest tests/
	@echo "--- 2. Running End-to-End Analysis ---"
	docker run --rm -v "$(ARTIFACTS_DIR):/app/artifacts/release" $(IMAGE_NAME) python src/main.py
	@echo "---------------------------------------------------"
	@echo "DEMO COMPLETE. Check artifacts/release/ for report."
	@echo "---------------------------------------------------"

clean:
	rm -rf artifacts/release/* data/*

	find . -name "__pycache__" -type d -exec rm -rf {} +
