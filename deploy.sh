#!/bin/bash
set -e # Exit on error

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}Starting Deployment Process...${NC}"

# 1. Update Codebase
echo -e "${GREEN}[1/5] Pulling latest changes...${NC}"
git pull

# 2. Check Environment
echo -e "${GREEN}[2/5] Checking Docker Environment...${NC}"
docker version > /dev/null 2>&1 || { echo "Docker is not running!"; exit 1; }

# 3. Clean Slate
echo -e "${GREEN}[3/5] Cleaning up old resources...${NC}"
docker compose down --remove-orphans
docker system prune -f > /dev/null 2>&1 # Optional: Clean unused images

# 4. Build and Launch
echo -e "${GREEN}[4/5] Building and Starting Services...${NC}"
docker compose up -d --build

# 5. Verification
echo -e "${GREEN}[5/5] Verifying Deployment...${NC}"
sleep 5
docker compose ps

echo -e "${YELLOW}--- Backend Logs (Last 50 lines) ---${NC}"
docker compose logs --tail=50 backend

echo -e "${YELLOW}--- Traefik Logs (Last 20 lines) ---${NC}"
docker compose logs --tail=20 traefik

echo -e "${GREEN}Deployment Complete!${NC}"
echo -e "Dashboard: https://ai.bytenex.io/dashboard/"
echo -e "API Docs:  https://ai.bytenex.io/docs"
