# Generated by Django 4.1 on 2022-08-08 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_city_options_user_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='east',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='city',
            name='north',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
