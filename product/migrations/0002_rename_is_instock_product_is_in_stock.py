# Generated by Django 4.1.5 on 2023-01-21 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='is_instock',
            new_name='is_in_stock',
        ),
    ]
