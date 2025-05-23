# Generated by Django 4.2.18 on 2025-01-19 03:03

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='A',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    ),
                ),
                (
                    'uuid',
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, unique=True, verbose_name='uuid'
                    ),
                ),
                ('name', models.CharField(max_length=64, verbose_name='name')),
                (
                    'nickname',
                    models.CharField(default='[unknown]', max_length=64, verbose_name='nickname'),
                ),
                (
                    'sex',
                    models.CharField(
                        blank=True,
                        choices=[('M', 'Man'), ('F', 'Female'), ('-', '-')],
                        max_length=8,
                        verbose_name='sex',
                    ),
                ),
                (
                    'sex2',
                    models.CharField(
                        blank=True,
                        choices=[('Man', 'Man'), ('Female', 'Female'), ('-', '-')],
                        max_length=8,
                        verbose_name='sex',
                    ),
                ),
                (
                    'age',
                    models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='age'),
                ),
                (
                    'balance',
                    models.DecimalField(
                        decimal_places=2, default=0.0, max_digits=8, verbose_name='balance'
                    ),
                ),
                ('score', models.PositiveIntegerField(default=0, verbose_name='score')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                (
                    'created_time',
                    models.DateTimeField(auto_now_add=True, verbose_name='created time'),
                ),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='updated time')),
            ],
            options={
                'verbose_name': 'A',
                'verbose_name_plural': 'As',
            },
        ),
        migrations.CreateModel(
            name='B',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    ),
                ),
                (
                    'a',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to='app.a', verbose_name='A'
                    ),
                ),
            ],
            options={
                'verbose_name': 'B',
                'verbose_name_plural': 'Bs',
            },
        ),
    ]
