# Botanical Garden

**Prerequisites:**
- Docker installed and running.
- Docker Compose installed.

**Usage:**

1. **Build&Run containers:**
   ```bash
   docker compose up --build -d
   ```
2. **Install requirements**
   ```bash
   python3 -m venv venv
   source ./venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Fill .env credentials**
    ```
    MINIO_ACCESS_KEY=<TOKEN>
    MINIO_SECRET_KEY=<TOKEN>
    ```

4. **Make Django migrations**
   ```bash
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```

5. **Create Django superuser**
   ```bash
   python3 manage.py createsuperuser
   ```

6. **Run server**
   ```bash
   python3 manage.py runserver
   ```