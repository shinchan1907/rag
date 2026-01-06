#!/bin/bash

# Pull the latest changes
git pull

# Check Docker version on host
docker version

# Verify config
echo "Verifying Docker config in compose file..."
grep "DOCKER" docker-compose.yml

# Clean up old containers
docker compose down --remove-orphans

# Rebuild and restart the containers
docker compose up -d --build

# Show the status
docker compose ps

# Show logs
echo "Checking backend logs..."
docker compose logs --tail=20 fastapi_backend
echo "Checking traefik logs..."
docker compose logs --tail=20 traefik
