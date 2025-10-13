# Django Cookbook

[How to Read **"Django"**](https://lucas-six.github.io/django-cookbook/audio/django_pronunciation.mp3)

## Target Environment

- Python 3.13 with Django 4.2 (DRF)
- Database: PostgreSQL 16
- Cache: Redis 8
- Linting & Type Checking: Ruff, Mypy
- Colorful Logging
- Debug Toolbar

## Quick Start

### Requirements

- Python 3.13
- PostgreSQL 16 (See [Setup PostgreSQL](https://lucas-six.github.io/linux-cookbook/cookbook/admin/postgresql/postgresql_setup))
- Redis 7/8 (See [Setup Redis](https://lucas-six.github.io/linux-cookbook/cookbook/admin/redis/redis_setup))

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

- [PostgreSQL CLI: `psql` Usage - Linux Cookbook](https://lucas-six.github.io/linux-cookbook/cookbook/admin/postgresql/postgresql_usage)
- [Redis CLI: `redis-cli` Basic Usage - Linux Cookbook](https://lucas-six.github.io/linux-cookbook/cookbook/admin/redis/redis_usage_basic)
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
