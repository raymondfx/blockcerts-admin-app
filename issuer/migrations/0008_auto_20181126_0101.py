# Generated by Django 2.1.3 on 2018-11-26 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issuer', '0007_auto_20181126_0006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='credential',
            name='associated_filename',
        ),
        migrations.AddField(
            model_name='issuance',
            name='associated_filename',
            field=models.CharField(default='', max_length=50),
        ),
    ]
