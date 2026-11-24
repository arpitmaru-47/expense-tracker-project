
# Personal Expense Tracker

A simple expense tracking web application built using Python Flask, SQLite and Docker.

## Features

- Add daily expenses
- View all expenses
- Update existing expenses
- Delete expenses
- Calculate total expenses
- Count total transactions
- Persistent database storage

## Technology Stack

- Python
- Flask
- SQLite
- HTML
- CSS
- Docker
- Docker Compose

## Project Structure

expense-tracker/
- app.py
- Dockerfile
- compose.yaml
- requirements.txt
- .dockerignore
- .gitignore
- README.md
- templates/
- static/
- data/

## Run Using Docker Compose

### 1. Clone Repository

git clone YOUR_REPOSITORY_URL

### 2. Enter Project

cd expense-tracker

### 3. Start Application

docker compose up -d --build

### 4. Open Browser

http://localhost:5000

## Useful Docker Commands

docker compose ps

docker compose logs

docker compose down

docker compose up -d

## Learning Outcomes

- Docker image creation
- Container management
- Port mapping
- Docker volumes
- Data persistence
- Docker networking
- Docker Compose
