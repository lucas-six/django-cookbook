# Generated by Django 4.2.18 on 2025-02-02 09:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('app', '0003_a_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='a',
            name='group',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='auth.group',
                verbose_name='Group',
            ),
        ),
    ]
