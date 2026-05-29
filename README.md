# AI-Powered Customer Request Routing System

## Overview

This project is a mini AI-powered customer request routing system built using Django, Django REST Framework, PostgreSQL, Redis, Celery, and JWT authentication.

The system allows authenticated(JWT authentication) users to submit customer requests, process them asynchronously using a mock AI classifier, and manage them through a simple dashboard.

## Features

* JWT Authentication
* Customer request submission
* Async AI classification using Celery
* Redis task queue
* PostgreSQL database
* Dashboard for viewing requests
* Request detail page
* Status updates
* Live auto-refresh dashboard behavior implemented using periodic polling.

## Tech Stack

* Django
* Django REST Framework
* PostgreSQL
* Redis
* Celery
* HTML
* JavaScript

## Setup Instructions

### Clone Repository

```bash
git clone <repo-url>
cd project-name
```

### Create Virtual Environment

python -m venv venv

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create `.env` file:

```env
SECRET_KEY=your_secret_key

DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432
```

### Run Migrations

```bash
python manage.py migrate
```

### Start Redis

```bash
docker run -d -p 6379:6379 redis
```

### Start Celery Worker

```bash
celery -A pro worker -l info -P solo
```

### Run Server

```bash
python manage.py runserver
```
## AI Workflow

1. User submits request.
2. API stores request immediately.
3. Celery task is triggered.
4. Mock AI classifier processes message.
5. Request classification and status are updated.
6. Dashboard reflects latest updates.

## Architecture

Frontend → Django API → PostgreSQL

Django API → Redis Queue → Celery Worker → Mock AI Classifier

## API Endpoints

| Method | Endpoint            | Purpose        |
| ------ | ------------------- | -------------- |
| POST   | /api/token/         | JWT Login      |
| GET    | /api/requests/      | List Requests  |
| POST   | /api/requests/      | Create Request |
| GET    | /api/requests/<id>/ | Request Detail |
| PATCH  | /api/requests/<id>/ | Update Status  |

## Known Limitations

* Mock AI classification only
* Minimal frontend UI
* Auto-refresh used instead of full WebSocket implementation
* No role-based permissions

## Future Improvements

With two more weeks, I would improve:

* Full WebSocket realtime updates
* Role-based access control
* Internal notes system
* Better frontend UI
* Docker Compose deployment
* Retry logic for failed AI tasks

## Live Demo

Demo Link : https://ai-customer-routing-system-production.up.railway.app/

This project uses Celery + Redis for asynchronous request classification during local development.
In the deployed Railway version, Redis/Celery worker infrastructure is not enabled due to free-tier service limitations. Customer requests are still stored and managed normally, but background classification tasks are not processed in production.

## Demo Credentials

Username: mithun
Password: mithun