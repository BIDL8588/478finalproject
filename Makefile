.PHONY: build up demo clean

IMAGE_NAME = password-cracker
ARTIFACTS_DIR = $(PWD)/artifacts/release

# Windows/Linux compatibility for directory creation
init:
	mkdir -p "$(ARTIFACTS_DIR)"
	mkdir -p data

# Builds the Docker image (The 'Environment')
build: init
	docker build -t $(IMAGE_NAME) .

# Requirement: 'make up' must prepare the system.
# Since we aren't using docker-compose, 'up' just ensures the image is built.
up: build
	@echo "System is up. Docker image built and ready."

# Requirement: 'make demo' runs the vertical slice.
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