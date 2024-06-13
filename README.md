# Custom logging for FastAPI
This application formats output logs to a log file.
There are two loggers "main" It needs for log your data, and request/response log as middleware for logging all incoming and outgoing information

## Requirements
- loguru
- fastapi
- stackprinter
- uvicorn
- sqlalchemy
- alembic

## Run app
```
uvicorn --host=0.0.0.0 --port 8888 app.main:app --reload

```

## Project Structe
```
.
├── app
│   ├── api
│   │   ├── __init__.py
│   │   └── v1
│   │       ├── endpoints
│   ├── core
|   │   ├── config.py
│   │   ├── __init__.py
│   │   ├── logging_config.py
│   ├── db
│   │   ├── base.py
│   │   ├── crud.py
│   │   ├── init_db.py
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   └── session.py
│   ├── exceptions
│   │   ├── handlers.py
│   │   ├── __init__.py
│   ├── __init__.py
│   ├── main.py
│   ├── middleware
│   │   ├── __init__.py
│   │   ├── logging_middleware.py
│   ├── services
│   │   ├── __init__.py
│   │   └── redis_service.py
│   └── test
│       └── __init__.py
├── logs
│   └── app.log
├── poetry.lock
├── pyproject.toml
├── README.md
├── requirements.txt
└── test.db
```
