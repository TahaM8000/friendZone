# Generated by Django 4.1 on 2022-09-09 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_alter_user_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='Friends',
        ),
    ]