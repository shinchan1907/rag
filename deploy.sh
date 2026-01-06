#!/bin/bash

# Pull the latest changes
git pull

# Rebuild and restart the containers
docker compose up -d --build

# Show the status
docker compose ps

# Show backend logs to check for startup errors
echo "Checking backend logs..."
docker compose logs --tail=50 fastapi_backend
