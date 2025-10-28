.PHONY: build up down restart logs clean ps install

# Build the Docker image
build:
	docker-compose build

# Run the container in detached mode
up:
	docker-compose up -d --build

# Stop the container
down:
	docker-compose down

# Restart the container
restart: down up

# View container logs
logs:
	docker-compose logs -f 

# Remove containers, networks, and images
clean:
	docker-compose down --rmi all --volumes --remove-orphans

# Show running containers
ps:
	docker-compose ps

# Install dependencies
install:
	poetry install


