# Generated by Django 3.2.4 on 2022-10-01 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_wxchat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.CharField(max_length=15, verbose_name='手机号'),
        ),
    ]
