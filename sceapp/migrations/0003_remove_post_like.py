# Generated by Django 5.1.3 on 2024-11-26 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sceapp', '0002_post_delete_schedulemanage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='like',
        ),
    ]
