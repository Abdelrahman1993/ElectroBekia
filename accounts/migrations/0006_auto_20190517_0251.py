# Generated by Django 2.2.1 on 2019-05-17 02:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20190517_0239'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='category_category',
            new_name='user_category',
        ),
    ]
