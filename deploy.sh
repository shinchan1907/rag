#!/bin/bash
set -e

# Colors
GREEN='\033[0;32m'
NC='\033[0m'

echo -e "${GREEN}Deploying Jyoti AI...${NC}"

# 1. Pull latest code
echo -e "${GREEN}Pulling latest changes...${NC}"
git stash # Stash local changes (like .env) to avoid conflicts
git pull
git stash pop || true # Restore local changes, ignore if nothing to pop

# 2. Build Docs
echo -e "${GREEN}Building Documentation...${NC}"

# 3. Restart Services
echo -e "${GREEN}Restarting Services...${NC}"
# Try 'docker compose' first, fallback to 'docker-compose'
if docker compose version > /dev/null 2>&1; then
    DOCKER_COMPOSE_CMD="docker compose"
else
    DOCKER_COMPOSE_CMD="docker-compose"
fi

$DOCKER_COMPOSE_CMD down --remove-orphans
$DOCKER_COMPOSE_CMD up -d --build

# 4. Verify
echo -e "${GREEN}Verifying Deployment...${NC}"
sleep 10
$DOCKER_COMPOSE_CMD ps

echo -e "${GREEN}Deployment Complete!${NC}"
echo -e "Docs:      https://ai.bytenex.io/"
echo -e "API:       https://ai.bytenex.io/api/health"
echo -e "Grafana:   https://ai.bytenex.io/grafana/"
