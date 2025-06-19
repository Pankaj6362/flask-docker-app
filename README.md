
# Simple Flask App in Docker

This is a basic Python Flask web application running inside a Docker container.

## Prerequisites

- Docker installed on your system

## How to Build and Run

### Step 1: Build the Docker Image

```bash
docker build -t flask-docker-app .

docker run -d -p 5000:5000 --name flask-container flask-docker-app
