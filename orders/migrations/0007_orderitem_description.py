# Generated by Django 2.2.1 on 2019-05-22 06:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_orderimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='description',
            field=models.TextField(default="", max_length=500, validators=[django.core.validators.MinLengthValidator(150)]),
            preserve_default=False,
        ),
    ]