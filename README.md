# Personal Expense Tracker – Docker Advanced Capstone

A containerized expense tracking application built using Flask, SQLite, Docker, Docker Compose, Gunicorn, and Nginx.

This project demonstrates practical Docker and DevOps concepts, including multi-stage builds, container security, persistent storage, reverse proxy, health checks, logging, and troubleshooting.

## Architecture

```text
User Browser
     |
     v
Nginx (Port 8080)
     |
     v
Flask + Gunicorn (Port 5000)
     |
     v
SQLite Database
(Persistent Storage)
```

## Features

- Add, view, edit, and delete expenses
- Expense dashboard with total amount and transaction count
- SQLite persistent database storage
- Flask application served using Gunicorn
- Nginx reverse proxy
- Docker multi-stage build
- Non-root container user
- Read-only root filesystem
- Dropped Linux capabilities
- Docker health checks
- Resource limits
- Docker logging and log rotation
- Isolated frontend and backend networks
- Environment variable configuration
- Docker Compose secrets

## Technology Stack

| Technology | Purpose |
|---|---|
| Python / Flask | Backend |
| SQLite | Database |
| HTML / CSS | Frontend |
| Docker | Containerization |
| Docker Compose | Multi-container orchestration |
| Gunicorn | WSGI application server |
| Nginx | Reverse proxy |

## Project Structure

```text
expense-tracker/
├── app.py
├── requirements.txt
├── Dockerfile
├── compose.yaml
├── .dockerignore
├── .gitignore
├── .env.example
├── nginx/
│   └── default.conf
├── secrets/
│   └── app_secret.txt  # Create locally
├── data/               # Created locally
├── templates/
├── static/
└── README.md
```

## Prerequisites

- Docker Engine
- Docker Compose plugin
- Git

## Setup and Run

### 1. Clone the repository

```bash
git clone https://github.com/arpitmaru-47/expense-tracker-project.git
cd expense-tracker-project
```

### 2. Create environment configuration

```bash
cp .env.example .env
```

### 3. Create the local Docker secret

```bash
mkdir -p secrets data
echo "local-demo-secret-change-me" > secrets/app_secret.txt
```

Replace the demo value with a suitable local secret if the application actually uses it.

### 4. Build and start containers

```bash
docker compose config
docker compose up -d --build
```

### 5. Open the application

Visit:

http://localhost:8080

### 6. Check container status

```bash
docker compose ps
```

### 7. View logs

```bash
docker compose logs --tail 50
```

## Docker Security

The project demonstrates:

- Non-root application user
- Read-only root filesystem
- Dropped Linux capabilities
- No-new-privileges security option
- Temporary filesystems for writable temporary paths
- Container CPU and memory limits
- Separate frontend and backend networks
- Local Compose secrets configuration

Note: File-backed Compose secrets are not a replacement for an encrypted production secrets manager.

## Monitoring and Troubleshooting

```bash
docker compose ps
docker compose logs web
docker compose logs nginx
docker stats
docker top expense-app
docker inspect expense-app
docker compose config
```

## Data Persistence

The SQLite database is stored in the local `data/` directory through a bind mount.

This allows application data to survive container recreation. Back up the database separately.

## Learning Outcomes

Through this project, I practiced:

- Docker image optimization
- Multi-stage Docker builds
- Docker Compose networking
- Nginx reverse proxy configuration
- Container security hardening
- Persistent storage
- Health checks
- Logging and monitoring
- Deployment troubleshooting
- Database backup and recovery

## Author

**Arpit Maru**

GitHub: https://github.com/arpitmaru-47

---

*This project is a Docker Advanced learning capstone. It is not claimed to be a fully production-certified application.*