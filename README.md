# Django Cookbook

[How to Read **"Django"**](https://lucas-six.github.io/django-cookbook/audio/django_pronunciation.mp3)

## Target

- Python 3.12 with Django 4.2 (DRF)
- Database: PostgreSQL 16
- Cache: Redis 7
- Linting & Type Checking: Ruff, Mypy
- Colorful Logging
- Debug Toolbar

## Quick Start

### Requirements

- Python 3.12
- PostgreSQL 16
- Redis 7

### Database (PostgreSQL)

```ini
# postgresql.conf

#listen_addresses = 'localhost'  # '*' for all
#port = 5432
max_connections = 1024
password_encryption = scram-sha-256
client_encoding = 'UTF8'
default_transaction_isolation = 'read committed'
timezone = 'UTC'
```

### Setup

```bash
cp -r pyproject.toml lint.bash .pre-commit-config.yaml .vscode/ <target-path>

# Modify pyproject.toml

cd <target-path>
uv sync

$ uv run --env-file .env django-admin version
4.2.x

uv run --env-file .env django-admin startproject <target-project>

# Create App
uv run --env-file .env python <target-project>/manage.py startapp <app_name>
mv <app_name> <target-project>/.

# Modify settings.py

# Run
uv run --env-file .env python <target-project>/manage.py makemigrations
uv run --env-file .env python <target-project>/manage.py migrate
uv run --env-file .env python <target-project>/manage.py createsuperuser
uv run --env-file .env python <target-project>/manage.py runserver [localhost:8000]
```

### Lint

```bash
chmod u+x lint.bash
./lint.bash
```

## More

- [PostgreSQL Setup - Linux Cookbook](https://lucas-six.github.io/linux-cookbook/cookbook/admin/postgresql/postgresql_setup)
- [PostgreSQL CLI: `psql` Usage - Linux Cookbook](https://lucas-six.github.io/linux-cookbook/cookbook/admin/postgresql/postgresql_usage)
- [Redis Setup - Linux Cookbook](https://lucas-six.github.io/linux-cookbook/cookbook/admin/redis/redis_setup)
- [CLI: `redis-cli` Basic Usage - Linux Cookbook](https://lucas-six.github.io/linux-cookbook/cookbook/admin/redis/redis_usage_basic)
- [Redis Python API: `redis-py` - Python Coobook](https://lucas-six.github.io/python-cookbook/cookbook/system_services/redis)
- [Logging Usage - Python Cookbook](https://lucas-six.github.io/python-cookbook/cookbook//core/logging/logging_usage)
- [Logging Dictionary Configuration - Python Cookbook](https://lucas-six.github.io/python-cookbook/cookbook//core/logging/logging_dict_config)

## References

- [Django Documentation](https://docs.djangoproject.com/)
- [`django-stubs` PyPI](https://pypi.org/project/django-stubs/)
- [PostgreSQL Home](https://www.postgresql.org/)
- [`psycopg` Documetation](https://www.psycopg.org/psycopg3/docs/)
- [Django Cache Framework](https://docs.djangoproject.com/en/4.2/topics/cache/)
- [Redis Documentation](https://redis.io/docs/)
- [`redis-py` Documentation](https://redis.readthedocs.io/en/latest/)
- [Django Logging](https://docs.djangoproject.com/en/4.2/topics/logging/)
- [`django-debug-toolbar` Documentation](https://django-debug-toolbar.readthedocs.io/en/latest/)
- [`django-rest-framework` Home](https://www.django-rest-framework.org/)
