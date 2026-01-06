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

# Ensure Docker Compose Plugin is installed
if ! docker compose version > /dev/null 2>&1; then
    echo -e "${GREEN}Installing Docker Compose Plugin...${NC}"
    sudo apt-get update
    sudo apt-get install -y docker-compose-plugin
fi

docker compose down --remove-orphans
docker compose up -d --build

# 4. Verify
echo -e "${GREEN}Verifying Deployment...${NC}"
sleep 10
$DOCKER_COMPOSE_CMD ps

echo -e "${GREEN}Deployment Complete!${NC}"
echo -e "Docs:      https://ai.bytenex.io/"
echo -e "API:       https://ai.bytenex.io/api/health"
echo -e "Grafana:   https://ai.bytenex.io/grafana/"
