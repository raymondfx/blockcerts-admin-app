# Generated by Django 2.1.3 on 2018-11-26 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issuer', '0006_auto_20181124_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personissuances',
            name='is_issued',
            field=models.BooleanField(default=False),
        ),
    ]
