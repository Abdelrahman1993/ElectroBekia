# Generated by Django 2.2.1 on 2019-05-27 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_auto_20190527_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='status',
            field=models.CharField(choices=[('r', 'تم رفض اللسعر'), ('a', 'تم قبول السعر')], max_length=5),
        ),
    ]
