# Generated by Django 4.1.4 on 2023-08-20 04:38

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0006_connectionhistory'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='connectionhistory',
            unique_together={('user',)},
        ),
        migrations.RemoveField(
            model_name='connectionhistory',
            name='device_id',
        ),
    ]
