# Generated by Django 2.2.1 on 2019-05-22 05:08

from django.db import migrations, models
import django.db.models.deletion
import orders.models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_delete_orderimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to=orders.models.get_file_path)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.OrderItem')),
            ],
        ),
    ]
