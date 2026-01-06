#!/bin/bash
set -e

# Colors
GREEN='\033[0;32m'
NC='\033[0m'

echo -e "${GREEN}Deploying Jyoti AI...${NC}"

# 1. Pull latest code
git pull

# 2. Build Docs
echo -e "${GREEN}Building Documentation...${NC}"
# We need to build the docs site before mounting it, or let the container do it. 
# The squidfunk/mkdocs-material image runs 'mkdocs serve' by default which is fine for dev/prod if exposed.
# But for better performance, we could build to static HTML. 
# For now, we'll let the container serve it dynamically.

# 3. Restart Services
echo -e "${GREEN}Restarting Services...${NC}"
docker compose down --remove-orphans
docker compose up -d --build

# 4. Verify
echo -e "${GREEN}Verifying Deployment...${NC}"
sleep 10
docker compose ps

echo -e "${GREEN}Deployment Complete!${NC}"
echo -e "Docs:      https://ai.bytenex.io/"
echo -e "API:       https://ai.bytenex.io/api/health"
echo -e "Grafana:   https://ai.bytenex.io/grafana/"
