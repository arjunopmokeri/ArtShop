# Generated by Django 3.1.3 on 2020-12-25 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='place',
            new_name='price',
        ),
    ]