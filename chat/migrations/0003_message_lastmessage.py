# Generated by Django 4.1.4 on 2023-08-18 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='lastmessage',
            field=models.TextField(blank=True, null=True),
        ),
    ]
