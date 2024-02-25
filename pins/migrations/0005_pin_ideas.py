# Generated by Django 5.0.2 on 2024-02-23 15:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0001_initial'),
        ('pins', '0004_delete_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='pin',
            name='ideas',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, related_name='ideas', to='ideas.idea'),
            preserve_default=False,
        ),
    ]