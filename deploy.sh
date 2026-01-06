#!/bin/bash

# 1. Pull latest code
git pull

# 2. Check Docker version for debugging
docker version

# 3. Clean up EVERYTHING (Containers, Networks, Orphans)
docker compose down --remove-orphans

# 4. Prune unused images to save space (Optional but good for clean slate)
docker image prune -f

# 5. Build and Start
docker compose up -d --build

# 6. Wait a moment and show status
sleep 5
docker compose ps

# 7. Show logs to verify startup
echo "--- Traefik Logs ---"
docker compose logs --tail=20 traefik
echo "--- Backend Logs ---"
docker compose logs --tail=20 fastapi_backend
