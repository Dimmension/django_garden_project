#!/bin/bash
export POSTGRES_HOST=127.0.0.1
export POSTGRES_PORT=5432
export POSTGRES_USER=test
export POSTGRES_PASSWORD=test
export POSTGRES_DB=test

export SECRET_KEY=sirius
export MINIO_USE_HTTPS=False
export MINIO_ACCESS_KEY=Px50bigfQ2RwNKphG0Ee
export MINIO_SECRET_KEY=H6XnWKXrsSeiRxLONkdmgoEtCs3zPIn0nphAtRmm
export MINIO_ENDPOINT=http://localhost:9000
export MINIO_CONSISTENCY_CHECK_ON_START=False

python3 garden/manage.py test $1