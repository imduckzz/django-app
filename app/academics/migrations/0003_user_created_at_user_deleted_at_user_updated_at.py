# Generated by Django 5.0.2 on 2024-03-11 16:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0002_user_ident_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 11, 11, 12, 1, 648797)),
        ),
        migrations.AddField(
            model_name='user',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 11, 11, 12, 1, 648797)),
        ),
    ]
