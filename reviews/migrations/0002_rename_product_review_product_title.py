# Generated by Django 3.2.15 on 2023-02-16 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='product',
            new_name='product_title',
        ),
    ]
