#!/bin/bash

if [ "$1" = "build" ]; then
    echo "=> Building images..."
    docker-compose -f docker-compose.dev.yml build
fi

docker-compose -f docker-compose.dev.yml up --build
