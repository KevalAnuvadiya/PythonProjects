# Generated by Django 4.1.3 on 2023-03-12 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_task_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='user',
        ),
    ]
