# Generated by Django 2.2.1 on 2019-05-27 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20190522_0710'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='status',
            field=models.CharField(choices=[('w', 'قي انتظار الرد'), ('r', 'تم رفض اللسعر'), ('a', 'تم قبول السعر')], default='w', max_length=5),
        ),
    ]
