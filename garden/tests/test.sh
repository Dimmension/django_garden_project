#!/bin/bash
export PG_HOST=127.0.0.1
export PG_PORT=5432
export PG_USER=test
export PG_PASSWORD=test
export PG_DBNAME=test

export MINIO_CONSISTENCY_CHECK_ON_START=False

export MINIO_ROOT_USER=minioadmin
export MINIO_ROOT_PASSWORD=minioadmin

export MINIO_ACCESS_KEY=nAIQPSuVvwBF7FkBIk24
export MINIO_SECRET_KEY=6Xrfq5KUZEcgzGx9FKjlF6BIuL0KoW54RgBYLQDC

python3 garden/manage.py test $1