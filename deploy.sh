#!/bin/bash

# Pull the latest changes
git pull

# Rebuild and restart the containers
docker compose up -d --build

# Show the status
docker compose ps
