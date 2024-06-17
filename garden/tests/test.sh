#!/bin/bash
export PG_HOST=127.0.0.1
export PG_PORT=5432
export PG_USER=test
export PG_PASSWORD=test
export PG_DBNAME=test

export MINIO_USE_HTTPS=False
export MINIO_ACCESS_KEY=Px50bigfQ2RwNKphG0Ee
export MINIO_SECRET_KEY=H6XnWKXrsSeiRxLONkdmgoEtCs3zPIn0nphAtRmm
export MINIO_ENDPOINT=http://localhost:9000

python3 garden/manage.py test $1