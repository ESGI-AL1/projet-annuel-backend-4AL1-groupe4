# Generated by Django 5.0.4 on 2024-04-20 13:16

import api.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_program_file'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='programs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='program',
            name='file',
            field=models.FileField(blank=True, default=True, upload_to=api.models.get_unique_filename),
        ),
    ]
