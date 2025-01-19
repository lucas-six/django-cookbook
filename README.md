# Django Cookbook

[How to Read **"Django"**](https://lucas-six.github.io/django-cookbook/audio/django_pronunciation.mp3)

## Quick Start

### Setup

```bash
pipenv --python 3.11
pipenv install --dev black isort mypy pylint

pipenv install "django~=4.2"
pipenv install "django-stubs[compatible-mypy]"
pipenv install --dev pylint-django
#pipenv install --dev flake8-django

$ pipenv run django-admin version
4.2.7

pipenv run django-admin startproject django_cookbook
```

### Database (PostgreSQL)

```bash
pipenv install 'psycopg[binary, pool]>=3.2'
```

```ini
# postgresql.conf

client_encoding = 'UTF8'
default_transaction_isolation = 'read committed'
timezone = 'UTC'
```

### Cache (Redis)

```bash
pipenv install redis[hiredis] types-redis
```

### Logging

```bash
pipenv install --dev colorlog
```

### Lint

```bash
pipenv run black .
pipenv run isort .
pipenv run mypy .
DJANGO_SETTINGS_MODULE="django_cookbook" pipenv run pylint .
```

### Run

```bash
pipenv run python django_cookbook/manage.py makemigrations
pipenv run python django_cookbook/manage.py migrate
pipenv run python django_cookbook/manage.py createsuperuser
pipenv run python django_cookbook/manage.py runserver [localhost:8000]
```

### Debug Toolbar

```bash
pipenv install --dev django-debug-toolbar
```

### Django REST Framework (DRF)

```bash
pipenv install djangorestframework
```

### Create App

```bash
pipenv run python django_cookbook/manage.py startapp <app_name>
mv app django_cookbook/.
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
